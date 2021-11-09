from dataclasses import dataclass, field
from typing import Optional
from .activate_device_input_parms import ActivateDeviceInputParms
from .request_header import RequestHeader

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class ActivateDeviceRequest:
    class Meta:
        name = "activate_deviceRequest"

    parameters: Optional[ActivateDeviceInputParms] = field(
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
