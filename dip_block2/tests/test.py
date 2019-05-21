import json
import unittest
from dip_block2.app import search
import mock

class TestApp(unittest.TestCase):

    def test_search(self):
        self.user =
        with mock.patch('app.user', self.user):
            self.assertTrue(search(user))


if __name__ == '__main__':
    unittest.main()
