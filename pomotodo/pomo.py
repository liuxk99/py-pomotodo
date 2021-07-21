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
# json data structure
# {
#     "uuid": "26a37b6f-6e69-4a2e-ae79-e9c264a4a653",
#     "created_at": "2020-03-30T12:25:26.800Z",
#     "updated_at": "2020-03-30T12:25:26.800Z",
#     "description": "xxx",
#     "started_at": "2020-03-30T11:59:20.254Z",
#     "ended_at": "2020-03-30T12:25:26.799Z",
#     "local_started_at": "2020-03-30T19:59:20.000Z",
#     "local_ended_at": "2020-03-30T20:25:26.000Z",
#     "length": 25,
#     "abandoned": false,
#     "manual": false
# },

from pomotodo import datetime_utils


def sort_key(pomo):
    return pomo._started_at


class Pomo:
    def __init__(self, uuid, created_at, updated_at, description, started_at, ended_at,
                 local_started_at, local_ended_at, length, abandoned=False, manual=False):
        self._uuid = uuid
        self._created_at = created_at
        self._updated_at = updated_at
        self._description = description
        self._started_at = started_at
        self._ended_at = ended_at
        self._local_started_at = local_started_at
        self._local_ended_at = local_ended_at
        self._length = length
        self._abandoned = abandoned
        self._manual = manual

    def __str__(self):
        uuid = str(self._uuid)
        created_at = self._created_at.isoformat()
        updated_at = self._updated_at.isoformat()
        description = self._description
        started_at = self._started_at.isoformat()
        ended_at = self._ended_at.isoformat()
        local_started_at = self._local_started_at.isoformat()
        local_ended_at = self._local_ended_at.isoformat()
        length = str(self._length)
        abandoned = str(self._abandoned)
        manual = str(self._manual)

        return (u'uuid: %s\n started_at: %s, ended_at: %s\n'
                u' local_started_at: %s, local_ended_at: %s\n'
                u' description: %s\n'
                u' create_at: %s, update_at: %s\n'
                u' length: %s, abandoned: %s, manual: %s\n'
                % (uuid, started_at, ended_at,
                   local_started_at, local_ended_at,
                   description,
                   created_at, updated_at,
                   self.duration(), abandoned, manual))

    def to_text(self):
        uuid = str(self._uuid)
        description = self._description
        local_started_at = self._local_started_at
        local_ended_at = self._local_ended_at
        length = str(self._length)
        abandoned = str(self._abandoned)
        manual = str(self._manual)

        return (u'uuid: %s\n'
                u' [%s - %s]\n'
                u' "%s"\n'
                u' length: %s, abandoned: %s, manual: %s'
                % (uuid,
                   local_started_at.strftime("%H:%M"), local_ended_at.strftime("%H:%M"),
                   description,
                   self.duration(), abandoned, manual))

    def to_markdown(self):
        cur_date = self._local_started_at.strftime("%Y/%m/%d")
        begin_time = self._local_started_at.strftime("%H:%M")
        end_time = self._local_ended_at.strftime("%H:%M")

        return u'%s [%s - %s]\n**\\%s**\n\n---' % (cur_date, begin_time, end_time, self._description)

    @staticmethod
    def from_json(e):
        uuid = e[u'uuid']
        created_at = e[u'created_at']
        updated_at = e[u'updated_at']
        description = e[u'description']
        started_at = e[u'started_at']
        ended_at = e[u'ended_at']
        local_started_at = e[u'local_started_at']
        local_ended_at = e[u'local_ended_at']
        length = e[u'length']
        abandoned = e[u'abandoned']
        manual = e[u'manual']

        return Pomo(uuid, datetime_utils.from_iso8601(created_at), datetime_utils.from_iso8601(updated_at), description,
                    datetime_utils.from_iso8601(started_at), datetime_utils.from_iso8601(ended_at),
                    datetime_utils.from_iso8601(local_started_at), datetime_utils.from_iso8601(local_ended_at),
                    length, abandoned, manual)

    def duration(self):
        delta = self._ended_at - self._started_at
        return delta.total_seconds()
