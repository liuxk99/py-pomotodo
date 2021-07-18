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
from pomotodo import datetime_utils


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