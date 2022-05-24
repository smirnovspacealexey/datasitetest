import json
from random import randrange

import requests

from .settings import API_URL


def get_forms_uids():
    data = {
        "jsonrpc": "2.0",
        "id": randrange(1000000000),
        "method": "get-uids",
    }

    r = requests.post(API_URL, data=data)
    response = json.loads(r.content.decode("utf-8"))

    if "result" in response:
        return response["result"]

    return None


class APIForm:
    def __init__(self, form_uid):
        self.form_uid = form_uid

    def get_rows(self):
        data = {
            "jsonrpc": "2.0",
            "id": randrange(1000000000),
            "method": "get-rows",
            "params": [self.form_uid, ]
        }

        r = requests.post(API_URL, data=data)
        response = json.loads(r.content.decode("utf-8"))
        if "result" in response:
            return response["result"]
        return None

    def set_result(self, result):
        result.update({"uid": self.form_uid})
        data = {
            "jsonrpc": "2.0",
            "id": randrange(1000000000),
            "method": "set-result",
            "params": str(result).replace("'", '"').replace("None", "null")
        }

        r = requests.post(API_URL, data=data)
        response = json.loads(r.content.decode("utf-8"))
        if "result" in response:
            return response["result"]
        return False

    def get_result(self):
        data = {
            "jsonrpc": "2.0",
            "id": randrange(1000000000),
            "method": "get-result",
            "params": [self.form_uid, ]
        }

        r = requests.post(API_URL, data=data)
        response = json.loads(r.content.decode("utf-8"))
        if "result" in response:
            return response["result"]
        return None

