from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    MonthsMainIndoorIceRinkInUse,
    NumberOfCurlingSheets,
    NumberOfFteworkers,
    NumberOfIndoorIceRinks,
    NumberOfWeeklyIceResurfacingForAllRinks,
    SpectatorSeatingCapacity,
    TotalGrossFloorArea,
    TotalIceRinkSurfaceAreaForAllRinks,
)


@dataclass
class IceCurlingRinkType:
    class Meta:
        name = "iceCurlingRinkType"

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
    use_details: Optional["IceCurlingRinkType.UseDetails"] = field(
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
        number_of_indoor_ice_rinks: Optional[NumberOfIndoorIceRinks] = field(
            default=None,
            metadata={
                "name": "numberOfIndoorIceRinks",
                "type": "Element",
            },
        )
        total_ice_rink_surface_area_for_all_rinks: Optional[
            TotalIceRinkSurfaceAreaForAllRinks
        ] = field(
            default=None,
            metadata={
                "name": "totalIceRinkSurfaceAreaForAllRinks",
                "type": "Element",
            },
        )
        months_main_indoor_ice_rink_in_use: Optional[
            MonthsMainIndoorIceRinkInUse
        ] = field(
            default=None,
            metadata={
                "name": "monthsMainIndoorIceRinkInUse",
                "type": "Element",
            },
        )
        number_of_weekly_ice_resurfacing_for_all_rinks: Optional[
            NumberOfWeeklyIceResurfacingForAllRinks
        ] = field(
            default=None,
            metadata={
                "name": "numberOfWeeklyIceResurfacingForAllRinks",
                "type": "Element",
            },
        )
        number_of_fteworkers: Optional[NumberOfFteworkers] = field(
            default=None,
            metadata={
                "name": "numberOfFTEWorkers",
                "type": "Element",
            },
        )
        number_of_curling_sheets: Optional[NumberOfCurlingSheets] = field(
            default=None,
            metadata={
                "name": "numberOfCurlingSheets",
                "type": "Element",
            },
        )
        spectator_seating_capacity: Optional[SpectatorSeatingCapacity] = field(
            default=None,
            metadata={
                "name": "spectatorSeatingCapacity",
                "type": "Element",
            },
        )


@dataclass
class IceCurlingRink(IceCurlingRinkType):
    """Buildings that include one or more indoor ice sheets used for public or
    private, recreational or professional skating, hockey, or ringette.

    Buildings that are exclusively used for curling are not currently
    eligible to earn an ENERGY STAR score but can be benchmarked using
    this property use. Gross Floor Area should include all space within
    the building(s), including ice area, spectator areas, concession
    stands, restaurants, retail areas, locker rooms,
    administrative/office areas, employee break rooms, mechanical rooms,
    and storage areas.Larger facilities primarily serving professional
    or collegiate functions and with significant spectator seating
    (usually above 5,000 seats) should review the definition for Indoor
    Arena to determine the best classification
    """

    class Meta:
        name = "iceCurlingRink"
