from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    AreaOfAllWalkInRefrigerationUnits,
    CookingFacilities,
    ExteriorEntranceToThePublic,
    LengthOfAllOpenClosedRefrigerationUnits,
    NumberOfCashRegisters,
    NumberOfComputers,
    NumberOfOpenClosedRefrigerationUnits,
    NumberOfWalkInRefrigerationUnits,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    SingleStore,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class WholesaleClubSupercenterType:
    class Meta:
        name = "wholesaleClubSupercenterType"

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
    use_details: Optional["WholesaleClubSupercenterType.UseDetails"] = field(
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
        exterior_entrance_to_the_public: Optional[
            ExteriorEntranceToThePublic
        ] = field(
            default=None,
            metadata={
                "name": "exteriorEntranceToThePublic",
                "type": "Element",
            },
        )
        weekly_operating_hours: Optional[WeeklyOperatingHours] = field(
            default=None,
            metadata={
                "name": "weeklyOperatingHours",
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
        number_of_cash_registers: Optional[NumberOfCashRegisters] = field(
            default=None,
            metadata={
                "name": "numberOfCashRegisters",
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
        number_of_open_closed_refrigeration_units: Optional[
            NumberOfOpenClosedRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfOpenClosedRefrigerationUnits",
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
        single_store: Optional[SingleStore] = field(
            default=None,
            metadata={
                "name": "singleStore",
                "type": "Element",
            },
        )
        area_of_all_walk_in_refrigeration_units: Optional[
            AreaOfAllWalkInRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "areaOfAllWalkInRefrigerationUnits",
                "type": "Element",
            },
        )
        length_of_all_open_closed_refrigeration_units: Optional[
            LengthOfAllOpenClosedRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "lengthOfAllOpenClosedRefrigerationUnits",
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


@dataclass
class WholesaleClubSupercenter(WholesaleClubSupercenterType):
    """
    Buildings used to conduct the retail sale of a wide variety of merchandise,
    typically in bulk quantities.
    """

    class Meta:
        name = "wholesaleClubSupercenter"
