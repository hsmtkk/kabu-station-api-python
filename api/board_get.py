import json

import pydantic
import requests

import enum_code
import handler


class Request(pydantic.BaseModel):
    symbol: str

    def __init__(
        self,
        symbol: str,
        market_code: enum_code.MarketCode,
    ):
        super().__init__(symbol=f"{symbol}@{market_code}")


class Response(pydantic.BaseModel):
    symbol: str
    symbolname: str
    current_price: pydantic.NonNegativeInt
    iv: pydantic.NonNegativeFloat | None
    delta: float | None
    gamma: pydantic.NonNegativeFloat | None
    vega: pydantic.NonNegativeFloat | None
    theta: pydantic.NegativeFloat | None


class Handler(handler.Handler):
    def __init__(self, port: int, token: str):
        self._base_path = "/board"
        super().__init__(port)
        self._token = token

    def handle(self, req: Request) -> Response:
        path = f"{self._base_path}/{req.symbol}"
        url = self.make_url(path)
        resp = requests.get(url, headers={"X-API-KEY": self._token})
        decoded = self.decode_response(resp)
        resp = Response(
            symbol=decoded["Symbol"],
            symbolname=decoded["SymbolName"],
            current_price=decoded["CurrentPrice"],
            iv=decoded.get("IV", None),
            delta=decoded.get("Delta", None),
            gamma=decoded.get("Gamma", None),
            vega=decoded.get("Vega", None),
            theta=decoded.get("Theta", None),
        )
        return resp
