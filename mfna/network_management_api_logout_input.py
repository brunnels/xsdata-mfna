from dataclasses import dataclass, field
from typing import Optional
from .logout_request import LogoutRequest
from .request_header import RequestHeader

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class NetworkManagementApiLogoutInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["NetworkManagementApiLogoutInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["NetworkManagementApiLogoutInput.Body"] = field(
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
        logout_request: Optional[LogoutRequest] = field(
            default=None,
            metadata={
                "name": "logoutRequest",
                "type": "Element",
                "namespace": "http://microfocus.com/nas/2020/08",
            }
        )
