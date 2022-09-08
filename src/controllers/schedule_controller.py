from flask import Blueprint
from cfbd import GamesApi
from config.cfbd import CFBDClient

schedule_api = Blueprint('schedule_api', __name__)

@schedule_api.route("/<year>/<week>", methods=["GET"])
def get_schedule(year, week):
    api_instance = GamesApi(CFBDClient.instance())
    api_response = api_instance.get_games(int(year), week=int(week), division="fbs")
    return [x.to_dict() for x in api_response]
