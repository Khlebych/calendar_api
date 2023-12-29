from flask import Flask
from flask import request

app = Flask(__name__)

import model
import logic

_avent_logic = logic.AventLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_avent: str) -> model.Avent:
    parts = raw_avent.split('|')
    if len(parts) == 3:
        avent = model.Avent()
        avent.id = None
        avent.date = parts[0]
        avent.title = parts[1]
        avent.text = parts[2]
        return avent
    elif len(parts) == 4:
        avent = model.Avent()
        avent.id = parts[0]
        avent.date = parts[1]
        avent.title = parts[2]
        avent.text = parts[3]
        return avent
    else:
        raise ApiException(f"invalid RAW avent data {raw_avent}")


def _to_raw(avent: model.Avent) -> str:
    if avent.id is None:
        return f"{avent.date}|{avent.title}|{avent.text}"
    else:
        return f"{avent.id}|{avent.date}|{avent.title}|{avent.text}"


API_ROOT = "/api/v1"
CALENDAR_API_ROOT = API_ROOT + "/calendar"

#avents = []


@app.route(CALENDAR_API_ROOT + "/", methods=["POST"])
def create():
    try:
        date = request.get_data().decode('utf-8')
        avent = _from_raw(date)
        _id = _avent_logic.create(avent)
        return f"new id: {_id}", 201

    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/", methods=["GET"])
def list():
    try:
        avents = _avent_logic.list()
        raw_avents = ""
        for avent in avents:
            raw_avents += _to_raw(avent) + '\n'
        return raw_avents, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        avent = _avent_logic.read(_id)
        raw_avent = _to_raw(avent)
        return raw_avent, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        date = request.get_data().decode('utf-8')
        avent = _from_raw(date)
        _avent_logic.update(_id, avent)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _avent_logic.delete(_id)
        # avents = _avent_logic.list()
        # avents.pop(int(_id)-1)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
