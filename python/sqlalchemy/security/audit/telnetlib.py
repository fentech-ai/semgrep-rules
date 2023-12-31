# cf. https://github.com/PyCQA/bandit/blob/d5f8fa0d89d7b11442fc6ec80ca42953974354c8/examples/telnetlib.py

import getpass
import telnetlib

host = sys.argv[1]

username = raw_input("Username:")
password = getpass.getpass()
# ruleid:telnetlib
tn = telnetlib.Telnet(host)

tn.read_until("login: ")
tn.write(username + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ## Il we have hierarchy then create regulator
        regs = [self.preproc.get_reg()] if self.preproc.aggregator is not None else None

        ##
        df_matrix = df_matrix.loc[
            df_matrix.index.sort_values(), df_matrix.columns.sort_values()
        ]

        ## Fit model
        optim_params = optim_params if optim_params is not None else {}
        self.model.fit(df_matrix, regs=regs, **optim_params)

    def _check(self, df, sc):
        ## Check dataframe
        if not pd.core.dtypes.common.is_datetime_or_timedelta_dtype(df[sc.date]):
            raise ValueError("Date must be TimeStamp")

        nan_values = df.isna().sum() > 0
        if nan_values.any():
            raise ValueError(f"DataFrame has nan values {nan_values}")

    def _build_model(self, factors_params, df):

        ## Init model
        constraints = factors_params.get("constraints", None)
        model = factors_model.FactorModel(constraints=constraints, sc=self.sc)

        ## Add factors
        for factor_params in factors_params["factors"]:
            ## fit factor required
            f_callable = factor_params["f_callable"]
            if hasattr(f_callable, "fit"):
                f_callable.fit(df=df, sc=self.sc)

            ## Add factor to model
            model.add_factor(**factor_params)

        return model

    def predict(
        self, steps=None, freq=None, start_date=None, products=None, dates=None
    ):

        if dates is None and steps is None:
            raise TypeError("predict must have either dates or steps given")

        if dates is None:

            ## Define dates from steps and freq
            if start_date is None:
                ## check signature
                if freq is None:
                    raise TypeError("predict must have either dates or freq given")
                ## Define dates starting from start_date+freq
                dates = pd.date_range(self.end_date, periods=steps + 1, freq=freq)[1:]
            else:
                ## Define date range
                dates = pd.date_range(start_date, periods=steps, freq=freq)

        ## Convert date
        dates = pd.to_datetime(dates)

        ## Define time_index and products index
        time_index = self.preproc.date_to_index(dates)
        products_index = (
            self.preproc.product_to_index(products) if products is not None else None
        )

        ## Get prediction for defined products
        sales_matrix = self.model.predict(time=time_index, products=products_index)

        ## Get df from sales matrix
        df = self.preproc.inverse_transform(sales_matrix)

        ##
        ## CAN BE MODIFIED LATER
        if True and self.preproc.aggregator is not None:
            df = df[df[self.sc.product].isin(self.preproc.aggregator.ts_leaves)]

        return df

    def sample_predict(self, freq=pd.to_timedelta("1D")):

        steps = (self.end_date - self.start_date) / freq + 1
        yp = self.predict(steps=steps, start_date=self.start_date, freq=freq)

        return yp

    @classmethod
    def read_dict(cls, params_dict, df, api_sc=None, sc=None, fit=False):

        ## Copy dict
        params_dict = deepcopy(params_dict)

        ## Define schma
        sc = sc if sc is not None else C.schema
        api_sc = api_sc if api_sc is not None else None

        ## Read date range to normalize factor params
        date_range = (df[sc.date].max() - df[sc.date].min()) / pd.to_timedelta("1D")
        width = date_range * 1.2

        ## Define init and fit params dict
        fit_params = {}
        init_params = {"sc": sc}

        ## Sclae is used to set time parameter to vary between O and 1 and ease optimization
        for param_key, t_params in params_dict["factors"].items():

            ## Define default_args as an empyt dict if not given
            if "default_args" not in t_params.keys():
                t_params["default_args"] = {}

            ## Define factor name from key
            t_params["name"] = param_key

            ## Define a callable function to use for the factor
            if param_key in cls._FUNCTIONS_MAP.keys():
                t_params["f_callable"] = cls._FUNCTIONS_MAP[param_key]
            else:
                raise ValueError(f"No function implemented for {param_key} factor")

            ## Define default size as 1
            t_params["size"] = t_params.get("size", 1)

        ## Define factor_model params
        factor_model_params = {
            "factors": list(params_dict["factors"].values()),
            "constraints": params_dict.get("constraints", None),
        }

        ## Drop None values
        factor_model_params = {
            key: value
            for key, value in factor_model_params.items()
            if value is not None
        }
        ## Get optim params
        optim_params = {
            "ga_params": params_dict.get("ga_params", None),
            "lo_params": params_dict.get("lo_params", None),
        }

        ## Drop None values
        optim_params = {
            key: value for key, value in optim_params.items() if value is not None
        }

        ## Define fit params
        fit_params = {
            "preproc_params": {
                "freq": pd.to_timedelta("1D"),
                "agg_params": params_dict.get("agg_params"),
                "norm_params": params_dict.get("norm_params"),
            },
            "factors_params": factor_model_params,
            "optim_params": optim_params,
        }

        if fit:
            model = cls(**init_params)
            model.fit(df=df, **fit_params)
            return model
        else:
            return init_params, fit_params

    def save(self, output):
        import joblib

        joblib.dump(self, output)

    def extract_factors(self, dates):

        sc = self.sc

        ## Get matrix factors
        data = {}
        for key, factor in self.model.h_factors.items():
            key = key[0] + "__" + str(key[1])
            data[key] = factor(dates)
        data = pd.DataFrame(data)
        data[sc.date] = dates

        ## Get coefs
        m = self.model.get_weights()["hmatrix"]
        products = self.preproc.index_to_product(range(m.shape[0]))

        columns = [f"{key[0]}__{key[1]}" for key in self.model.h_factors.keys()]
        x = pd.DataFrame(m)
        x.columns = columns
        x.index = products
        x = x.reset_index().rename(columns={"index": sc.product})

        data = data.merge(x, how="cross", suffixes=("", "_coef"))
        for col in columns:
            factor_col = col + "_coef"
            data[factor_col] = data[factor_col] * data[col]

        return data
