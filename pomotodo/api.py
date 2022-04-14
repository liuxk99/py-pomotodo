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
import tzlocal

API_URL = 'https://api.pomotodo.com/1/'


def compose_pomo(description, started_at, ended_at, timezone, description1):
    data_args = {'description': description, 'started_at': started_at, 'ended_at': ended_at}
    if timezone is None:
        data_args['timezone'] = tzlocal.get_localzone()
    return data_args


def post_pomo(token, started_at, ended_at, timezone, description):
    headers = {'Authorization': 'token ' + token}

    data_args = compose_pomo(description, started_at, ended_at, timezone, description)
    response = requests.post(API_URL + "pomos", headers=headers, data=data_args)
    print("statue code: %d" % response.status_code)

    if 200 <= response.status_code < 300:
        json_obj = response.json()
        return json_obj
    else:
        print(response.content)
        return None

def get_pomos(token, started_later_than_dt, started_earlier_than=None, manual=False):
    headers = {'Authorization': 'token ' + token}
    query_params = {'started_later_than': started_later_than_dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 'limit': "100"}
    if started_earlier_than:
        query_params['started_earlier_than'] = started_earlier_than.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    if manual:
        query_params['manual'] = "true"

    print(query_params)
    response = requests.get(API_URL + "pomos/", headers=headers, params=query_params)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        print("status code: %d" % response.status_code)
    return None


def get_pomo(token, uuid):
    headers = {'Authorization': 'token ' + token}
    result = requests.get(API_URL + "pomos/%s" % uuid, headers=headers)
    return result.json()


def get_todos(token):
    headers = {'Authorization': 'token ' + token}
    parameters = {'limit': "100"}
    result = requests.get(API_URL + "todos/", headers=headers, params=parameters)
    return result.json()


def get_todo(token, uuid):
    """
    Refer:
    https://pomotodo.github.io/api-doc/#api-Todo-ListTodos
    """

    headers = {'Authorization': 'token ' + token}
    result = requests.get(API_URL + "todos/%s" % uuid, headers=headers)
    print("statue code: %d" % result.status_code)
    if 200 <= result.status_code < 300:
        return result.json()
    return None


def pin_todo(token, uuid):
    """
    Refer:
    https://pomotodo.github.io/api-doc/#api-Todo-ListTodos
    """

    headers = {'Authorization': 'token ' + token}
    data_args = {"pin": "true"}
    result = requests.patch(API_URL + "todos/%s" % uuid, headers=headers, data=data_args)
    print("statue code: %d" % result.status_code)
    return result.json()


def unpin_todo(token, uuid):
    """
    Refer:
    https://pomotodo.github.io/api-doc/#api-Todo-ListTodos
    """

    headers = {'Authorization': 'token ' + token}
    data_args = {"pin": "false"}
    result = requests.patch(API_URL + "todos/%s" % uuid, headers=headers, data=data_args)
    print("statue code: %d" % result.status_code)
    return result.json()


def delete_todo(token, uuid):
    """
    Refer:
    https://pomotodo.github.io/api-doc/#api-Todo-ListTodos
    """

    headers = {'Authorization': 'token ' + token}
    result = requests.delete(API_URL + "todos/%s" % uuid, headers=headers)
    print("statue code: %d" % result.status_code)
    return result.status_code


def post_todo(token, description,
              notice=None, pin=None,
              completed=None, completed_at=None,
              repeat_type=None, remind_time=None, estimated_pomo_count=-1, costed_pomo_count=-1):
    """
    Refer:
    https://pomotodo.github.io/api-doc/#api-Todo-ListTodos
    """

    headers = {}
    headers['Authorization'] = 'token %s' % token
    # # set content type and accept headers to handle JSON
    # headers['Content-Type'] = 'application/json; charset=utf-8'
    headers['Accept'] = 'application/json'

    data_args = compose_todo(description, notice, pin, completed, completed_at, repeat_type, remind_time,
                             estimated_pomo_count, costed_pomo_count)
    response = requests.post(API_URL + "todos", headers=headers, data=data_args)
    print("statue code: %d" % response.status_code)

    if 200 <= response.status_code < 300:
        json_obj = response.json()
        return json_obj
    else:
        print(response.content)
        return None


def patch_todo(token, uuid, description,
               notice=None, pin=None,
               completed=None, completed_at=None,
               repeat_type=None, remind_time=None, estimated_pomo_count=-1, costed_pomo_count=-1):
    """
    Refer:
    https://pomotodo.github.io/api-doc/#api-Todo-ListTodos
    """

    headers = {'Authorization': 'token %s' % token}
    data_args = compose_todo(description, notice, pin, completed, completed_at, repeat_type, remind_time,
                             estimated_pomo_count, costed_pomo_count)
    result = requests.patch(API_URL + "todos/%s" % uuid, headers=headers, data=data_args)
    print("statue code: %d" % result.status_code)
    return result.json()


def compose_todo(description, notice, pin, completed, completed_at, repeat_type, remind_time, estimated_pomo_count,
                 costed_pomo_count):
    param_dict = {}
    if description:
        param_dict['description'] = description
    if notice:
        param_dict['notice'] = notice
    if pin:
        param_dict['pin'] = "%r" % pin
    if completed:
        param_dict['completed'] = "%r" % completed
    if completed_at:
        param_dict['completed_at'] = completed_at.isoformat()
    if repeat_type:
        param_dict['repeat_type'] = repeat_type
    if remind_time:
        param_dict['remind_time'] = remind_time.isoformat()
    if estimated_pomo_count > 0:
        param_dict['estimated_pomo_count'] = estimated_pomo_count
    if costed_pomo_count > 0:
        param_dict['costed_pomo_count'] = costed_pomo_count
    return param_dict
