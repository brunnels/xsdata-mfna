from dataclasses import dataclass, field
from typing import Optional
from ..result import Result

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class LogoutResponse:
    class Meta:
        name = "logoutResponse"

    result: Optional[Result] = field(
        default=None,
        metadata={
            "name": "Result",
            "type": "Element",
            "namespace": "",
        }
    )
