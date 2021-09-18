# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask
from api_calls import add_btc_price
from push_notification import send_sms
from level_watcher import gas_push_calculation

# https://cloud.google.com/debugger/docs/setup/python
# Note - install libraries globally
try:
    import googleclouddebugger
    googleclouddebugger.enable(
        breakpoint_enable_canary=True
    )
except ImportError:
    pass


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def endpoints():
    """Return endpoint options."""
    return "/btcprice"


@app.route('/btcprice')
def price():
    """Return BTC to USD Price."""
    return add_btc_price()

@app.route('/sendsms')
def sms():
    """Return push notification."""
    return send_sms()

@app.route('/check_gas')
def gas():
    """Return gas level check"""
    return gas_push_calculation


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
