from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class LoginInputParms:
    class Meta:
        name = "loginInputParms"
        namespace = "http://microfocus.com/nas/2020/08"

    username: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
