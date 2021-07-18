# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from pomotodo.pomo import Pomo
from pomotodo import api
from pomotodo.todo import Todo

try:
    # PyOpenSSL works around some issues in python ssl modules
    # In particular in python < 2.7.9 and python < 3.2
    # It is not a hard requirement, so it's not listed in requirements.txt
    # More info https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning
    import urllib3.contrib.pyopenssl

    urllib3.contrib.pyopenssl.inject_into_urllib3()
except:
    pass


class PomotodoClient(object):
    """ Base class for Pomotodo API access """

    def __init__(self, token):
        """
        Constructor

        :token: API key generated at https://pomotodo.com/developer
        """

        self.token = token

    def get_pomos(self, started_later_than_dt, started_earlier_than=None, manual=False):
        json_items = api.get_pomos(self.token, started_later_than_dt, started_earlier_than, manual)
        pomos = []
        if json_items:
            for e in json_items:
                pomos.append(Pomo.from_json(e))

        return pomos

    def get_pomo(self, uuid):
        pomo_json = api.get_pomo(self.token, uuid)
        pomo = Pomo.from_json(pomo_json)
        print(pomo.to_text())
        pass

    def get_todos(self):
        todos = []
        json_items = api.get_todos(self.token)
        for item in json_items:
            todos.append(Todo.from_json(item))
        return todos

    def get_todo(self, uuid):
        todo = None
        json = api.get_todo(self.token, uuid)
        if json:
            todo = Todo.from_json(json)
        return todo

    def pin_todo(self, uuid):
        json = api.pin_todo(self.token, uuid)
        return Todo.from_json(json)

    def unpin_todo(self, uuid):
        json = api.unpin_todo(self.token, uuid)
        return Todo.from_json(json)

    def delete_todo(self, uuid):
        status_code = api.delete_todo(self.token, uuid)
        return 200 <= status_code < 300

    def patch_todo(self, uuid,
                   description,
                   notice=None, pin=None,
                   completed=None, completed_at=None,
                   repeat_type=None, remind_time=None, estimated_pomo_count=-1, costed_pomo_count=-1):
        json = api.patch_todo(self.token, uuid, description,
                              notice, pin,
                              completed, completed_at,
                              repeat_type, remind_time,
                              estimated_pomo_count, costed_pomo_count)
        return Todo.from_json(json)
        pass

    def post_todo(self,
                   description,
                   notice=None, pin=None,
                   completed=None, completed_at=None,
                   repeat_type=None, remind_time=None, estimated_pomo_count=-1, costed_pomo_count=-1):
        json = api.post_todo(self.token, description,
                              notice, pin,
                              completed, completed_at,
                              repeat_type, remind_time,
                              estimated_pomo_count, costed_pomo_count)
        return Todo.from_json(json)
