from flask import Blueprint, request
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
