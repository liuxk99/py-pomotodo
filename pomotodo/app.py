# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        pomo
# Purpose:      python client for pomotodo
#
# Author:      thomas
#
# Created:     01/04/2020
# Copyright:   (c) thomas 2020
# Licence:     <your licence>
# coding=utf-8
# -------------------------------------------------------------------------------
import csv
import os
from datetime import timedelta

from pomotodo import datetime_utils, pomo, todo, utils
from pomotodo.utils import dump_pomos_simple


def generate_today_todos(client):
    plan_todo = "#时间管理 '日'·计划"
    weather_todo = "#生活/日常 '天气<应用:墨迹天气>'"
    attendance_todo = "#公司(乐视)/管理 '考勤'"
    mail_todo = "#日常/办公 '邮件'"
    zhimi_todo = "#人文/语言(英语) '单词<应用:知米背单词>'"
    shanbei_todo = "#人文/语言(英语) '单词<应用:扇贝单词>'"
    walk_todo = "#生命/健康 '锻炼'·散步"
    record_todo = "#时间管理 '日'·记录"
    summary_todo = "#时间管理 '日'·总结"
    todo_list = [plan_todo, weather_todo, attendance_todo, mail_todo, zhimi_todo, shanbei_todo, walk_todo,
                 record_todo, summary_todo]

    today_todos = []
    date = datetime_utils.local_today()
    for item in todo_list:
        todo_text = "%s %s" % (item, date.strftime("|%Y/%m/%d"))
        todo_item = client.post_todo(todo_text)
        if todo_item:
            today_todos.append(todo_item)
        print(todo_item)

    today_todos.reverse()
    for item in today_todos:
        client.pin_todo(item.uuid)

    for item in today_todos:
        client.unpin_todo(item.uuid)

    return None


def get_pomos_date(client, date):
    started_later_than = date
    started_earlier_than = date + timedelta(days=1)

    pomos = client.get_pomos(started_later_than, started_earlier_than)
    # dump_pomos(pomos)
    pomos_manual = client.get_pomos(started_later_than, started_earlier_than, True)
    # dump_pomos(pomos_manual)
    for e in pomos_manual:
        pomos.append(e)
    pomos.sort(key=pomo.sort_key)
    print(datetime_utils.to_local(started_later_than).strftime("%Y/%m/%d"))
    print("---")
    dump_pomos_simple(pomos)


def snap_todos(todos, csv_filename):
    print('snap_todos("%s")' % csv_filename)

    fields = ["uuid", "description"]
    with open(csv_filename, 'w', newline='', encoding="utf-8") as csvfile:
        # creating a csv writer object
        writer = csv.writer(csvfile)

        # writing the fields
        writer.writerow(fields)

        # writing the data rows
        for item in todos:
            row = [item.uuid, item.description]
            writer.writerow(row)


def snap_todos_1(client):
    todos = client.get_todos()
    todos.sort(key=todo.sort_key, reverse=True)
    for item in todos:
        print('%s, "%s"' % (item.uuid, item.description))

    csv_filename = utils.gen_todos_snap_filename()
    csv_path = "csv" + os.sep + csv_filename
    print("csv path: %s" % csv_path)

    snap_todos(todos, csv_filename)
    pass
