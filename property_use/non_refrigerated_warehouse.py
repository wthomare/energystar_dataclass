from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    ClearHeight,
    NumberOfWalkInRefrigerationUnits,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    PercentUsedForColdStorage,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class NonRefrigeratedWarehouseType:
    class Meta:
        name = "nonRefrigeratedWarehouseType"

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
    use_details: Optional["NonRefrigeratedWarehouseType.UseDetails"] = field(
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
        number_of_workers: Optional[NumberOfWorkers] = field(
            default=None,
            metadata={
                "name": "numberOfWorkers",
                "type": "Element",
            },
        )
        percent_used_for_cold_storage: Optional[PercentUsedForColdStorage] = (
            field(
                default=None,
                metadata={
                    "name": "percentUsedForColdStorage",
                    "type": "Element",
                },
            )
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
        clear_height: Optional[ClearHeight] = field(
            default=None,
            metadata={
                "name": "clearHeight",
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
class NonRefrigeratedWarehouse(NonRefrigeratedWarehouseType):
    """
    Unrefrigerated Buildings that are used to store goods, manufactured products,
    merchandise or raw materials.
    """

    class Meta:
        name = "nonRefrigeratedWarehouse"
