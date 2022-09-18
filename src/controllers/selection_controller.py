from flask import Blueprint, current_app, request
from models.selection import Selection
from repositories.selection_repository import SelectionRepository
from validators.validate_headers import authorize

selection_api = Blueprint('selection_api', __name__)

@selection_api.route("/", methods=["POST"])
@authorize
def create_selection(user):
    selection = Selection.from_dict(request.get_json(), infer_missing=True)
    selection.user_id = user["email"]
    SelectionRepository().create(selection)
    return selection.to_dict(), 200

@selection_api.route("/batch/", methods=["POST"])
@authorize
def create_batch_selections(user):
    selections = Selection.schema().load(request.get_json(), many=True)
    for selection in selections:
        selection.user_id = user["email"]
    SelectionRepository().create_batch(selections)
    return [selection.to_dict() for selection in selections], 200

@selection_api.route("/mine/<game_set_id>/", methods=["GET"])
@authorize
def get_my_selections(game_set_id, user):
    current_app.logger.info(user)
    selections = SelectionRepository().get_by_gameset(game_set_id, user)
    return [s.to_dict() for s in selections], 200
