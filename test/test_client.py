from datetime import timedelta
from unittest import TestCase

from pomotodo import datetime_utils, utils, pomo
from pomotodo.client import PomotodoClient


def dump_pomos(pomos):
    print("There are %d pomos." % len(pomos))
    i = 0
    seconds = 0
    for item in pomos:
        i = i + 1
        seconds += item._length
        print("=> No.%02d" % i)
        print(item.to_markdown())
    # "总计 4 小时 47 分钟"
    print("完成了 %d 个番茄, 总计 %d seconds" % (i, seconds))


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

    def test_get_pomo(self):
        uuid = "fa8e9021-87b5-4751-8c53-5aa047563ecd"
        self.client.get_pomo(uuid)
        pass
