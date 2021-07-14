from datetime import timedelta
from unittest import TestCase

from pomotodo import datetime_utils, utils, pomo
from pomotodo.client import PomotodoClient


def dump_pomos(pomos):
    print("There are %d pomos." % len(pomos))
    i = 0
    for pomo in pomos:
        i=i+1
        print("No.%02d" % i)
        print(pomo.to_text())
        print("---")


class TestTrelloClient(TestCase):
    def setUp(self):
        p = utils.load("pomotodo.properties")
        print("token: %s" % p.properties['token'])
        self.client = PomotodoClient(
            token=p.properties['token']
        )
        pass

    def test_get_pomos_yesterday(self):
        started_earlier_than = datetime_utils.utc_today()
        started_later_than = started_earlier_than - timedelta(days=1)
        pomos = self.client.get_pomos(started_later_than, started_earlier_than)
        # dump_pomos(pomos)
        pomos_manual = self.client.get_pomos(started_later_than, started_earlier_than, True)
        # dump_pomos(pomos_manual)

        for e in pomos_manual:
            pomos.append(e)

        pomos.sort(key=pomo.sort_key)
        print(datetime_utils.to_local(started_later_than).strftime("%Y/%m/%d"))
        dump_pomos(pomos)
        pass
