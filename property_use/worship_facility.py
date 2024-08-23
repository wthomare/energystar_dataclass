from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    CeilingHeight,
    CookingFacilities,
    GrossFloorAreaUsedForFoodPreparation,
    NumberOfCommercialRefrigerationUnits,
    NumberOfComputers,
    NumberOfWeekdaysOpen,
    PercentCooled,
    PercentHeated,
    SeatingCapacity,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class WorshipFacilityType:
    class Meta:
        name = "worshipFacilityType"

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
    use_details: Optional["WorshipFacilityType.UseDetails"] = field(
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
        weekly_operating_hours: Optional[WeeklyOperatingHours] = field(
            default=None,
            metadata={
                "name": "weeklyOperatingHours",
                "type": "Element",
            },
        )
        seating_capacity: Optional[SeatingCapacity] = field(
            default=None,
            metadata={
                "name": "seatingCapacity",
                "type": "Element",
            },
        )
        ceiling_height: Optional[CeilingHeight] = field(
            default=None,
            metadata={
                "name": "ceilingHeight",
                "type": "Element",
            },
        )
        cooking_facilities: Optional[CookingFacilities] = field(
            default=None,
            metadata={
                "name": "cookingFacilities",
                "type": "Element",
            },
        )
        gross_floor_area_used_for_food_preparation: Optional[
            GrossFloorAreaUsedForFoodPreparation
        ] = field(
            default=None,
            metadata={
                "name": "grossFloorAreaUsedForFoodPreparation",
                "type": "Element",
            },
        )
        number_of_weekdays_open: Optional[NumberOfWeekdaysOpen] = field(
            default=None,
            metadata={
                "name": "numberOfWeekdaysOpen",
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
        number_of_commercial_refrigeration_units: Optional[
            NumberOfCommercialRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfCommercialRefrigerationUnits",
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


@dataclass
class WorshipFacility(WorshipFacilityType):
    """Buildings used as places of worship.

    This includes churches, temples, mosques, synagogues, meetinghouses,
    or any other Buildings that primarily function as a place of
    religious worship.
    """

    class Meta:
        name = "worshipFacility"
