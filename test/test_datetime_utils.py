from datetime import timedelta, datetime
from unittest import TestCase

from pomotodo import datetime_utils


class Test(TestCase):
    def test_local_today(self):
        print(datetime_utils.local_today())
        print(datetime_utils.utc_today())

        started_earlier_than = datetime_utils.utc_today()
        print(started_earlier_than)

        started_later_than = started_earlier_than - timedelta(days=1)
        print(started_later_than)
        # self.fail()
        pass

    def test_local_now(self):
        now = datetime_utils.to_local(datetime.now())
        print(now.isoformat())
        print(datetime_utils.to_iso8601(now))

    def test_local_now_2(self):
        now_str = datetime.now().isoformat()
        print(now_str)
