from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class ActivateDeviceInputParms:
    class Meta:
        name = "activate_deviceInputParms"
        namespace = "http://microfocus.com/nas/2020/08"

    sessionid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
    host: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
    fqdn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
    deviceid: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
