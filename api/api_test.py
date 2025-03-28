import datetime
import os
import unittest

import api
import enum_code
import symbolname_future_get
import symbolname_option_get


class TestAPI(unittest.TestCase):
    def setUp(self):
        apiPassword = os.environ["KABU_STATION_API_PASSWORD"]
        self._client = api.LiveClient(apiPassword)

    def test_symbolname_future_get(self):
        resp = self._client.symbolname_future_get(
            symbolname_future_get.Request(enum_code.FutureCode.NK225mini)
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)

        today = datetime.date.today()
        next_month = today + datetime.timedelta(days=30)
        resp = self._client.symbolname_future_get(
            symbolname_future_get.Request(enum_code.FutureCode.NK225mini, next_month)
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)

    def test_symbolname_option_get(self):
        resp = self._client.symbolname_option_get(
            symbolname_option_get.Request(
                enum_code.OptionCode.NK225op, enum_code.PutOrCall.Put, 35000
            )
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)

        today = datetime.date.today()
        next_month = today + datetime.timedelta(days=30)
        resp = self._client.symbolname_option_get(
            symbolname_option_get.Request(
                enum_code.OptionCode.NK225op, enum_code.PutOrCall.Put, 35000, next_month
            )
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)
