import os
import json
from fxdayu_dataz.IO import MONGO, FREQ, FILES, STOCK, STORAGE, CODES, MARKETINDEX, LOG


root = os.path.join(os.environ.get("fxdayu", os.path.expanduser("~/.fxdayu")), "dataz")


def path(name=''):
    return os.path.join(root, name)


def get_storage():
    if os.path.exists(path(STORAGE)):
        return json.load(
            open(path(STORAGE))
        )
    else:
        from fxdayu_dataz.IO.default import storage
        return storage


def get_files():
    return get_storage().get(FILES, "/data")


def get_mongo():
    return get_storage()[MONGO]


def get_codes():
    if os.path.exists(path(CODES)):
        return json.load(
            open(path(CODES))
        )
    else:
        from fxdayu_dataz.IO.codes import codes
        return codes