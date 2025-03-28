import datetime
import os
import unittest

import client
import board_get
import enum_code
import register_put
import symbolname_future_get
import symbolname_option_get


class TestAPI(unittest.TestCase):
    def setUp(self):
        apiPassword = os.environ["KABU_STATION_API_PASSWORD"]
        self._client = client.LiveClient(apiPassword)

    def test_symbolname_future_get(self):
        resp = self._client.symbolname_future_get(
            symbolname_future_get.Request(future_code=enum_code.FutureCode.NK225mini)
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)

        today = datetime.date.today()
        next_month = today + datetime.timedelta(days=30)
        resp = self._client.symbolname_future_get(
            symbolname_future_get.Request(
                future_code=enum_code.FutureCode.NK225mini, deriv_month=next_month
            )
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)

    def test_symbolname_option_get(self):
        resp = self._client.symbolname_option_get(
            symbolname_option_get.Request(
                option_code=enum_code.OptionCode.NK225op,
                put_or_call=enum_code.PutOrCall.Put,
                strike_price=35000,
            )
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)

        today = datetime.date.today()
        next_month = today + datetime.timedelta(days=30)
        resp = self._client.symbolname_option_get(
            symbolname_option_get.Request(
                option_code=enum_code.OptionCode.NK225op,
                put_or_call=enum_code.PutOrCall.Put,
                strike_price=35000,
                deriv_month=next_month,
            )
        )
        self.assertIsNotNone(resp.symbol)
        self.assertIsNotNone(resp.symbolname)

    def test_board_get(self):
        resp = self._client.board_get(
            board_get.Request(
                symbol="130046718", market_code=enum_code.MarketCode.WholeDay
            )
        )
        self.assertIsNotNone(resp)

    def test_register(self):
        self._client.unregister_all_put()
        symbols = [
            register_put.SymbolExchange(
                symbol="130046718", exchange=enum_code.MarketCode.WholeDay
            )
        ]
        resp = self._client.register_put(register_put.Request(symbols=symbols))
        self.assertIsNotNone(resp)
        print(resp)
