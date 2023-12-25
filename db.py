from typing import List

import model
import storage


class DBException(Exception):
    pass


class AventDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, avent: model.Avent) -> str:
        try:
            return self._storage.create(avent)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Avent]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Avent:
        try:
            return self._storage.read(_id)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _id: str, avent: model.Avent):
        try:
            return self._storage.update(_id, avent)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
