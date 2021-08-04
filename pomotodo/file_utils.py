#!/usr/bin/python
# coding=utf-8
import codecs


def read(filename):
    with codecs.open(filename, "r", "utf-8-sig") as f:
        text = f.read()
    return text


def write(filename, text):
    with codecs.open(filename, "w", "utf-8-sig") as f:
        f.write(text)
    pass
