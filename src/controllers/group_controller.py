import uuid
from flask import Blueprint, request, current_app
from models.group import Group
from repositories.game_set_repository import GameSetRepository
from repositories.group_repository import GroupRepository
from validators.validate_headers import authorize

groups_api = Blueprint('group_api', __name__)

@groups_api.route("/", methods=["GET"])
def groups_list():
    docs = GroupRepository().get_all()
    return Group.schema().dumps(docs, many=True)

@groups_api.route("/<group_id>", methods=["GET"])
def get_group(group_id):
    group = GroupRepository().get_by_id(group_id)
    if group.exists:
        gamesets = GameSetRepository().get_by_group(group_id)
        resp = group.to_dict()
        resp["gamesets"] = [x.to_dict() for x in list(gamesets)]
        return resp, 200
    else:
        return "", 204

@groups_api.route("/", methods=["POST"])
@authorize
def group_create(user):
    group = Group.from_dict(request.get_json())
    group.creator = user["email"]
    group.id = str(uuid.uuid4())
    GroupRepository().create(group)
    return group.to_dict(), 200

@groups_api.route("/mine", methods=["GET"])
@authorize
def get_my_groups(user):
    groups = GroupRepository().get_by_user(user)
    return [x.to_dict() for x in groups]
