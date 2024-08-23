from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    NumberOfDcFastEvChargingStations,
    NumberOfLevelOneEvChargingStations,
    NumberOfLevelTwoEvChargingStations,
)


@dataclass
class EvChargingStationType:
    class Meta:
        name = "evChargingStationType"

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
    use_details: Optional["EvChargingStationType.UseDetails"] = field(
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
        number_of_level_one_ev_charging_stations: Optional[
            NumberOfLevelOneEvChargingStations
        ] = field(
            default=None,
            metadata={
                "name": "numberOfLevelOneEvChargingStations",
                "type": "Element",
            },
        )
        number_of_level_two_ev_charging_stations: Optional[
            NumberOfLevelTwoEvChargingStations
        ] = field(
            default=None,
            metadata={
                "name": "numberOfLevelTwoEvChargingStations",
                "type": "Element",
            },
        )
        number_of_dc_fast_ev_charging_stations: Optional[
            NumberOfDcFastEvChargingStations
        ] = field(
            default=None,
            metadata={
                "name": "numberOfDcFastEvChargingStations",
                "type": "Element",
            },
        )


@dataclass
class ElectricVehicleChargingStation(EvChargingStationType):
    """
    Electric vehicle charging station area.
    """

    class Meta:
        name = "electricVehicleChargingStation"
