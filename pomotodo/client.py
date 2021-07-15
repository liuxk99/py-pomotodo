# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from pomotodo.pomo import Pomo
from pomotodo import api

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
