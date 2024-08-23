from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    AverageEffluentBiologicalOxygenDemand,
    AverageInfluentBiologicalOxygenDemand,
    FixedFilmTrickleFiltrationProcess,
    NutrientRemoval,
    PlantDesignFlowRate,
    TotalGrossFloorArea,
)


@dataclass
class WastewaterTreatmentPlantType:
    class Meta:
        name = "wastewaterTreatmentPlantType"

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
    use_details: Optional["WastewaterTreatmentPlantType.UseDetails"] = field(
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
        average_influent_biological_oxygen_demand: Optional[
            AverageInfluentBiologicalOxygenDemand
        ] = field(
            default=None,
            metadata={
                "name": "averageInfluentBiologicalOxygenDemand",
                "type": "Element",
            },
        )
        average_effluent_biological_oxygen_demand: Optional[
            AverageEffluentBiologicalOxygenDemand
        ] = field(
            default=None,
            metadata={
                "name": "averageEffluentBiologicalOxygenDemand",
                "type": "Element",
            },
        )
        plant_design_flow_rate: Optional[PlantDesignFlowRate] = field(
            default=None,
            metadata={
                "name": "plantDesignFlowRate",
                "type": "Element",
                "required": True,
            },
        )
        fixed_film_trickle_filtration_process: Optional[
            FixedFilmTrickleFiltrationProcess
        ] = field(
            default=None,
            metadata={
                "name": "fixedFilmTrickleFiltrationProcess",
                "type": "Element",
            },
        )
        nutrient_removal: Optional[NutrientRemoval] = field(
            default=None,
            metadata={
                "name": "nutrientRemoval",
                "type": "Element",
            },
        )


@dataclass
class WastewaterTreatmentPlant(WastewaterTreatmentPlantType):
    """
    Facilities designed to treat municipal wastewater.
    """

    class Meta:
        name = "wastewaterTreatmentPlant"
