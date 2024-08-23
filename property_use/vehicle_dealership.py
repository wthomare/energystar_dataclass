from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    AverageNumberOfVehiclesInInventory,
    NumberOfComputers,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class VehicleDealershipType:
    class Meta:
        name = "vehicleDealershipType"

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
    use_details: Optional["VehicleDealershipType.UseDetails"] = field(
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
        number_of_workers: Optional[NumberOfWorkers] = field(
            default=None,
            metadata={
                "name": "numberOfWorkers",
                "type": "Element",
            },
        )
        average_number_of_vehicles_in_inventory: Optional[
            AverageNumberOfVehiclesInInventory
        ] = field(
            default=None,
            metadata={
                "name": "averageNumberOfVehiclesInInventory",
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
        weekly_operating_hours: Optional[WeeklyOperatingHours] = field(
            default=None,
            metadata={
                "name": "weeklyOperatingHours",
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


@dataclass
class VehicleDealership(VehicleDealershipType):
    """
    Vehicle Dealership refers to buildings used for the sale of new or used light-,
    medium- and heavy-duty cars and trucks.
    """

    class Meta:
        name = "vehicleDealership"
