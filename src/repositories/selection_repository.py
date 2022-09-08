from models.selection import Selection
from repositories.firestore_repository import FirestoreRepository


class SelectionRepository(FirestoreRepository[Selection]):
    object_class = Selection

    def __init__(self):
        super().__init__("selections")