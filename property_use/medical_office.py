from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    NumberOfComputers,
    NumberOfMriMachines,
    NumberOfSurgicalOperatingBeds,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    SurgeryCenterFloorArea,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class MedicalOfficeType:
    class Meta:
        name = "medicalOfficeType"

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
    use_details: Optional["MedicalOfficeType.UseDetails"] = field(
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
        weekly_operating_hours: Optional[WeeklyOperatingHours] = field(
            default=None,
            metadata={
                "name": "weeklyOperatingHours",
                "type": "Element",
            },
        )
        number_of_surgical_operating_beds: Optional[
            NumberOfSurgicalOperatingBeds
        ] = field(
            default=None,
            metadata={
                "name": "numberOfSurgicalOperatingBeds",
                "type": "Element",
            },
        )
        surgery_center_floor_area: Optional[SurgeryCenterFloorArea] = field(
            default=None,
            metadata={
                "name": "surgeryCenterFloorArea",
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
        number_of_computers: Optional[NumberOfComputers] = field(
            default=None,
            metadata={
                "name": "numberOfComputers",
                "type": "Element",
            },
        )


@dataclass
class MedicalOffice(MedicalOfficeType):
    """
    Medical Office Buildings used to provide diagnosis and treatment for medical,
    dental, or psychiatric outpatient care.
    """

    class Meta:
        name = "medicalOffice"
