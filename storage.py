from typing import List

import model


class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}

    def create(self, avent: model.Avent) -> str:
        self._id_counter += 1
        avent.id = str(self._id_counter)
        self._storage[avent.id] = avent
        return avent.id

    def list(self) -> List[model.Avent]:
        return list(self._storage.values())

    def read(self, _id: str) -> model.Avent:
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        return self._storage[_id]

    def update(self, _id: str, avent: model.Avent):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        avent.id = _id
        self._storage[avent.id] = avent

    def delete(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        del self._storage[_id]
