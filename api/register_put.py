import requests

import enum_code
import handler
import json


class SymbolExchange:
    def __init__(self, symbol: str, exchange: enum_code.MarketCode):
        self._symbol = symbol
        self._exchange = exchange

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def exchange(self) -> enum_code.MarketCode:
        return self._exchange

    def __str__(self) -> str:
        d = {"symbol": self._symbol, "exchange": self._exchange}
        return json.dumps(d)


class Request:
    def __init__(self, symbols: list[SymbolExchange]):
        self._symbols = symbols

    @property
    def symbols(self) -> list[SymbolExchange]:
        return self._symbols


class Response:
    def __init__(
        self,
        regist_list: list[SymbolExchange],
    ):
        self._regist_list = regist_list

    @property
    def regist_list(self) -> list[SymbolExchange]:
        return self._regist_list

    def __str__(self) -> str:
        return str(self._regist_list)


class Handler(handler.Handler):
    def __init__(self, port: int, token: str):
        super().__init__(port)
        self._token = token

    def handle(self, req: Request) -> Response:
        url = self.make_url("/register")
        symbols = []
        for sym_ex in req.symbols:
            symbols.append({"Symbol": sym_ex.symbol, "Exchange": sym_ex.exchange})
        params = {"Symbols": symbols}
        resp = requests.put(url, json=params, headers={"X-API-KEY": self._token})
        decoded = self.decode_response(resp)
        regist_list = []
        for d in decoded["RegistList"]:
            regist_list.append(
                SymbolExchange(d["Symbol"], enum_code.MarketCode(d["Exchange"]))
            )
        return Response(regist_list)
