from models.group import Group
from repositories.firestore_repository import FirestoreRepository


class GroupRepository(FirestoreRepository[Group]):
    object_class = Group

    def __init__(self):
        super().__init__("groups")