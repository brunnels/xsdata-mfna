from dataclasses import dataclass, field
from typing import Optional
from .login_input_parms import LoginInputParms
from .request_header import RequestHeader

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class LoginRequest:
    class Meta:
        name = "loginRequest"

    parameters: Optional[LoginInputParms] = field(
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
