import datetime
import os
import unittest

import api
import enum_code


class TestAPI(unittest.TestCase):
    def setUp(self):
        apiPassword = os.environ["KABU_STATION_API_PASSWORD"]
        self._client = api.LiveClient(apiPassword)

    def test_symbolname_future_get(self):
        (symbol, symbolname) = self._client.symbolname_future_get(
            enum_code.FutureCode.NK225mini
        )
        self.assertIsNotNone(symbol)
        self.assertIsNotNone(symbolname)

        today = datetime.date.today()
        next_month = today + datetime.timedelta(days=30)
        (symbol, symbolname) = self._client.symbolname_future_get(
            enum_code.FutureCode.NK225mini, next_month
        )
        self.assertIsNotNone(symbol)
        self.assertIsNotNone(symbolname)

    def test_symbolname_option_get(self):
        (symbol, symbolname) = self._client.symbolname_option_get(
            enum_code.OptionCode.NK225op, enum_code.PutOrCall.Put, 38000
        )
        self.assertIsNotNone(symbol)
        self.assertIsNotNone(symbolname)

        today = datetime.date.today()
        next_month = today + datetime.timedelta(days=30)
        (symbol, symbolname) = self._client.symbolname_option_get(
            enum_code.OptionCode.NK225op, enum_code.PutOrCall.Put, 38000, next_month
        )
        self.assertIsNotNone(symbol)
        self.assertIsNotNone(symbolname)
