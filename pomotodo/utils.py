#!/usr/bin/python
# coding=utf-8
from jproperties import Properties


def load(properties_file):
    p = Properties()
    with open(properties_file, "rb") as f:
        p.load(f, "utf-8")

    return p
