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
class BarracksType:
    class Meta:
        name = "barracksType"

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
    use_details: Optional["BarracksType.UseDetails"] = field(
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
        number_of_rooms: Optional[NumberOfRooms] = field(
            default=None,
            metadata={
                "name": "numberOfRooms",
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
        percent_heated: Optional[PercentHeated] = field(
            default=None,
            metadata={
                "name": "percentHeated",
                "type": "Element",
            },
        )


@dataclass
class Barracks(BarracksType):
    """
    Residential buildings associated with military facilities or educational
    institutions which offer multiple accommodations for long-term residents.
    """

    class Meta:
        name = "barracks"
