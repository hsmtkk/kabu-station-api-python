import datetime

import requests

import enum_code
import handler


class Request:
    def __init__(
        self,
        option_code: enum_code.OptionCode,
        put_or_call: enum_code.PutOrCall,
        strike_price: int,
        deriv_month: datetime.date = None,
    ):
        self._option_code = option_code
        self._put_or_call = put_or_call
        self._strike_price = strike_price
        if deriv_month is None:
            self._deriv_month = 0
        else:
            self._deriv_month = deriv_month.strftime("%Y%m")

    @property
    def option_code(self) -> enum_code.OptionCode:
        return self._option_code

    @property
    def put_or_call(self) -> enum_code.PutOrCall:
        return self._put_or_call

    @property
    def strike_price(self) -> int:
        return self._strike_price

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
        super().__init__(port, "/symbolname/option")
        self._token = token

    def handle(self, req: Request) -> Response:
        url = self.make_url()
        params = {
            "OptionCode": req.option_code,
            "DerivMonth": req.deriv_month,
            "PutOrCall": req.put_or_call,
            "StrikePrice": req.strike_price,
        }
        resp = requests.get(url, params=params, headers={"X-API-KEY": self._token})
        decoded = self.decode_response(resp)
        return Response(decoded["Symbol"], decoded["SymbolName"])
