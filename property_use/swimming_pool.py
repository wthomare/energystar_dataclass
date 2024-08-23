from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    MonthsInUse,
    PoolLocation,
    PoolSize,
)


@dataclass
class SwimmingPoolType:
    class Meta:
        name = "swimmingPoolType"

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
    use_details: Optional["SwimmingPoolType.UseDetails"] = field(
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
        pool_size: Optional[PoolSize] = field(
            default=None,
            metadata={
                "name": "poolSize",
                "type": "Element",
                "required": True,
            },
        )
        pool_location: Optional[PoolLocation] = field(
            default=None,
            metadata={
                "name": "poolLocation",
                "type": "Element",
            },
        )
        months_in_use: Optional[MonthsInUse] = field(
            default=None,
            metadata={
                "name": "monthsInUse",
                "type": "Element",
            },
        )


@dataclass
class SwimmingPool(SwimmingPoolType):
    """
    Any heated swimming pools located either inside or outside.
    """

    class Meta:
        name = "swimmingPool"
