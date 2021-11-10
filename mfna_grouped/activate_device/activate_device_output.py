from dataclasses import dataclass, field
from typing import Optional
from .activate_device_response import ActivateDeviceResponse
from ..nas_fault import NasFault

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class ActivateDeviceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["ActivateDeviceOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        activate_device_response: Optional[ActivateDeviceResponse] = field(
            default=None,
            metadata={
                "name": "activate_deviceResponse",
                "type": "Element",
                "namespace": "http://microfocus.com/nas/2020/08",
            }
        )
        fault: Optional["ActivateDeviceOutput.Body.Fault"] = field(
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
            detail: Optional["ActivateDeviceOutput.Body.Fault.Detail"] = field(
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
