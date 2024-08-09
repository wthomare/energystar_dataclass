from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PropertyUse:
    """
    This is used to update property use name only.
    """

    class Meta:
        name = "propertyUse"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )
