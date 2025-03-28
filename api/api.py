import auth_token
import board_get
import register_put
import symbolname_future_get
import symbolname_option_get
import unregister_all_put

LIVE_PORT = 18080
TEST_PORT = 18081


class Client:
    def __init__(self, api_password: str, port: int) -> None:
        self._port = port
        self._set_token(api_password)

    def _set_token(self, api_password: str) -> None:
        handler = auth_token.Handler(self._port)
        resp = handler.handle(auth_token.Request(api_password))
        self._token = resp.token

    def board_get(self, req: board_get.Request) -> board_get.Response:
        handler = board_get.Handler(self._port, self._token)
        return handler.handle(req)

    def register_put(self, req: register_put.Request) -> register_put.Response:
        handler = register_put.Handler(self._port, self._token)
        return handler.handle(req)

    def symbolname_future_get(
        self, req: symbolname_future_get.Request
    ) -> symbolname_future_get.Response:
        handler = symbolname_future_get.Handler(self._port, self._token)
        return handler.handle(req)

    def symbolname_option_get(
        self, req: symbolname_option_get.Request
    ) -> symbolname_option_get.Response:
        handler = symbolname_option_get.Handler(self._port, self._token)
        return handler.handle(req)

    def unregister_all_put(self) -> None:
        handler = unregister_all_put.Handler(self._port, self._token)
        handler.handle()


class LiveClient(Client):
    def __init__(self, apiPassword: str) -> None:
        super().__init__(apiPassword, LIVE_PORT)


class TestClient(Client):
    def __init__(self, apiPassword: str) -> None:
        super().__init__(apiPassword, TEST_PORT)
