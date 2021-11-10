from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class RequestHeader:
    class Meta:
        namespace = "http://microfocus.com/nas/2020/08"

    drop_null_elements: Optional[str] = field(
        default=None,
        metadata={
            "name": "DropNullElements",
            "type": "Element",
            "required": True,
        }
    )
