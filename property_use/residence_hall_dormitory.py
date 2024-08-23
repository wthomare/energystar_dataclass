from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    HasComputerLab,
    HasDiningHall,
    NumberOfRooms,
    PercentCooled,
    PercentHeated,
    TotalGrossFloorArea,
)


@dataclass
class ResidenceHallDormitoryType:
    class Meta:
        name = "residenceHallDormitoryType"

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
    use_details: Optional["ResidenceHallDormitoryType.UseDetails"] = field(
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
        total_gross_floor_area: Optional[TotalGrossFloorArea] = field(
            default=None,
            metadata={
                "name": "totalGrossFloorArea",
                "type": "Element",
                "required": True,
            },
        )
        number_of_rooms: Optional[NumberOfRooms] = field(
            default=None,
            metadata={
                "name": "numberOfRooms",
                "type": "Element",
            },
        )
        percent_heated: Optional[PercentHeated] = field(
            default=None,
            metadata={
                "name": "percentHeated",
                "type": "Element",
            },
        )
        percent_cooled: Optional[PercentCooled] = field(
            default=None,
            metadata={
                "name": "percentCooled",
                "type": "Element",
            },
        )
        has_computer_lab: Optional[HasComputerLab] = field(
            default=None,
            metadata={
                "name": "hasComputerLab",
                "type": "Element",
            },
        )
        has_dining_hall: Optional[HasDiningHall] = field(
            default=None,
            metadata={
                "name": "hasDiningHall",
                "type": "Element",
            },
        )


@dataclass
class ResidenceHallDormitory(ResidenceHallDormitoryType):
    """
    Buildings associated with educational institutions or military facilities which
    offer multiple accommodations for long-term residents.
    """

    class Meta:
        name = "residenceHallDormitory"
