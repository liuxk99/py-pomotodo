from unittest import TestCase

from pomotodo import utils


class Test(TestCase):
    def test_load(self):

        p = utils.load("pomotodo.properties")
        if p.properties:
            print(p.properties['token'])
        # self.fail()
