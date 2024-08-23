from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    CookingFacilities,
    GrossFloorAreaUsedForFoodPreparation,
    GymnasiumFloorArea,
    IsHighSchool,
    MonthsInUse,
    NumberOfComputers,
    NumberOfWalkInRefrigerationUnits,
    NumberOfWorkers,
    OpenOnWeekends,
    PercentCooled,
    PercentHeated,
    SchoolDistrict,
    StudentSeatingCapacity,
    TotalGrossFloorArea,
)


@dataclass
class K12SchoolType:
    class Meta:
        name = "k12SchoolType"

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
    use_details: Optional["K12SchoolType.UseDetails"] = field(
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
        open_on_weekends: Optional[OpenOnWeekends] = field(
            default=None,
            metadata={
                "name": "openOnWeekends",
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
        number_of_computers: Optional[NumberOfComputers] = field(
            default=None,
            metadata={
                "name": "numberOfComputers",
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
        is_high_school: Optional[IsHighSchool] = field(
            default=None,
            metadata={
                "name": "isHighSchool",
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
        school_district: Optional[SchoolDistrict] = field(
            default=None,
            metadata={
                "name": "schoolDistrict",
                "type": "Element",
            },
        )
        student_seating_capacity: Optional[StudentSeatingCapacity] = field(
            default=None,
            metadata={
                "name": "studentSeatingCapacity",
                "type": "Element",
            },
        )
        number_of_workers: Optional[NumberOfWorkers] = field(
            default=None,
            metadata={
                "name": "numberOfWorkers",
                "type": "Element",
            },
        )
        gymnasium_floor_area: Optional[GymnasiumFloorArea] = field(
            default=None,
            metadata={
                "name": "gymnasiumFloorArea",
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


@dataclass
class K12School(K12SchoolType):
    """
    Buildings or campuses used as a school for Kindergarten through 12th grade
    students.
    """

    class Meta:
        name = "k12School"
