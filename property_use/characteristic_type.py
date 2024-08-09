from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDate

from test_fixtures.primer.common.audit import LogType


class PlantDesignFlowRateUnitsType(Enum):
    MILLION_GALLONS_PER_DAY = "Million Gallons per Day"
    CUBIC_METERS_PER_DAY = "Cubic Meters per Day"


class AmountOfLaundryProcessedAnnuallyUnitsType(Enum):
    POUNDS = "pounds"
    KILOGRAM = "Kilogram"
    SHORT_TONS = "short tons"


class CoolingEquipmentRedundancyTypeValue(Enum):
    N = "N"
    N_1 = "N+1"
    N_2 = "N+2"
    VALUE_2_N = "2N"
    GREATER_THAN_2_N = "Greater than 2N"
    NONE_OF_THE_ABOVE = "None of the Above"


class CustomUnitsType(Enum):
    FEET = "Feet"
    GALLONS_US = "Gallons (US)"
    GALLONS_UK = "Gallons (UK)"
    KILOGRAM = "Kilogram"
    METERS = "Meters"
    TONNES_METRIC = "Tonnes (metric)"
    OTHER = "Other"
    POUNDS = "Pounds"
    SQUARE_FEET = "Square Feet"
    SQUARE_METERS = "Square Meters"
    TONS_SHORT = "Tons (short)"


class CustomUseDetailsTypeDataType(Enum):
    NUMERIC = "numeric"
    STRING = "string"


class HoursPerDayGuestsOnsiteTypeValue(Enum):
    LESS_THAN_15 = "Less Than 15"
    VALUE_15_TO_19 = "15 To 19"
    MORE_THAN_20 = "More Than 20"


class ItEnergyConfigurationTypeValue(Enum):
    UPS_SUPPORTS_ONLY_IT_EQUIPMENT = "UPS Supports Only IT Equipment"
    UPS_INCLUDE_NON_IT_LOAD_LESS_THAN_10 = (
        "UPS Include Non IT Load Less Than 10%"
    )
    UPS_INCLUDE_NON_IT_LOAD_GREATER_THAN_10_LOAD_SUBMETERED = (
        "UPS Include Non-IT Load Greater Than 10% Load Submetered"
    )
    UPS_INCLUDE_NON_IT_LOAD_GREATER_THAN_10_LOAD_NOT_SUBMETERED = (
        "UPS Include Non IT Load Greater Than 10% Load Not Submetered"
    )
    FACILITY_HAS_NO_UPS = "Facility Has No UPS"
    NO_IT_ENERGY_CONFIGURATION_SELECTED = "No IT Energy Configuration Selected"


class LengthUnitsType(Enum):
    FEET = "Feet"
    METERS = "Meters"


class OnsiteLaundryTypeValue(Enum):
    LINENS_ONLY = "Linens only"
    TERRY_ONLY = "Terry only"
    BOTH_LINENS_AND_TERRY = "Both linens and terry"
    NO_LAUNDRY_FACILITY = "No laundry facility"


class OwnedByTypeValue(Enum):
    FOR_PROFIT = "For Profit"
    NON_PROFIT = "Non Profit"
    GOVERNMENTAL = "Governmental"


class PercentCooledTypeValue(Enum):
    VALUE_0 = "0"
    VALUE_10 = "10"
    VALUE_20 = "20"
    VALUE_30 = "30"
    VALUE_40 = "40"
    VALUE_50 = "50"
    VALUE_60 = "60"
    VALUE_70 = "70"
    VALUE_80 = "80"
    VALUE_90 = "90"
    VALUE_100 = "100"


class PercentHeatedTypeValue(Enum):
    VALUE_0 = "0"
    VALUE_10 = "10"
    VALUE_20 = "20"
    VALUE_30 = "30"
    VALUE_40 = "40"
    VALUE_50 = "50"
    VALUE_60 = "60"
    VALUE_70 = "70"
    VALUE_80 = "80"
    VALUE_90 = "90"
    VALUE_100 = "100"


class PercentOfficeCooledTypeValue(Enum):
    VALUE_50_OR_MORE = "50% or more"
    LESS_THAN_50 = "Less than 50%"
    NOT_AIR_CONDITIONED = "Not Air Conditioned"


class PercentOfficeHeatedTypeValue(Enum):
    VALUE_50_OR_MORE = "50% or more"
    LESS_THAN_50 = "Less than 50%"
    NOT_HEATED = "Not Heated"


class PoolSizeTypeValue(Enum):
    RECREATIONAL_20_YARDS_X_15_YARDS = "Recreational (20 yards x 15 yards)"
    SHORT_COURSE_25_YARDS_X_20_YARDS = "Short Course (25 yards x 20 yards)"
    OLYMPIC_50_METERS_X_25_METERS = "Olympic (50 meters x 25 meters)"


class PoolTypeValue(Enum):
    INDOOR = "Indoor"
    OUTDOOR = "Outdoor"


class ResidentPopulationTypeValue(Enum):
    NO_SPECIFIC_RESIDENT_POPULATION = "No specific resident population"
    DEDICATED_STUDENT = "Dedicated Student"
    DEDICATED_MILITARY = "Dedicated Military"
    DEDICATED_SENIOR_INDEPENDENT_LIVING = "Dedicated Senior/Independent Living"
    DEDICATED_SPECIAL_ACCESSIBILITY_NEEDS = (
        "Dedicated Special Accessibility Needs"
    )
    OTHER_DEDICATED_HOUSING = "Other dedicated housing"


class UpsSystemRedundancyTypeValue(Enum):
    N = "N"
    N_1 = "N+1"
    N_2 = "N+2"
    VALUE_2_N = "2N"
    GREATER_THAN_2_N = "Greater than 2N"
    NONE_OF_THE_ABOVE = "None of the Above"


