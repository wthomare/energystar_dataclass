from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    NumberOfComputers,
    NumberOfWorkers,
    PercentOfficeCooled,
    PercentOfficeHeated,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class BankBranchType:
    class Meta:
        name = "bankBranchType"

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
    use_details: Optional["BankBranchType.UseDetails"] = field(
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
        number_of_computers: Optional[NumberOfComputers] = field(
            default=None,
            metadata={
                "name": "numberOfComputers",
                "type": "Element",
            },
        )
        percent_office_cooled: Optional[PercentOfficeCooled] = field(
            default=None,
            metadata={
                "name": "percentOfficeCooled",
                "type": "Element",
            },
        )
        percent_office_heated: Optional[PercentOfficeHeated] = field(
            default=None,
            metadata={
                "name": "percentOfficeHeated",
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


@dataclass
class BankBranch(BankBranchType):
    """
    A commercial banking outlet that offers banking services to walk-in customers.
    """

    class Meta:
        name = "bankBranch"
