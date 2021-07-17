# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        pomo
# Purpose:      python client for pomotodo
#
# Author:      thomas
#
# Created:     07/07/2021
# Copyright:   (c) thomas 2021
# Licence:     <your licence>
# coding=utf-8
# -------------------------------------------------------------------------------
"""
Refer:
https://pomotodo.github.io/api-doc/#api-Todo-GetTodo
[
  {
    "uuid": "ac753187-2f22-4b5c-b716-f1fcecfb4410",
    "created_at": "2016-08-06T06:48:52.000Z",
    "updated_at": "2016-08-06T06:51:12.000Z",
    "description": "Catch some little Monsters",
    "notice": null,
    "pin": false,
    "completed": false,
    "completed_at": null,
    "repeat_type": "none",
    "remind_time": null,
    "estimated_pomo_count": null,
    "costed_pomo_count": 0,
    "sub_todos": [
      "81921b2e-8b54-46cf-bb47-0d3c3c7e8302",
      "ff59811e-4c53-404f-a842-9590b632616f"
    ]
  }
]
"""
from uuid import UUID
from datetime import datetime
from typing import List

from pomotodo import datetime_utils


class Todo:
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    description: str
    notice: str
    pin: bool
    completed: bool
    completed_at: datetime
    repeat_type: str
    remind_time: datetime
    estimated_pomo_count: int
    costed_pomo_count: int
    sub_todos: List[UUID]

    def __init__(self, uuid: UUID,
                 created_at: datetime, updated_at: datetime,
                 description: str,
                 notice: str, pin: bool,
                 completed: bool, completed_at: datetime,
                 repeat_type: str, remind_time: datetime,
                 estimated_pomo_count: int, costed_pomo_count: int,
                 sub_todos: List[UUID]) -> None:
        self.uuid = uuid
        self.created_at = created_at
        self.updated_at = updated_at
        self.description = description
        self.notice = notice
        self.pin = pin
        self.completed = completed
        self.completed_at = completed_at
        self.repeat_type = repeat_type
        self.remind_time = remind_time
        self.estimated_pomo_count = estimated_pomo_count
        self.costed_pomo_count = costed_pomo_count
        self.sub_todos = sub_todos

    def __str__(self):
        return (u'uuid: %s\n'
                u' created_at: %s, updated_at: %s\n'
                u' description: %s\n'
                u' notice: %s, pin: %r\n'
                u' completed: %s, completed_at: %s\n'
                u' repeat_type = %s, remind_time = %s\n'
                u' sub_todos: %s\n'
                % (str(self.uuid),
                   self.created_at.isoformat(), self.updated_at.isoformat(),
                   self.description,
                   self.notice, self.pin,
                   self.completed, self.completed_at,
                   self.repeat_type, self.remind_time, self.sub_todos))

    @staticmethod
    def from_json(e):
        uuid = e['uuid']
        created_at = datetime_utils.from_iso8601(e['created_at'])
        updated_at = datetime_utils.from_iso8601(e['updated_at'])
        description = e['description']
        notice = e['notice']
        pin = e['pin']

        completed = e['completed']
        completed_at = None
        completed_at_str = e['completed_at']
        if completed_at_str:
            completed_at = datetime_utils.from_iso8601(completed_at_str)

        repeat_type = e['repeat_type']
        remind_time = None
        remind_time_str = e['remind_time']
        if remind_time_str:
            remind_time = datetime_utils.from_iso8601(remind_time_str)

        estimated_pomo_count = e['estimated_pomo_count']
        costed_pomo_count = e['costed_pomo_count']
        sub_todos = e['sub_todos']

        return Todo(uuid,
                    created_at, updated_at,
                    description,
                    notice, pin,
                    completed, completed_at,
                    repeat_type, remind_time,
                    estimated_pomo_count, costed_pomo_count,
                    sub_todos)
        pass
