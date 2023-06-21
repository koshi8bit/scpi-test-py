from flask import Flask
from waitress import serve
import logging

app = Flask(__name__)


@app.route("/")
def root():
    return """hello world <br><br>
    <a href="/api/v1/channels">/api/v1/channels</a><br>
    <a href="/api/v1/channels/elv">/api/v1/channels/elv</a><br>
    <a href="/api/v1/channels/elv/dark">/api/v1/channels/elv/dark</a><br>
    """


@app.route("/api/v1/channels/")
def api_v1_channels():
    elv = {
        "dark": 2.3,
        "voltage": 980
    }

    result = {
        "bergoz": 1.6,
        "beam0": 1.3,
        "elv": elv
    }

    return result


@app.route("/api/v1/channels/elv")
def api_v1_channels_elv():
    elv = {
        "dark": 2.3,
        "voltage": 980
    }

    return elv


@app.route("/api/v1/channels/elv/dark")
def api_v1_channels_elv_dark():
    return {"dark": 2.3}


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.warning("init ok")

    # serve(app, host='0.0.0.0', port=5053) USE IN PRODUCTION
    app.run(host='0.0.0.0', port=5052)
