import logging
from flask import Blueprint, request
from models.game_set import GameSet
from repositories.game_set_repository import GameSetRepository

game_set_api = Blueprint('game_set_api', __name__)

@game_set_api.route("/<int:group>/<int:year>/<int:week>", methods=["GET"])
def get_game_set(group: int, year: int, week: int):
    doc = GameSetRepository().get_by_week(group, year, week)
    logging.info(f"group: {group} year: {year} week: {week}")
    return doc.to_dict()

@game_set_api.route("/", methods=["POST"])
def game_set_create():
    game_set = GameSet.from_dict(request.get_json())
    GameSetRepository().create(game_set)
    return game_set.to_dict(), 200
