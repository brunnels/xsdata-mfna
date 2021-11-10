from dataclasses import dataclass, field
from typing import Optional
from .logout_input_parms import LogoutInputParms
from ..request_header import RequestHeader

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class LogoutRequest:
    class Meta:
        name = "logoutRequest"

    parameters: Optional[LogoutInputParms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    request_header: Optional[RequestHeader] = field(
        default=None,
        metadata={
            "name": "RequestHeader",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
        }
    )
