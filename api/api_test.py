import os
import unittest

import api


class TestAPI(unittest.TestCase):
    def setUp(self):
        apiPassword = os.environ["KABU_STATION_API_PASSWORD"]
        self._client = api.LiveClient(apiPassword)

    def test0(self):
        pass
