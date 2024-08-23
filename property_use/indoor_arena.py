from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    EnclosedFloorArea,
    IceEvents,
    NumberOfComputers,
    NumberOfConcertShowEventsPerYear,
    NumberOfSpecialOtherEventsPerYear,
    NumberOfSportingEventsPerYear,
    NumberOfWalkInRefrigerationUnits,
    PercentCooled,
    PercentHeated,
    SizeOfElectronicScoreBoards,
    TotalGrossFloorArea,
)


@dataclass
class IndoorArenaType:
    class Meta:
        name = "indoorArenaType"

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
    use_details: Optional["IndoorArenaType.UseDetails"] = field(
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
        enclosed_floor_area: Optional[EnclosedFloorArea] = field(
            default=None,
            metadata={
                "name": "enclosedFloorArea",
                "type": "Element",
            },
        )
        number_of_sporting_events_per_year: Optional[
            NumberOfSportingEventsPerYear
        ] = field(
            default=None,
            metadata={
                "name": "numberOfSportingEventsPerYear",
                "type": "Element",
            },
        )
        number_of_concert_show_events_per_year: Optional[
            NumberOfConcertShowEventsPerYear
        ] = field(
            default=None,
            metadata={
                "name": "numberOfConcertShowEventsPerYear",
                "type": "Element",
            },
        )
        number_of_special_other_events_per_year: Optional[
            NumberOfSpecialOtherEventsPerYear
        ] = field(
            default=None,
            metadata={
                "name": "numberOfSpecialOtherEventsPerYear",
                "type": "Element",
            },
        )
        size_of_electronic_score_boards: Optional[
            SizeOfElectronicScoreBoards
        ] = field(
            default=None,
            metadata={
                "name": "sizeOfElectronicScoreBoards",
                "type": "Element",
            },
        )
        ice_events: Optional[IceEvents] = field(
            default=None,
            metadata={
                "name": "iceEvents",
                "type": "Element",
            },
        )
        number_of_computers: Optional[NumberOfComputers] = field(
            default=None,
            metadata={
                "name": "numberOfComputers",
                "type": "Element",
            },
        )
        number_of_walk_in_refrigeration_units: Optional[
            NumberOfWalkInRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfWalkInRefrigerationUnits",
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
class IndoorArena(IndoorArenaType):
    """Enclosed structures used for professional or collegiate sports and
    entertainment events.

    (typically with a capacity of at least 5,000 seats)
    """

    class Meta:
        name = "indoorArena"
