from unittest import TestCase

from pomotodo import datetime_utils


class Test(TestCase):
    def test_local_today(self):
        print(datetime_utils.local_today())
        # self.fail()
        pass
