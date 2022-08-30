from typing import Generic, Type, TypeVar, ClassVar
from dataclasses_json import DataClassJsonMixin
from repositories.firestore_connection import FirestoreConnection

T = TypeVar("T", bound=DataClassJsonMixin)

class FirestoreRepository(Generic[T]):

    object_class: ClassVar[Type[T]]

    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.db = FirestoreConnection.instance()

    def create(self, item: T):
        doc_ref = self.db.collection(self.collection_name).document(item.id)
        doc_ref.set(item.to_dict())
        return item

    def get_all(self):
        coll_ref = self.db.collection(self.collection_name)
        docs = [self.object_class.from_dict(x.to_dict()) for x in coll_ref.stream()]
        return docs
