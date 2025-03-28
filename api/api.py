import datetime
import requests

import future_code

LIVE_PORT = 18080
TEST_PORT = 18081


class Client:
    def __init__(self, api_password: str, port: int) -> None:
        self._port = port
        self._token = self._get_token(api_password)

    def _get_token(self, api_password: str) -> None:
        url = self._make_url("/token")
        params = {"APIPassword": api_password}
        resp = requests.post(url, json=params)
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

    def symbolname_future_get(
        self, future_code: future_code.FutureCode, deriv_month: datetime.date = None
    ) -> tuple[str, str]:
        if deriv_month is None:
            year_month = 0
        else:
            year_month = deriv_month.strftime("%Y%m")
        url = self._make_url("/symbolname/future")
        params = {"FutureCode": future_code, "DerivMonth": year_month}
        resp = requests.get(url, params=params, headers={"X-API-KEY": self._token})
        decoded = self._handle_response(resp)
        return decoded["Symbol"], decoded["SymbolName"]


class LiveClient(Client):
    def __init__(self, apiPassword: str) -> None:
        super().__init__(apiPassword, LIVE_PORT)


class TestClient(Client):
    def __init__(self, apiPassword: str) -> None:
        super().__init__(apiPassword, TEST_PORT)
