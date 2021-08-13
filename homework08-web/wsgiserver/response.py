import dataclasses
import http.client
import typing as tp


@dataclasses.dataclass
class HTTPResponse:
    status: int
    headers: tp.Dict[str, str] = dataclasses.field(default_factory=dict)
    body: bytes = b""

    def to_http1(self) -> bytes:
        return (
            f"HTTP/1.1 {self.status} {http.client.responses[self.status]}\r\n"
            + "\r\n".join(
                [
                    f"{key}: {value}"
                    for key, value in zip(self.headers.keys(), self.headers.values())
                ]
            )
            + f"\r\n\r\n{self.body.decode()}"
        ).encode()


@dataclasses.dataclass
class WSGIResponse(HTTPResponse):
    status: int = 200

    def start_response(
        self, status: str, response_headers: tp.List[tp.Tuple[str, str]], exc_info=None
    ) -> None:
        self.headers = {key: value for (key, value) in response_headers}
        self.status = int(status.split(" ")[0])
