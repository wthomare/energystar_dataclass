from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from test_fixtures.primer.property_use.characteristic_type import (
    UseAttributeBase,
)


class GrossFloorAreaUnitsType(Enum):
    SQUARE_FEET = "Square Feet"
    SQUARE_METERS = "Square Meters"


@dataclass
class FloorAreaTypeBase(UseAttributeBase):
    """
    :ivar units: The units of the Gross Floor Area (Square Foot or
        Square Meter).
    """

    class Meta:
        name = "floorAreaTypeBase"

    units: Optional[GrossFloorAreaUnitsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class GrossFloorAreaType(FloorAreaTypeBase):
    """
    The total gross floor area of all buildings at the property, measured at the
    exterior boundary of the enclosing walls, including all areas within the
    building (common, tenant, maintenance, etc).
    """

    class Meta:
        name = "grossFloorAreaType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class OptionalFloorAreaType(FloorAreaTypeBase):
    class Meta:
        name = "optionalFloorAreaType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
