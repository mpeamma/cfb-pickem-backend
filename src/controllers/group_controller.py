from flask import Blueprint, request
from models.group import Group
from repositories.group_repository import GroupRepository
from validators.validate_headers import authorize

groups_api = Blueprint('group_api', __name__)

@groups_api.route("/", methods=["GET"])
def groups_list():
    docs = GroupRepository().get_all()
    return Group.schema().dumps(docs, many=True)

@groups_api.route("/", methods=["POST"])
@authorize
def groups_create(user):
    group = Group.from_dict(request.get_json())
    GroupRepository().create(group)
    return group.to_dict(), 200

@groups_api.route("/mine", methods=["GET"])
@authorize
def get_my_groups(user):
    groups = GroupRepository().get_by_user(user)
    return [x.to_dict() for x in groups]
