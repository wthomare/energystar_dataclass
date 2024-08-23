from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    NumberOfBedrooms,
    NumberOfPeople,
    TotalGrossFloorArea,
)


@dataclass
class SingleFamilyHomeType:
    class Meta:
        name = "singleFamilyHomeType"

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
    use_details: Optional["SingleFamilyHomeType.UseDetails"] = field(
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
        number_of_bedrooms: Optional[NumberOfBedrooms] = field(
            default=None,
            metadata={
                "name": "numberOfBedrooms",
                "type": "Element",
            },
        )
        number_of_people: Optional[NumberOfPeople] = field(
            default=None,
            metadata={
                "name": "numberOfPeople",
                "type": "Element",
            },
        )


@dataclass
class SingleFamilyHome(SingleFamilyHomeType):
    """
    A standalone building with its own lot that provides living space for one
    household or family.
    """

    class Meta:
        name = "singleFamilyHome"
