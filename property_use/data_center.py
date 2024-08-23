from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    CoolingEquipmentRedundancy,
    EstimatesApplied,
    ItEnergyMeterConfiguration,
    TotalGrossFloorArea,
    UpsSystemRedundancy,
)


@dataclass
class DataCenterType:
    class Meta:
        name = "dataCenterType"

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
    use_details: Optional["DataCenterType.UseDetails"] = field(
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
        estimates_applied: Optional[EstimatesApplied] = field(
            default=None,
            metadata={
                "name": "estimatesApplied",
                "type": "Element",
            },
        )
        cooling_equipment_redundancy: Optional[CoolingEquipmentRedundancy] = (
            field(
                default=None,
                metadata={
                    "name": "coolingEquipmentRedundancy",
                    "type": "Element",
                },
            )
        )
        it_energy_meter_configuration: Optional[ItEnergyMeterConfiguration] = (
            field(
                default=None,
                metadata={
                    "name": "itEnergyMeterConfiguration",
                    "type": "Element",
                },
            )
        )
        ups_system_redundancy: Optional[UpsSystemRedundancy] = field(
            default=None,
            metadata={
                "name": "upsSystemRedundancy",
                "type": "Element",
            },
        )


@dataclass
class DataCenter(DataCenterType):
    """
    Buildings specifically designed and equipped to meet the needs of high density
    computing equipment, such as server racks, used for data storage and
    processing.
    """

    class Meta:
        name = "dataCenter"
