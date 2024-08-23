from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    GrossFloorAreaUsedForFoodPreparation,
    HasLaboratory,
    IsTertiaryCare,
    LicensedBedCapacity,
    MaximumNumberOfFloors,
    NumberOfFteworkers,
    NumberOfMriMachines,
    NumberOfStaffedBeds,
    NumberOfSterilizationUnits,
    NumberOfWorkers,
    OnSiteLaundryFacility,
    OwnedBy,
    PercentCooled,
    PercentHeated,
    TotalGrossFloorArea,
)


@dataclass
class HospitalType:
    class Meta:
        name = "hospitalType"

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
    use_details: Optional["HospitalType.UseDetails"] = field(
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
        gross_floor_area_used_for_food_preparation: Optional[
            GrossFloorAreaUsedForFoodPreparation
        ] = field(
            default=None,
            metadata={
                "name": "grossFloorAreaUsedForFoodPreparation",
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
        number_of_staffed_beds: Optional[NumberOfStaffedBeds] = field(
            default=None,
            metadata={
                "name": "numberOfStaffedBeds",
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
        number_of_workers: Optional[NumberOfWorkers] = field(
            default=None,
            metadata={
                "name": "numberOfWorkers",
                "type": "Element",
            },
        )
        number_of_mri_machines: Optional[NumberOfMriMachines] = field(
            default=None,
            metadata={
                "name": "numberOfMriMachines",
                "type": "Element",
            },
        )
        number_of_sterilization_units: Optional[NumberOfSterilizationUnits] = (
            field(
                default=None,
                metadata={
                    "name": "numberOfSterilizationUnits",
                    "type": "Element",
                },
            )
        )
        on_site_laundry_facility: Optional[OnSiteLaundryFacility] = field(
            default=None,
            metadata={
                "name": "onSiteLaundryFacility",
                "type": "Element",
            },
        )
        has_laboratory: Optional[HasLaboratory] = field(
            default=None,
            metadata={
                "name": "hasLaboratory",
                "type": "Element",
            },
        )
        is_tertiary_care: Optional[IsTertiaryCare] = field(
            default=None,
            metadata={
                "name": "isTertiaryCare",
                "type": "Element",
            },
        )
        maximum_number_of_floors: Optional[MaximumNumberOfFloors] = field(
            default=None,
            metadata={
                "name": "maximumNumberOfFloors",
                "type": "Element",
            },
        )
        owned_by: Optional[OwnedBy] = field(
            default=None,
            metadata={
                "name": "ownedBy",
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
class Hospital(HospitalType):
    """A general medical and surgical hospital (including critical access hospitals
    and children’s hospitals).

    These facilities provide acute care services intended to treat
    patients for short periods of time, including emergency medical
    care, physician's office services, diagnostic care, ambulatory care,
    surgical care, and limited specialty services such as rehabilitation
    and cancer care.
    """

    class Meta:
        name = "hospital"
