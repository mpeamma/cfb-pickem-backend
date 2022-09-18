from flask import Blueprint, request
from models.game_set import GameSet
from repositories.game_set_repository import GameSetRepository
from cfbd import GamesApi
from config.cfbd import CFBDClient

game_set_api = Blueprint('game_set_api', __name__)

@game_set_api.route("/<string:group>/<int:year>/<int:week>/", methods=["GET"])
def get_game_set(group: str, year: int, week: int):
    api_instance = GamesApi(CFBDClient.instance())
    api_response = api_instance.get_games(int(year), week=int(week), division="fbs")
    gameset = GameSetRepository().get_by_week(group, year, week).to_dict()
    gamelist = []
    for game_id in gameset["games"]:
        game = next((x for x in api_response if x.id == game_id), None)
        gamelist.append(game.to_dict())
    gameset["games"] = gamelist
    return gameset

@game_set_api.route("/", methods=["POST"])
def create_game_set():
    game_set = GameSet.from_dict(request.get_json())
    GameSetRepository().create(game_set)
    return game_set.to_dict(), 200
