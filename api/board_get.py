import json

import requests

import enum_code
import handler


class Request:
    def __init__(
        self,
        symbol: str,
        market_code: enum_code.MarketCode,
    ):
        self._symbol = f"{symbol}@{market_code}"

    @property
    def symbol(self) -> str:
        return self._symbol


class Response:
    def __init__(
        self,
        symbol: str,
        symbolname: str,
        current_price: int,
        iv: float | None = None,
        delta: float | None = None,
        gamma: float | None = None,
        vega: float | None = None,
        theta: float | None = None,
    ):
        self._symbol = symbol
        self._symbolname = symbolname
        self._current_price = current_price
        self._iv = iv
        self._delta = delta
        self._gamma = gamma
        self._vega = vega
        self._theta = theta

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def symbolname(self) -> str:
        return self._symbolname

    @property
    def current_price(self) -> int:
        return self._current_price

    @property
    def iv(self) -> float:
        return self._iv

    @property
    def delta(self) -> float:
        return self._delta

    @property
    def gamma(self) -> float:
        return self._gamma

    @property
    def vega(self) -> float:
        return self._vega

    @property
    def theta(self) -> float:
        return self._theta

    def __str__(self) -> str:
        d = {
            "symbol": self.symbol,
            "symbolname": self.symbolname,
            "current_price": self.current_price,
            "iv": self.iv,
            "delta": self.delta,
            "gamma": self.gamma,
            "vega": self.vega,
            "theta": self.theta,
        }
        return json.dumps(d)


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
            decoded["Symbol"],
            decoded["SymbolName"],
            decoded["CurrentPrice"],
            decoded.get("IV", None),
            decoded.get("Delta", None),
            decoded.get("Gamma", None),
            decoded.get("Vega", None),
            decoded.get("Theta", None),
        )
        return resp
