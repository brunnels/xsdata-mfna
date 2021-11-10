from dataclasses import dataclass, field
from typing import Optional
from .result_set import ResultSet

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class Result:
    class Meta:
        namespace = "http://microfocus.com/nas/2020/08"

    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "required": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    stack_trace: Optional[str] = field(
        default=None,
        metadata={
            "name": "StackTrace",
            "type": "Element",
        }
    )
    result_set: Optional[ResultSet] = field(
        default=None,
        metadata={
            "name": "ResultSet",
            "type": "Element",
        }
    )
