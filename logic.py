from typing import List
from datetime import date

import model
import db

TITLE_LIMIT = 30
TEXT_LIMIT = 200

today = date.today()
date_create = today.strftime("%Y-%m-%d")


class LogicException(Exception):
    pass


class AventLogic:
    def __init__(self):
        self._avent_db = db.AventDB()

    @staticmethod
    def _validate_avent(avent: model.Avent):
        if avent is None:
            raise LogicException("avent is None")
        if avent.date is None or avent.date == date_create:
            raise LogicException(f'check the creation date')
        if avent.title is None or len(avent.title) > TITLE_LIMIT:
            raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
        if avent.text is None or len(avent.text) > TEXT_LIMIT:
            raise LogicException(f"text length > MAX: {TEXT_LIMIT}")

    def create(self, avent: model.Avent) -> str:
        self._validate_avent(avent)
        try:
            return self._avent_db.create(avent)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Avent]:
        try:
            return self._avent_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Avent:
        try:
            return self._avent_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, avent: model.Avent):
        self._validate_avent(avent)
        try:
            return self._avent_db.update(_id, avent)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str) -> object:
        try:
            return self._avent_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
