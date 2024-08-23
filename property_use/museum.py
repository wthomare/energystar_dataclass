from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    GrossFloorAreaThatIsExhibitSpace,
    NumberOfComputers,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    PrecisionControlsForTemperatureAndHumidity,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class MuseumType:
    class Meta:
        name = "museumType"

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
    use_details: Optional["MuseumType.UseDetails"] = field(
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
        number_of_workers: Optional[NumberOfWorkers] = field(
            default=None,
            metadata={
                "name": "numberOfWorkers",
                "type": "Element",
            },
        )
        precision_controls_for_temperature_and_humidity: Optional[
            PrecisionControlsForTemperatureAndHumidity
        ] = field(
            default=None,
            metadata={
                "name": "precisionControlsForTemperatureAndHumidity",
                "type": "Element",
            },
        )
        gross_floor_area_that_is_exhibit_space: Optional[
            GrossFloorAreaThatIsExhibitSpace
        ] = field(
            default=None,
            metadata={
                "name": "grossFloorAreaThatIsExhibitSpace",
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
        number_of_computers: Optional[NumberOfComputers] = field(
            default=None,
            metadata={
                "name": "numberOfComputers",
                "type": "Element",
            },
        )
        weekly_operating_hours: Optional[WeeklyOperatingHours] = field(
            default=None,
            metadata={
                "name": "weeklyOperatingHours",
                "type": "Element",
            },
        )


@dataclass
class Museum(MuseumType):
    """Museum refers to buildings that display collections to outside visitors for
    public viewing and enjoyment and for informational/educational purposes.

    <br xmlns=""/> <br xmlns=""/> Gross Floor Area should include all
    space within the building(s), including but not limited to public
    collection display areas, meeting rooms, restrooms, classrooms, gift
    shops, food service areas, administrative/office space, mechanical
    rooms, storage areas for collections, libraries, elevator shafts,
    stairwells, and movie theatre space inside the museum. Areas not in
    enclosed building such as outdoor exhibit, open-air theaters,
    walkways, and landscaped areas should not be included in the Gross
    Floor Area.
    """

    class Meta:
        name = "museum"
