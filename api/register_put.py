import pydantic
import requests

import enum_code
import handler


class SymbolExchange(pydantic.BaseModel):
    symbol: str
    exchange: enum_code.MarketCode


class Request(pydantic.BaseModel):
    symbols: list[SymbolExchange]


class Response(pydantic.BaseModel):
    regist_list: list[SymbolExchange]


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
                SymbolExchange(
                    symbol=d["Symbol"], exchange=enum_code.MarketCode(d["Exchange"])
                )
            )
        return Response(regist_list=regist_list)
