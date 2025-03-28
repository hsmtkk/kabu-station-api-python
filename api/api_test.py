import datetime
import os
import unittest

import api
import future_code


class TestAPI(unittest.TestCase):
    def setUp(self):
        apiPassword = os.environ["KABU_STATION_API_PASSWORD"]
        self._client = api.LiveClient(apiPassword)

    def test_symbolname_future_get(self):
        (symbol, symbolname) = self._client.symbolname_future_get(
            future_code.FutureCode.NK225mini
        )
        self.assertIsNotNone(symbol)
        self.assertIsNotNone(symbolname)

        today = datetime.date.today()
        next_month = today + datetime.timedelta(days=30)
        (symbol, symbolname) = self._client.symbolname_future_get(
            future_code.FutureCode.NK225mini, next_month
        )
        self.assertIsNotNone(symbol)
        self.assertIsNotNone(symbolname)
