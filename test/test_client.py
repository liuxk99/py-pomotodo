from datetime import timedelta
from unittest import TestCase

from pomotodo import datetime_utils, utils
from pomotodo.client import PomotodoClient


class TestTrelloClient(TestCase):
    def test_get_pomos(self):
        p = utils.load("pomotodo.properties")
        print("token: %s" % p.properties['token'])
        client = PomotodoClient(
            token=p.properties['token']
        )

        started_later_than = datetime_utils.utc_today()
        print(started_later_than)
        pomos = client.get_pomos(started_later_than, None)
        pomos.append(client.get_pomos(started_later_than, None, True))
        print("There are %d pomos." % len(pomos))
        for pomo in pomos:
            print(pomo)

        # self.fail()

        pass
