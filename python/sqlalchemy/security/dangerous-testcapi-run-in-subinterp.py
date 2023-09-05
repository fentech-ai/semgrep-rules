from test import support

import flask

app = flask.Flask(__name__)


@app.route("/route_param/<route_param>")
def route_param(route_param):

    # ruleid: dangerous-testcapi-run-in-subinterp
    support.run_in_subinterp(route_param)

    return "oops!"


# Flask true negatives
@app.route("/route_param/<route_param>")
def route_param2(route_param):

    # ok: dangerous-testcapi-run-in-subinterp

    return "ok!"
