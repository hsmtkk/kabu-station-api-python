import datetime

import requests

import enum_code
import handler


class Request:
    def __init__(
        self, future_code: enum_code.FutureCode, deriv_month: datetime.date = None
    ):
        self._future_code = future_code
        if deriv_month is None:
            self._deriv_month = 0
        else:
            self._deriv_month = deriv_month.strftime("%Y%m")

    @property
    def future_code(self) -> enum_code.FutureCode:
        return self._future_code

    @property
    def deriv_month(self) -> str:
        return self._deriv_month


class Response:
    def __init__(self, symbol: str, symbolname: str):
        self._symbol = symbol
        self._symbolname = symbolname

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def symbolname(self) -> str:
        return self._symbolname


class Handler(handler.Handler):
    def __init__(self, port: int, token: str):
        super().__init__(port)
        self._token = token

    def handle(self, req: Request) -> Response:
        url = self.make_url("/symbolname/future")
        params = {"FutureCode": req.future_code, "DerivMonth": req.deriv_month}
        resp = requests.get(url, params=params, headers={"X-API-KEY": self._token})
        decoded = self.decode_response(resp)
        return Response(decoded["Symbol"], decoded["SymbolName"])
