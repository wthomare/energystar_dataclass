from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    DeliveryFacility,
    NumberOfComputers,
    NumberOfLettersPackagesPerYear,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class MailingCenterPostOfficeType:
    class Meta:
        name = "mailingCenterPostOfficeType"

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
    use_details: Optional["MailingCenterPostOfficeType.UseDetails"] = field(
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
        number_of_computers: Optional[NumberOfComputers] = field(
            default=None,
            metadata={
                "name": "numberOfComputers",
                "type": "Element",
            },
        )
        number_of_letters_packages_per_year: Optional[
            NumberOfLettersPackagesPerYear
        ] = field(
            default=None,
            metadata={
                "name": "numberOfLettersPackagesPerYear",
                "type": "Element",
            },
        )
        delivery_facility: Optional[DeliveryFacility] = field(
            default=None,
            metadata={
                "name": "deliveryFacility",
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
class MailingCenterPostOffice(MailingCenterPostOfficeType):
    """
    Mailing Center/Post Office refers to buildings used as establishments dedicated
    to mail and mailing supplies.
    """

    class Meta:
        name = "mailingCenterPostOffice"
