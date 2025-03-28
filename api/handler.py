import requests


class Handler:
    def __init__(self, port: int) -> None:
        self._port = port

    def make_url(self, path: str) -> str:
        return f"http://localhost:{self._port}/kabusapi{path}"

    def decode_response(self, resp: requests.Response) -> dict:
        resp.raise_for_status()
        decoded = resp.json()
        if "Code" in decoded and decoded["Code"] != 0:
            raise resp
        return decoded
