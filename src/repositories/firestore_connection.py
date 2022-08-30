from firebase_admin import firestore

class FirestoreConnection():
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = firestore.client()
        return cls._instance