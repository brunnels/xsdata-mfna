from dataclasses import dataclass, field
from typing import Optional
from .logout_response import LogoutResponse
from .nas_fault import NasFault

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class NetworkManagementApiLogoutOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NetworkManagementApiLogoutOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        logout_response: Optional[LogoutResponse] = field(
            default=None,
            metadata={
                "name": "logoutResponse",
                "type": "Element",
                "namespace": "http://microfocus.com/nas/2020/08",
            }
        )
        fault: Optional["NetworkManagementApiLogoutOutput.Body.Fault"] = field(
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
            detail: Optional["NetworkManagementApiLogoutOutput.Body.Fault.Detail"] = field(
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
                        "name": "error",
                        "type": "Element",
                        "namespace": "http://microfocus.com/nas/2020/08",
                    }
                )
