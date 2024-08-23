from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    AmountOfLaundryProcessedAnnually,
    CookingFacilities,
    FullServiceSpaFloorArea,
    GrossFloorAreaHotelConferenceSpace,
    GrossFloorAreaUsedForFoodPreparation,
    GymCenterFloorArea,
    HoursPerDayGuestsOnsite,
    LaundryFacility,
    NumberOfCommercialRefrigerationUnits,
    NumberOfGuestMealsServedPerYear,
    NumberOfHotelRooms,
    NumberOfWorkers,
    PercentCooled,
    PercentHeated,
    TotalGrossFloorArea,
)


@dataclass
class HotelType:
    """This xml type represents a property use type.

    If an element is missing it will be populated with a default value.
    """

    class Meta:
        name = "hotelType"

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
    use_details: Optional["HotelType.UseDetails"] = field(
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
        full_service_spa_floor_area: Optional[FullServiceSpaFloorArea] = field(
            default=None,
            metadata={
                "name": "fullServiceSpaFloorArea",
                "type": "Element",
            },
        )
        gym_center_floor_area: Optional[GymCenterFloorArea] = field(
            default=None,
            metadata={
                "name": "gymCenterFloorArea",
                "type": "Element",
            },
        )
        hours_per_day_guests_onsite: Optional[HoursPerDayGuestsOnsite] = field(
            default=None,
            metadata={
                "name": "hoursPerDayGuestsOnsite",
                "type": "Element",
            },
        )
        number_of_commercial_refrigeration_units: Optional[
            NumberOfCommercialRefrigerationUnits
        ] = field(
            default=None,
            metadata={
                "name": "numberOfCommercialRefrigerationUnits",
                "type": "Element",
            },
        )
        number_of_guest_meals_served_per_year: Optional[
            NumberOfGuestMealsServedPerYear
        ] = field(
            default=None,
            metadata={
                "name": "numberOfGuestMealsServedPerYear",
                "type": "Element",
            },
        )
        number_of_hotel_rooms: Optional[NumberOfHotelRooms] = field(
            default=None,
            metadata={
                "name": "numberOfHotelRooms",
                "type": "Element",
            },
        )
        laundry_facility: Optional[LaundryFacility] = field(
            default=None,
            metadata={
                "name": "laundryFacility",
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
        cooking_facilities: Optional[CookingFacilities] = field(
            default=None,
            metadata={
                "name": "cookingFacilities",
                "type": "Element",
            },
        )
        amount_of_laundry_processed_annually: Optional[
            AmountOfLaundryProcessedAnnually
        ] = field(
            default=None,
            metadata={
                "name": "amountOfLaundryProcessedAnnually",
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
        gross_floor_area_used_for_food_preparation: Optional[
            GrossFloorAreaUsedForFoodPreparation
        ] = field(
            default=None,
            metadata={
                "name": "grossFloorAreaUsedForFoodPreparation",
                "type": "Element",
            },
        )
        gross_floor_area_hotel_conference_space: Optional[
            GrossFloorAreaHotelConferenceSpace
        ] = field(
            default=None,
            metadata={
                "name": "grossFloorAreaHotelConferenceSpace",
                "type": "Element",
            },
        )


@dataclass
class Hotel(HotelType):
    """
    Buildings that sell overnight accommodations on a room/suite and nightly basis,
    and typically include a bath/shower and other facilities in guest rooms.
    """

    class Meta:
        name = "hotel"
