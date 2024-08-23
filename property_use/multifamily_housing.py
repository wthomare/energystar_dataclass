from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    CommonEntrance,
    GovernmentSubsidizedHousing,
    NumberOfBedrooms,
    NumberOfLaundryHookupsInAllUnits,
    NumberOfLaundryHookupsInCommonArea,
    NumberOfResidentialLivingUnits,
    NumberOfResidentialLivingUnitsHighRiseSetting,
    NumberOfResidentialLivingUnitsLowRiseSetting,
    NumberOfResidentialLivingUnitsMidRiseSetting,
    PercentCooled,
    PercentHeated,
    ResidentPopulation,
    TotalGrossFloorArea,
)


@dataclass
class MultifamilyHousingType:
    class Meta:
        name = "multifamilyHousingType"

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
    use_details: Optional["MultifamilyHousingType.UseDetails"] = field(
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
        number_of_residential_living_units: Optional[
            NumberOfResidentialLivingUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfResidentialLivingUnits",
                "type": "Element",
            },
        )
        number_of_bedrooms: Optional[NumberOfBedrooms] = field(
            default=None,
            metadata={
                "name": "numberOfBedrooms",
                "type": "Element",
            },
        )
        number_of_residential_living_units_mid_rise_setting: Optional[
            NumberOfResidentialLivingUnitsMidRiseSetting
        ] = field(
            default=None,
            metadata={
                "name": "numberOfResidentialLivingUnitsMidRiseSetting",
                "type": "Element",
            },
        )
        number_of_laundry_hookups_in_all_units: Optional[
            NumberOfLaundryHookupsInAllUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfLaundryHookupsInAllUnits",
                "type": "Element",
            },
        )
        number_of_laundry_hookups_in_common_area: Optional[
            NumberOfLaundryHookupsInCommonArea
        ] = field(
            default=None,
            metadata={
                "name": "numberOfLaundryHookupsInCommonArea",
                "type": "Element",
            },
        )
        number_of_residential_living_units_low_rise_setting: Optional[
            NumberOfResidentialLivingUnitsLowRiseSetting
        ] = field(
            default=None,
            metadata={
                "name": "numberOfResidentialLivingUnitsLowRiseSetting",
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
        percent_cooled: Optional[PercentCooled] = field(
            default=None,
            metadata={
                "name": "percentCooled",
                "type": "Element",
            },
        )
        number_of_residential_living_units_high_rise_setting: Optional[
            NumberOfResidentialLivingUnitsHighRiseSetting
        ] = field(
            default=None,
            metadata={
                "name": "numberOfResidentialLivingUnitsHighRiseSetting",
                "type": "Element",
            },
        )
        resident_population: Optional[ResidentPopulation] = field(
            default=None,
            metadata={
                "name": "residentPopulation",
                "type": "Element",
            },
        )
        government_subsidized_housing: Optional[
            GovernmentSubsidizedHousing
        ] = field(
            default=None,
            metadata={
                "name": "governmentSubsidizedHousing",
                "type": "Element",
            },
        )
        common_entrance: Optional[CommonEntrance] = field(
            default=None,
            metadata={
                "name": "commonEntrance",
                "type": "Element",
            },
        )


@dataclass
class MultifamilyHousing(MultifamilyHousingType):
    """
    Residential Buildings that contain more than two residential living units.
    """

    class Meta:
        name = "multifamilyHousing"
