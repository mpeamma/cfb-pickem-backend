from typing import Generic, List, Type, TypeVar, ClassVar
import uuid
from dataclasses_json import DataClassJsonMixin
from repositories.firestore_connection import FirestoreConnection

T = TypeVar("T", bound=DataClassJsonMixin)

class FirestoreRepository(Generic[T]):

    object_class: ClassVar[Type[T]]

    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.db = FirestoreConnection.instance()

    def get_by_id(self, item_id):
        doc_ref = self.db.collection(self.collection_name).document(item_id)
        return doc_ref.get()

    def create(self, item: T):
        doc_ref = self.db.collection(self.collection_name).document(item.id)
        doc_ref.set(item.to_dict())
        return item

    def create_batch(self, items: List[T]):
        batch = self.db.batch()
        for item in items:
            id = str(uuid.uuid4())
            item.id = id
            docRef = self.db.collection(self.collection_name).document(id)
            batch.set(docRef, item.to_dict())
        batch.commit()

    def get_all(self):
        coll_ref = self.db.collection(self.collection_name)
        docs = [self.object_class.from_dict(x.to_dict()) for x in coll_ref.stream()]
        return docs
