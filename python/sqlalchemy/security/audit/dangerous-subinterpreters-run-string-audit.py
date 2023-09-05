from typing import Optional

import pandas as pd
from pydantic import BaseModel


class Request(BaseModel):
    """
    Model to represent the response after processing a job.

    Attributes
    ----------
    company_id: str
        The unique identifier of the company for which the job was processed.
    job_id: int
        The unique identifier of the job.
    initial_request: dict
        A dictionary containing the initial request parameters for the job.
    simulation_id: Optional[int]
        An optional identifier for the simulation related to the job.
    """

    company_id: str
    job_id: int
    initial_request: dict
    simulation_id: Optional[int]


def nested_crossval(data, T, nb_max=None):
    """
    nested_crossval is a function dedicated to build
    nested crossvaldation datasets for time series.

    input:
    ------
        data : np.array : timeseries array to split in various ways (timeseries x dates)
        T : integer : number of timestep to forecast
        nb_max : integer : maximum number of cross validation data

    output:
    -------
        dikt_data_nested : dict : dictionnary for cross val datasets.

    """
    dikt_data_nested = {}
    i = 1
    if nb_max is None:
        nb_max = data.shape[i]
    while data.shape[1] - T * i > 10 and i <= nb_max:
        t_splt = data.shape[1] - T * i
        res_x = data[:, :t_splt].copy()
        res_y = data[:, t_splt : t_splt + T].copy()
        dikt_data_nested[i] = {"x": res_x, "y": res_y}
        i = i + 1
    if i == 1:
        return None
    else:
        return dikt_data_nested


def funk_reformat1(data):
    """
    Function that turns a data frame stackedd in to the format we need for the prediction

    input:
        data: pandas data frame

    output :
        res : dataframe : output data with the right format
    """

    # on suppose que data['Date'] est deja un pd.TimeStampIndex, sinon
    # faire : data['Date'] = pd.to_datetime(data.Date)
    ts = data.groupby(
        [x for x in data.columns if x not in ["Date", "Sales", "Stock", "Turnover"]]
        + ["Date"]
    )
    return ts.sum()["Sales"].unstack().fillna(0)


def split_train_test(data, time, T, nb_max=None):
    """
    split_train_test is a function that builds a set of nested data for cross
    validation, a train data set and a test dataset.

    input:
    ------
        data : np.array : timeseries array to split in various ways (timeseries x dates)
        time : integer : index of the data to split train and test.
        T : integer : number of timestep to forecast
        nb_max : integer : maximum number of cross validation data

    output:
    -------
        [dikt_data_nested, data_train, data_test] : list of dixt and np.array : list of
                           nested data , train data and test data
    """
    data_train = data[:, :time]
    data_test = data[:, time : time + T]
    dikt_cross = nested_crossval(data_train, T, nb_max)
    return [dikt_cross, data_train, data_test]


def load_data(element):
    """
    This function aims at turning the data in to a the right format for prediction
    """
    data = element["data"]
    freq = element["freq"]
    T = element["T"]
    nbm = element["nbm"]

    if freq is None:
        freq = "W-SUN"
    if not isinstance(data, pd.DataFrame):
        data = pd.read_json(data)

    # Adding some aliases
    data = data.rename(
        columns={
            "Sale": "Sales",
            "Stocks": "Stock",
            "Store": "StoreID",
            "Boutique": "StoreID",
            "SKU": "ProductID",
            "sku": "ProductID",
            "ItemID": "ProductID",
        }
    )
    if any(i not in data.columns for i in ["Date", "Sales", "ProductID"]):
        missing_fields = [
            i not in data.columns
            for i in ["Date", "Sales", "ProductID", "Price", "StoreID"]
        ]
        raise ValueError(f"Missing Fields {missing_fields}")

    if "StoreID" not in data.columns:
        data["StoreID"] = "All"

    # WARNING: Horribly Dangerous! - REMOVED -
    # data.columns = ["Date", "Sales", "ProductID", "Stocks", "Price", "Store"]
    data2 = data.groupby(["Date", "ProductID", "StoreID"]).sum()
    data2 = data2.loc[:, ["Sales"]].reset_index()
    data2 = funk_reformat1(data2)
    data2 = data2.T.copy()
    data2["Date"] = pd.to_datetime(data2.index.values)
    data2 = data2.groupby([pd.Grouper(key="Date", freq=freq)]).sum()
    data2 = data2.T
    #### CROSSVAL SPLITTING
    time = data2.shape[1] - T
    list_of_data = split_train_test(data2.values, time, T, nb_max=nbm)
    return [data2, list_of_data, data]


def format_output(prediction, idx, dates, freq, horizon):
    res_dates = pd.to_datetime(dates[-1])
    ldate = list(pd.date_range(res_dates, freq=freq, periods=horizon + 1))[1:]
    res = pd.DataFrame(prediction, columns=ldate)
    res.index = idx
    res.columns.name = "Date"
    return res.T.unstack().reset_index().rename(columns={0: "Demand"})
