from models.game_set import GameSet
from repositories.firestore_repository import FirestoreRepository


class GameSetRepository(FirestoreRepository[GameSet]):
    object_class = GameSet

    def __init__(self):
        super().__init__("game_sets")

    def get_by_week(self, group: str, year: int, week: int):
        coll = self.db.collection(self.collection_name)
        query = coll.where("week", "==", week).where("group_id", "==", group).where("year", "==", year)
        return next(query.stream())
