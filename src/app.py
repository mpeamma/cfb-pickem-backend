from flask import Flask
import os
import cfbd
from cfbd.rest import ApiException
from pprint import pprint
from controllers.group_controller import groups_api
import firebase_admin
from firebase_admin import firestore

app = Flask(__name__)

app.register_blueprint(groups_api, url_prefix="/groups")


# Application Default credentials are automatically created.
firestore_app = firebase_admin.initialize_app()
db = firestore.client()

@app.route("/games")
def get_games():
    API_KEY=os.environ.get("API_KEY")
    configuration = cfbd.Configuration()
    configuration.api_key['Authorization'] = API_KEY
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    configuration.api_key_prefix['Authorization'] = 'Bearer'

    # create an instance of the API class
    api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
    year = 2022

    try:
        # Season calendar
        api_response = api_instance.get_calendar(year)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->get_calendar: %s\n" % e)

    return {"foo": "bar"}

if __name__ == "__main__":
    app.run(host="0.0.0.0")