class UseAttributeBaseDefault(Enum):
    YES = "Yes"
    NO = "No"
    N_A = "N/A"


class YesNo(Enum):
    YES = "Yes"
    NO = "No"


@dataclass
class UseAttributeBase:
    """
    :ivar audit:
    :ivar id:
    :ivar current_as_of: The date that the characteristic is current as
        of.
    :ivar temporary: The characteristic is a temporary value
        (true/false)
    :ivar default: Indicates whether the value for this characteristic
        was calculated by the system using default values (Yes, No, or
        N/A). If the characteristic is required for benchmarking and the
        value is being defaulted then it is set to Yes otherwise No.  If
        the characteristic is not required for benchmarking then it is
        set to N/A. This attribute only applies to retrieving data.  It
        will be ignored if provided as input. Also note that even though
        gross floor area is required for benchmarking, it is set to No
        since the system never provides a value for that characteristic.
    """

    class Meta:
        name = "useAttributeBase"

    audit: Optional[LogType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    current_as_of: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "currentAsOf",
            "type": "Attribute",
        },
    )
    temporary: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    default: Optional[UseAttributeBaseDefault] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PlantDesignFlowRateType(UseAttributeBase):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    units: Optional[PlantDesignFlowRateUnitsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class AmountOfLaundryProcessedAnnuallyType(UseAttributeBase):
    class Meta:
        name = "amountOfLaundryProcessedAnnuallyType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    units: Optional[AmountOfLaundryProcessedAnnuallyUnitsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CeilingHeightUnitsType(UseAttributeBase):
    class Meta:
        name = "ceilingHeightUnitsType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("1.0"),
        },
    )
    units: Optional[LengthUnitsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ClearHeightUnitsType(UseAttributeBase):
    class Meta:
        name = "clearHeightUnitsType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    units: Optional[LengthUnitsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CoolingEquipmentRedundancyType(UseAttributeBase):
    class Meta:
        name = "coolingEquipmentRedundancyType"

    value: Optional[CoolingEquipmentRedundancyTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class CustomUseDetailsType(UseAttributeBase):
    class Meta:
        name = "customUseDetailsType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    custom_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "customName",
            "type": "Element",
            "namespace": "",
        },
    )
    custom_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "customUom",
            "type": "Element",
            "namespace": "",
        },
    )
    units: Optional[CustomUnitsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    data_type: Optional[CustomUseDetailsTypeDataType] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Attribute",
        },
    )


@dataclass
class HoursPerDayGuestsOnsiteType(UseAttributeBase):
    class Meta:
        name = "hoursPerDayGuestsOnsiteType"

    value: Optional[HoursPerDayGuestsOnsiteTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ItEnergyConfigurationType(UseAttributeBase):
    class Meta:
        name = "itEnergyConfigurationType"

    value: Optional[ItEnergyConfigurationTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class LengthOfAllOpenClosedRefrigerationUnitsType(UseAttributeBase):
    class Meta:
        name = "lengthOfAllOpenClosedRefrigerationUnitsType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    units: Optional[LengthUnitsType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MonthsInUseType(UseAttributeBase):
    class Meta:
        name = "monthsInUseType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1,
            "max_inclusive": 12,
        },
    )


@dataclass
class MonthsSchoolInUseType(UseAttributeBase):
    class Meta:
        name = "monthsSchoolInUseType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 8,
            "max_inclusive": 12,
        },
    )


@dataclass
class NumberOfWeekdaysType(UseAttributeBase):
    class Meta:
        name = "numberOfWeekdaysType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 0,
            "max_inclusive": 5,
        },
    )


@dataclass
class NumberOfWeeklyIceResurfacingType(UseAttributeBase):
    class Meta:
        name = "numberOfWeeklyIceResurfacingType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1,
        },
    )


@dataclass
class OnsiteLaundryType(UseAttributeBase):
    class Meta:
        name = "onsiteLaundryType"

    value: Optional[OnsiteLaundryTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class OwnedByType(UseAttributeBase):
    class Meta:
        name = "ownedByType"

    value: Optional[OwnedByTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PercentCooledType(UseAttributeBase):
    class Meta:
        name = "percentCooledType"

    value: Optional[PercentCooledTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PercentHeatedType(UseAttributeBase):
    class Meta:
        name = "percentHeatedType"

    value: Optional[PercentHeatedTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PercentOfficeCooledType(UseAttributeBase):
    class Meta:
        name = "percentOfficeCooledType"

    value: Optional[PercentOfficeCooledTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PercentOfficeHeatedType(UseAttributeBase):
    class Meta:
        name = "percentOfficeHeatedType"

    value: Optional[PercentOfficeHeatedTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PoolSizeType(UseAttributeBase):
    class Meta:
        name = "poolSizeType"

    value: Optional[PoolSizeTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class PoolType(UseAttributeBase):
    class Meta:
        name = "poolType"

    value: Optional[PoolTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ResidentPopulationType(UseAttributeBase):
    class Meta:
        name = "residentPopulationType"

    value: Optional[ResidentPopulationTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UpsSystemRedundancyType(UseAttributeBase):
    class Meta:
        name = "upsSystemRedundancyType"

    value: Optional[UpsSystemRedundancyTypeValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UseDecimalType(UseAttributeBase):
    class Meta:
        name = "useDecimalType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0"),
        },
    )


@dataclass
class UseIntegerType(UseAttributeBase):
    class Meta:
        name = "useIntegerType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 0,
        },
    )


@dataclass
class UseStringType(UseAttributeBase):
    class Meta:
        name = "useStringType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class UseYesNoType(UseAttributeBase):
    class Meta:
        name = "useYesNoType"

    value: Optional[YesNo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
