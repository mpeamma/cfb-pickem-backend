from datetime import datetime
from flask import Blueprint
from cfbd import GamesApi
from config.cfbd import CFBDClient

schedule_api = Blueprint('schedule_api', __name__)

@schedule_api.route("/<year>/<week>", methods=["GET"])
def get_schedule(year, week):
    api_instance = GamesApi(CFBDClient.instance())
    api_response = api_instance.get_games(int(year), week=int(week), division="fbs")
    return [x.to_dict() for x in api_response]

@schedule_api.route("/current")
def current_week():
    api_instance = GamesApi(CFBDClient.instance())
    today = datetime.now()
    api_response = api_instance.get_calendar(today.year)
    week_num = 1
    for week in api_response:
        start_time = datetime.strptime(week.first_game_start, '%Y-%m-%dT%H:%M:%S.%fZ')
        if today > start_time:
            week_num += 1
        else:
            return f"{week_num}", 200

    return f"{week_num}", 200
