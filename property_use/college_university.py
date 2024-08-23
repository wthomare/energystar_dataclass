from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    Enrollment,
    GrantDollars,
    NumberOfComputers,
    NumberOfFteworkers,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class CollegeUniversityType:
    class Meta:
        name = "collegeUniversityType"

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
    use_details: Optional["CollegeUniversityType.UseDetails"] = field(
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
        number_of_computers: Optional[NumberOfComputers] = field(
            default=None,
            metadata={
                "name": "numberOfComputers",
                "type": "Element",
            },
        )
        enrollment: Optional[Enrollment] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        grant_dollars: Optional[GrantDollars] = field(
            default=None,
            metadata={
                "name": "grantDollars",
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


@dataclass
class CollegeUniversity(CollegeUniversityType):
    """
    Buildings used for the purpose of higher education.
    """

    class Meta:
        name = "collegeUniversity"
