import datetime

import pydantic
import requests

import enum_code
import handler


class Request(pydantic.BaseModel):
    future_code: enum_code.FutureCode
    deriv_month: pydantic.NonNegativeInt

    def __init__(
        self, future_code: enum_code.FutureCode, deriv_month: datetime.date = None
    ):
        if deriv_month is None:
            year_month = 0
        else:
            year_month = int(deriv_month.strftime("%Y%m"))
        super().__init__(future_code=future_code, deriv_month=year_month)


class Response(pydantic.BaseModel):
    symbol: str
    symbolname: str


class Handler(handler.Handler):
    def __init__(self, port: int, token: str):
        super().__init__(port)
        self._token = token

    def handle(self, req: Request) -> Response:
        url = self.make_url("/symbolname/future")
        params = {"FutureCode": req.future_code, "DerivMonth": req.deriv_month}
        resp = requests.get(url, params=params, headers={"X-API-KEY": self._token})
        decoded = self.decode_response(resp)
        return Response(symbol=decoded["Symbol"], symbolname=decoded["SymbolName"])
