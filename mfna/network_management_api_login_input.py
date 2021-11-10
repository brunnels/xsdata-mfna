from dataclasses import dataclass, field
from typing import Optional
from .login_request import LoginRequest
from .request_header import RequestHeader

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class NetworkManagementApiLoginInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["NetworkManagementApiLoginInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["NetworkManagementApiLoginInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        request_header: Optional[RequestHeader] = field(
            default=None,
            metadata={
                "name": "RequestHeader",
                "type": "Element",
                "namespace": "http://microfocus.com/nas/2020/08",
            }
        )

    @dataclass
    class Body:
        login: Optional[LoginRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://microfocus.com/nas/2020/08",
            }
        )
