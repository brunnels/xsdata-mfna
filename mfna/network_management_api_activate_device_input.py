from dataclasses import dataclass, field
from typing import Optional
from .activate_device_request import ActivateDeviceRequest
from .request_header import RequestHeader

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class NetworkManagementApiActivateDeviceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional["NetworkManagementApiActivateDeviceInput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: Optional["NetworkManagementApiActivateDeviceInput.Body"] = field(
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
        activate_device: Optional[ActivateDeviceRequest] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://microfocus.com/nas/2020/08",
            }
        )
