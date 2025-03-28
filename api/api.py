import requests

LIVE_PORT = 18080
TEST_PORT = 18081


class Client:
    def __init__(self, apiPassword: str, port: int) -> None:
        self._port = port
        self._token = self._get_token(apiPassword)

    def _get_token(self, apiPassword: str) -> None:
        url = self._make_url("/token")
        reqBody = {"APIPassword": apiPassword}
        resp = requests.post(url, json=reqBody)
        decoded = self._handle_response(resp)
        return decoded["Token"]

    def _make_url(self, path) -> str:
        return f"http://localhost:{self._port}/kabusapi{path}"

    def _handle_response(self, resp: requests.Response) -> dict:
        resp.raise_for_status()
        decoded = resp.json()
        if "Code" in decoded and decoded["Code"] != 0:
            raise resp
        return decoded


class LiveClient(Client):
    def __init__(self, apiPassword: str) -> None:
        super().__init__(apiPassword, LIVE_PORT)


class TestClient(Client):
    def __init__(self, apiPassword: str) -> None:
        super().__init__(apiPassword, TEST_PORT)
