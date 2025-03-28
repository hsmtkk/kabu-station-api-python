import requests

import handler


class Request:
    def __init__(self, api_password: str):
        self._api_password = api_password

    @property
    def api_password(self) -> str:
        return self._api_password


class Response:
    def __init__(self, result_code: str, token: str):
        self._result_code = result_code
        self._token = token

    @property
    def result_code(self) -> str:
        return self._result_code

    @property
    def token(self) -> str:
        return self._token


class Handler(handler.Handler):
    def __init__(self, port: int):
        super().__init__(port, "/token")

    def handle(self, req: Request) -> Response:
        url = self.make_url()
        params = {"APIPassword": req.api_password}
        resp = requests.post(url, json=params)
        decoded = self.decode_response(resp)
        return Response(decoded["ResultCode"], decoded["Token"])
