#!/usr/bin/python
# coding=utf-8
from jproperties import Properties

from pomotodo import datetime_utils


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


def hms(seconds):
    """
    总计 7 小时 27 分钟
    """
    ss = seconds % 60
    minutes = (seconds - ss) / 60
    mm = minutes % 60
    hh = (minutes - mm) / 60
    return hh, mm, ss


def gen_todos_snap_filename():
    csv_filename_date = datetime_utils.local_today().strftime("%Y%m%d")
    csv_filename = 'todos-%s.csv' % (csv_filename_date)
    return csv_filename


def dump_pomos_simple(pomos):
    i = 0
    seconds = 0
    for item in pomos:
        i = i + 1
        seconds += item.duration()
        print(item.to_markdown())
    h, m, s = utils.hms(seconds)
    print("完成了 %d 个番茄, 总计 %d 小时 %d 分钟 %d 秒" % (i, h, m, s))