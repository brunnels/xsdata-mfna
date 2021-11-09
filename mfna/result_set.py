from dataclasses import dataclass, field
from typing import List
from .row import Row

__NAMESPACE__ = "http://microfocus.com/nas/2020/08"


@dataclass
class ResultSet:
    row: List[Row] = field(
        default_factory=list,
        metadata={
            "name": "Row",
            "type": "Element",
            "namespace": "http://microfocus.com/nas/2020/08",
        }
    )
