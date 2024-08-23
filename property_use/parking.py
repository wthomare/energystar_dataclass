from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    CompletelyEnclosedFootage,
    OpenFootage,
    PartiallyEnclosedFootage,
    SupplementalHeating,
)


@dataclass
class ParkingType:
    class Meta:
        name = "parkingType"

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
    use_details: Optional["ParkingType.UseDetails"] = field(
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
        supplemental_heating: Optional[SupplementalHeating] = field(
            default=None,
            metadata={
                "name": "supplementalHeating",
                "type": "Element",
            },
        )
        open_footage: Optional[OpenFootage] = field(
            default=None,
            metadata={
                "name": "openFootage",
                "type": "Element",
                "required": True,
            },
        )
        completely_enclosed_footage: Optional[CompletelyEnclosedFootage] = (
            field(
                default=None,
                metadata={
                    "name": "completelyEnclosedFootage",
                    "type": "Element",
                    "required": True,
                },
            )
        )
        partially_enclosed_footage: Optional[PartiallyEnclosedFootage] = field(
            default=None,
            metadata={
                "name": "partiallyEnclosedFootage",
                "type": "Element",
                "required": True,
            },
        )


@dataclass
class Parking(ParkingType):
    """
    Buildings and lots used for parking vehicles.
    """

    class Meta:
        name = "parking"
