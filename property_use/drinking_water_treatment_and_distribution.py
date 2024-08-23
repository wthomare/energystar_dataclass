from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    TotalGrossFloorArea,
)


@dataclass
class DrinkingWaterTreatmentAndDistributionType:
    class Meta:
        name = "drinkingWaterTreatmentAndDistributionType"

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
    use_details: Optional[
        "DrinkingWaterTreatmentAndDistributionType.UseDetails"
    ] = field(
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


@dataclass
class DrinkingWaterTreatmentAndDistribution(
    DrinkingWaterTreatmentAndDistributionType
):
    """
    Facilities designed to pump and distribute drinking water through a network of
    pipes.
    """

    class Meta:
        name = "drinkingWaterTreatmentAndDistribution"
