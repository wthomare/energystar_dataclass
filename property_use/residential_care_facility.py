from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    AverageNumberOfResidents,
    LicensedBedCapacity,
    MaximumResidentCapacity,
    NumberOfCommercialRefrigerationUnits,
    NumberOfCommercialWashingMachines,
    NumberOfComputers,
    NumberOfResidentialLiftSystems,
    NumberOfResidentialLivingUnits,
    NumberOfResidentialWashingMachines,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    TotalGrossFloorArea,
)


@dataclass
class ResidentialCareFacilityType:
    class Meta:
        name = "residentialCareFacilityType"

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
    use_details: Optional["ResidentialCareFacilityType.UseDetails"] = field(
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
        number_of_residential_living_units: Optional[
            NumberOfResidentialLivingUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfResidentialLivingUnits",
                "type": "Element",
            },
        )
        average_number_of_residents: Optional[AverageNumberOfResidents] = (
            field(
                default=None,
                metadata={
                    "name": "averageNumberOfResidents",
                    "type": "Element",
                },
            )
        )
        maximum_resident_capacity: Optional[MaximumResidentCapacity] = field(
            default=None,
            metadata={
                "name": "maximumResidentCapacity",
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
        number_of_commercial_refrigeration_units: Optional[
            NumberOfCommercialRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfCommercialRefrigerationUnits",
                "type": "Element",
            },
        )
        number_of_commercial_washing_machines: Optional[
            NumberOfCommercialWashingMachines
        ] = field(
            default=None,
            metadata={
                "name": "numberOfCommercialWashingMachines",
                "type": "Element",
            },
        )
        number_of_residential_washing_machines: Optional[
            NumberOfResidentialWashingMachines
        ] = field(
            default=None,
            metadata={
                "name": "numberOfResidentialWashingMachines",
                "type": "Element",
            },
        )
        number_of_residential_lift_systems: Optional[
            NumberOfResidentialLiftSystems
        ] = field(
            default=None,
            metadata={
                "name": "numberOfResidentialLiftSystems",
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
        licensed_bed_capacity: Optional[LicensedBedCapacity] = field(
            default=None,
            metadata={
                "name": "licensedBedCapacity",
                "type": "Element",
            },
        )


@dataclass
class ResidentialCareFacility(ResidentialCareFacilityType):
    """
    Buildings that house and provide care and assistance for elderly residents.
    """

    class Meta:
        name = "residentialCareFacility"
