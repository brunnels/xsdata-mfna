from dataclasses import dataclass, field
from typing import Optional
from .login_response import LoginResponse
from .nas_fault import NasFault

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class NetworkManagementApiLoginOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NetworkManagementApiLoginOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        login_response: Optional[LoginResponse] = field(
            default=None,
            metadata={
                "name": "loginResponse",
                "type": "Element",
                "namespace": "http://microfocus.com/nas/2020/08",
            }
        )
        fault: Optional["NetworkManagementApiLoginOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional["NetworkManagementApiLoginOutput.Body.Fault.Detail"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

            @dataclass
            class Detail:
                nas_fault: Optional[NasFault] = field(
                    default=None,
                    metadata={
                        "name": "nasFault",
                        "type": "Element",
                        "namespace": "http://microfocus.com/nas/2020/08",
                    }
                )
