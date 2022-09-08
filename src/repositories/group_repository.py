from models.group import Group
from repositories.firestore_repository import FirestoreRepository


class GroupRepository(FirestoreRepository[Group]):
    object_class = Group

    def __init__(self):
        super().__init__("groups")

    def get_by_user(self, user):
        coll = self.db.collection(self.collection_name)
        query = coll.where("user_ids", "array_contains", user["email"])
        return query.stream()
