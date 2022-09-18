from models.selection import Selection
from repositories.firestore_repository import FirestoreRepository


class SelectionRepository(FirestoreRepository[Selection]):
    object_class = Selection

    def __init__(self):
        super().__init__("selections")

    def get_by_gameset(self, game_set_id, user):
        coll = self.db.collection(self.collection_name)
        query = coll.where("game_set_id", "==", game_set_id).where("user_id", "==", user["email"])
        return query.stream()