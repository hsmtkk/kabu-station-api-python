import datetime

import pydantic
import requests

import enum_code
import handler


class Request(pydantic.BaseModel):
    option_code: enum_code.OptionCode
    put_or_call: enum_code.PutOrCall
    strike_price: pydantic.NonNegativeInt
    deriv_month: pydantic.NonNegativeInt

    def __init__(
        self,
        option_code: enum_code.OptionCode,
        put_or_call: enum_code.PutOrCall,
        strike_price: int,
        deriv_month: datetime.date = None,
    ):
        if deriv_month is None:
            year_month = 0
        else:
            year_month = int(deriv_month.strftime("%Y%m"))
        super().__init__(
            option_code=option_code,
            put_or_call=put_or_call,
            strike_price=strike_price,
            deriv_month=year_month,
        )


class Response(pydantic.BaseModel):
    symbol: str
    symbolname: str


class Handler(handler.Handler):
    def __init__(self, port: int, token: str):
        super().__init__(port)
        self._token = token

    def handle(self, req: Request) -> Response:
        url = self.make_url("/symbolname/option")
        params = {
            "OptionCode": req.option_code,
            "DerivMonth": req.deriv_month,
            "PutOrCall": req.put_or_call,
            "StrikePrice": req.strike_price,
        }
        resp = requests.get(url, params=params, headers={"X-API-KEY": self._token})
        decoded = self.decode_response(resp)
        return Response(symbol=decoded["Symbol"], symbolname=decoded["SymbolName"])
