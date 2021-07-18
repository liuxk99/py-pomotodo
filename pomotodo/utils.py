#!/usr/bin/python
# coding=utf-8
from jproperties import Properties


def load(properties_file):
    p = Properties()
    with open(properties_file, "rb") as f:
        p.load(f, "utf-8")

    return p


import json


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
