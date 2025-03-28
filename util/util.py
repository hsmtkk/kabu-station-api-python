import datetime

import api.client
import api.board_get
import api.enum_code
import api.symbolname_future_get


class Utility:
    def __init__(self, client: api.client.Client):
        self._client = client

    def at_the_money(self) -> int:
        req = api.symbolname_future_get.Request(api.enum_code.FutureCode.NK225mini)
        resp = self._client.symbolname_future_get(req)
        req = api.board_get.Request(resp.symbol, api.enum_code.MarketCode.WholeDay)
        resp = self._client.board_get(req)
        price = resp.current_price
        return (price // 250) * 250

    def first_month(self) -> datetime.date:
        req = api.symbolname_future_get.Request(api.enum_code.FutureCode.NK225mini)
        resp = self._client.symbolname_future_get(req)
        return self._get_month_from_symbolname(resp.symbolname)

    def _get_month_from_symbolname(self, symbolname: str) -> datetime.date:
        elems = symbolname.split(" ")
        if len(elems) != 2:
            raise Exception(f"failed to parse symbolname {symbolname}")
        return datetime.datetime.strptime("%y/%m")
