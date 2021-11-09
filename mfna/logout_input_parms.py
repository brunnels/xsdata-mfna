from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class LogoutInputParms:
    class Meta:
        name = "logoutInputParms"
        namespace = "http://microfocus.com/nas/2020/08"

    sessionid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
