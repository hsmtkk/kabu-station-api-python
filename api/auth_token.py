import pydantic
import requests

import handler


class Request(pydantic.BaseModel):
    api_password: str


class Response(pydantic.BaseModel):
    result_code: pydantic.NonNegativeInt
    token: str


class Handler(handler.Handler):
    def __init__(self, port: int):
        super().__init__(port)

    def handle(self, req: Request) -> Response:
        url = self.make_url("/token")
        params = {"APIPassword": req.api_password}
        resp = requests.post(url, json=params)
        decoded = self.decode_response(resp)
        return Response(result_code=decoded["ResultCode"], token=decoded["Token"])
