from flask import Blueprint
from firebase_admin import firestore
from models.group import Group
from repositories.group_repository import GroupRepository

groups_api = Blueprint('group_api', __name__)

@groups_api.route("/", methods=["GET"])
def groups_list():
    docs = GroupRepository().get_all()
    return Group.schema().dumps(docs, many=True)

@groups_api.route("/", methods=["POST"])
def groups_create():
    db = firestore.client()
    doc_ref = db.collection('groups').document('12345')
    doc_ref.set({
        'id': 12345,
        'name': 'First',
    })
    return '', 200
