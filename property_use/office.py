import sys
from pathlib import Path


file = Path(__file__).resolve()
parent, top = file.parent, file.parents[3]
sys.path.append(str(top))

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

@dataclass
class OfficeType:
    class Meta:
        name = "officeType"

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
    use_details: Optional[UseDetails] = field(
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
class Office(OfficeType):
    """
    Buildings used for the conduct of commercial or governmental business
    activities.
    """

    class Meta:
        name = "office"



if __name__ == '__main__':
    # xsdata C:\Users\wilfr\Downloads\portfoliomanager-schemas-22.0\propertyUse\office.xsd --package test/fixtures.primer
    
    details = UseDetails(total_gross_floor_area = 100, number_of_workers = 10)
    bat_A = Office(name='Test', use_details = details)
    print(bat_A.name)
    print(bat_A.use_details.number_of_workers)