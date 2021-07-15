# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        sjPomotodo
# Purpose:      python client for pomotodo
#
# Author:      thomas
#
# Created:     31/03/2020
# Copyright:   (c) thomas 2020
# Licence:     <your licence>
# coding=utf-8
# -------------------------------------------------------------------------------

import requests

API_URL = 'https://api.pomotodo.com/1/'


def get_pomos(token, started_later_than_dt, started_earlier_than=None, manual=False):
    headers = {'Authorization': 'token ' + token}
    parameters = {'started_later_than': started_later_than_dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 'limit': "100"}
    if started_earlier_than:
        parameters['started_earlier_than'] = started_earlier_than.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    if manual:
        parameters['manual'] = "true"

    print(parameters)
    result = requests.get(API_URL + "pomos/", headers=headers, params=parameters)
    if 200 <= result.status_code < 300:
        return result.json()
    else:
        print("status code: %d" % result.status_code)
    return None


def get_todos(token):
    headers = {'Authorization': 'token ' + token}
    result = requests.get(API_URL + "todos/", headers=headers)
    return result.json()


def get_pomo(token, uuid):
    headers = {'Authorization': 'token ' + token}
    result = requests.get(API_URL + "pomos/%s" % uuid, headers=headers)
    return result.json()
