import requests


class Handler:
    def __init__(self, port: int, path: str) -> None:
        self._port = port
        self._path = path

    def make_url(self) -> str:
        return f"http://localhost:{self._port}/kabusapi{self._path}"

    def decode_response(self, resp: requests.Response) -> dict:
        resp.raise_for_status()
        decoded = resp.json()
        if "Code" in decoded and decoded["Code"] != 0:
            raise resp
        return decoded
