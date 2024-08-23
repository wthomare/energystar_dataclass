from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    CustomUseDetail1,
    CustomUseDetail2,
)


@dataclass
class CustomUseType:
    class Meta:
        name = "customUseType"

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
    use_details: Optional["CustomUseType.UseDetails"] = field(
        default=None,
        metadata={
            "name": "useDetails",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    audit: Optional[LogType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class UseDetails:
        custom_use_detail1: Optional[CustomUseDetail1] = field(
            default=None,
            metadata={
                "name": "customUseDetail1",
                "type": "Element",
            },
        )
        custom_use_detail2: Optional[CustomUseDetail2] = field(
            default=None,
            metadata={
                "name": "customUseDetail2",
                "type": "Element",
            },
        )


@dataclass
class CustomUse(CustomUseType):
    """
    A user-defined property use with custom user-defined use details.
    """

    class Meta:
        name = "customUse"
