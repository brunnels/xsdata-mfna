from dataclasses import dataclass, field
from typing import Optional
from .result import Result

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class ActivateDeviceResponse:
    class Meta:
        name = "activate_deviceResponse"

    result: Optional[Result] = field(
        default=None,
        metadata={
            "name": "Result",
            "type": "Element",
            "namespace": "",
        }
    )
