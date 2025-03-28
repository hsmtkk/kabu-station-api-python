import requests

import enum_code
import handler


class Handler(handler.Handler):
    def __init__(self, port: int, token: str):
        super().__init__(port)
        self._token = token

    def handle(self) -> None:
        url = self.make_url("/unregister/all")
        resp = requests.put(url, headers={"X-API-KEY": self._token})
        self.decode_response(resp)
