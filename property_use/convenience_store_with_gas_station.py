from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    AreaOfAllWalkInRefrigerationUnits,
    CookingFacilities,
    LengthOfAllOpenClosedRefrigerationUnits,
    NumberOfCashRegisters,
    NumberOfComputers,
    NumberOfCookingEquipmentUnits,
    NumberOfFteworkers,
    NumberOfOpenClosedRefrigerationUnits,
    NumberOfWalkInRefrigerationUnits,
    NumberOfWarmingHeatingEquipmentUnits,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class ConvenienceStoreWithGasStationType:
    class Meta:
        name = "convenienceStoreWithGasStationType"

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
    use_details: Optional["ConvenienceStoreWithGasStationType.UseDetails"] = (
        field(
            default=None,
            metadata={
                "name": "useDetails",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
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
        number_of_walk_in_refrigeration_units: Optional[
            NumberOfWalkInRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfWalkInRefrigerationUnits",
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
        number_of_cash_registers: Optional[NumberOfCashRegisters] = field(
            default=None,
            metadata={
                "name": "numberOfCashRegisters",
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
        number_of_fteworkers: Optional[NumberOfFteworkers] = field(
            default=None,
            metadata={
                "name": "numberOfFTEWorkers",
                "type": "Element",
            },
        )
        number_of_cooking_equipment_units: Optional[
            NumberOfCookingEquipmentUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfCookingEquipmentUnits",
                "type": "Element",
            },
        )
        number_of_warming_heating_equipment_units: Optional[
            NumberOfWarmingHeatingEquipmentUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfWarmingHeatingEquipmentUnits",
                "type": "Element",
            },
        )


@dataclass
class ConvenienceStoreWithGasStation(ConvenienceStoreWithGasStationType):
    """
    Buildings that are co-located with gas stations and are used for the sale of a
    limited range of items such as groceries, toiletries, newspapers, soft drinks,
    tobacco products, and other everyday items.
    """

    class Meta:
        name = "convenienceStoreWithGasStation"
