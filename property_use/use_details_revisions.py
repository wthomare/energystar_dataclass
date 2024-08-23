from dataclasses import dataclass, field
from typing import List, Optional

from test_fixtures.primer.common.links import LinksType
from test_fixtures.primer.property_use.characteristics import (
    AmountOfLaundryProcessedAnnually,
    AreaOfAllWalkInRefrigerationUnits,
    AverageEffluentBiologicalOxygenDemand,
    AverageInfluentBiologicalOxygenDemand,
    AverageNumberOfResidents,
    AverageNumberOfVehiclesInInventory,
    CeilingHeight,
    ClearHeight,
    CommonEntrance,
    CompletelyEnclosedFootage,
    CookingFacilities,
    CoolingEquipmentRedundancy,
    CustomUseDetail1,
    CustomUseDetail2,
    DeliveryFacility,
    EnclosedFloorArea,
    Enrollment,
    EstimatesApplied,
    ExteriorEntranceToThePublic,
    FixedFilmTrickleFiltrationProcess,
    FullServiceSpaFloorArea,
    GovernmentSubsidizedHousing,
    GrantDollars,
    GrossFloorAreaHotelConferenceSpace,
    GrossFloorAreaThatIsExhibitSpace,
    GrossFloorAreaUsedForFoodPreparation,
    GymCenterFloorArea,
    GymnasiumFloorArea,
    HasComputerLab,
    HasDiningHall,
    HasLaboratory,
    HoursPerDayGuestsOnsite,
    IceEvents,
    IsHighSchool,
    IsTertiaryCare,
    ItEnergyMeterConfiguration,
    LaundryFacility,
    LengthOfAllOpenClosedRefrigerationUnits,
    LicensedBedCapacity,
    MaximumNumberOfFloors,
    MaximumResidentCapacity,
    MonthsInUse,
    MonthsMainIndoorIceRinkInUse,
    NumberOfBedrooms,
    NumberOfCashRegisters,
    NumberOfCommercialRefrigerationUnits,
    NumberOfCommercialWashingMachines,
    NumberOfComputers,
    NumberOfConcertShowEventsPerYear,
    NumberOfCookingEquipmentUnits,
    NumberOfCurlingSheets,
    NumberOfFteworkers,
    NumberOfGuestMealsServedPerYear,
    NumberOfHotelRooms,
    NumberOfIndoorIceRinks,
    NumberOfLaundryHookupsInAllUnits,
    NumberOfLaundryHookupsInCommonArea,
    NumberOfLettersPackagesPerYear,
    NumberOfMriMachines,
    NumberOfOpenClosedRefrigerationUnits,
    NumberOfPeople,
    NumberOfResidentialLiftSystems,
    NumberOfResidentialLivingUnits,
    NumberOfResidentialLivingUnitsHighRiseSetting,
    NumberOfResidentialLivingUnitsLowRiseSetting,
    NumberOfResidentialLivingUnitsMidRiseSetting,
    NumberOfResidentialWashingMachines,
    NumberOfRooms,
    NumberOfSpecialOtherEventsPerYear,
    NumberOfSportingEventsPerYear,
    NumberOfStaffedBeds,
    NumberOfSterilizationUnits,
    NumberOfSurgicalOperatingBeds,
    NumberOfWalkInRefrigerationUnits,
    NumberOfWarmingHeatingEquipmentUnits,
    NumberOfWeekdaysOpen,
    NumberOfWeeklyIceResurfacingForAllRinks,
    NumberOfWorkers,
    NutrientRemoval,
    OnSiteLaundryFacility,
    OpenFootage,
    OpenOnWeekends,
    OwnedBy,
    PartiallyEnclosedFootage,
    PercentCooled,
    PercentHeated,
    PercentOfficeCooled,
    PercentOfficeHeated,
    PercentOfGrossFloorAreaThatIsCommonSpaceOnly,
    PercentUsedForColdStorage,
    PlantDesignFlowRate,
    PoolLocation,
    PoolSize,
    PrecisionControlsForTemperatureAndHumidity,
    ResidentPopulation,
    SchoolDistrict,
    SeatingCapacity,
    SingleStore,
    SizeOfElectronicScoreBoards,
    SpectatorSeatingCapacity,
    StudentSeatingCapacity,
    SupplementalHeating,
    SurgeryCenterFloorArea,
    TotalGrossFloorArea,
    TotalIceRinkSurfaceAreaForAllRinks,
    UpsSystemRedundancy,
    WeeklyOperatingHours,
)


@dataclass
class UseDetails:
    class Meta:
        name = "useDetails"

    amount_of_laundry_processed_annually: List[
        AmountOfLaundryProcessedAnnually
    ] = field(
        default_factory=list,
        metadata={
            "name": "amountOfLaundryProcessedAnnually",
            "type": "Element",
        },
    )
    average_effluent_biological_oxygen_demand: List[
        AverageEffluentBiologicalOxygenDemand
    ] = field(
        default_factory=list,
        metadata={
            "name": "averageEffluentBiologicalOxygenDemand",
            "type": "Element",
        },
    )
    average_influent_biological_oxygen_demand: List[
        AverageInfluentBiologicalOxygenDemand
    ] = field(
        default_factory=list,
        metadata={
            "name": "averageInfluentBiologicalOxygenDemand",
            "type": "Element",
        },
    )
    average_number_of_residents: List[AverageNumberOfResidents] = field(
        default_factory=list,
        metadata={
            "name": "averageNumberOfResidents",
            "type": "Element",
        },
    )
    completely_enclosed_footage: List[CompletelyEnclosedFootage] = field(
        default_factory=list,
        metadata={
            "name": "completelyEnclosedFootage",
            "type": "Element",
        },
    )
    cooking_facilities: List[CookingFacilities] = field(
        default_factory=list,
        metadata={
            "name": "cookingFacilities",
            "type": "Element",
        },
    )
    cooling_equipment_redundancy: List[CoolingEquipmentRedundancy] = field(
        default_factory=list,
        metadata={
            "name": "coolingEquipmentRedundancy",
            "type": "Element",
        },
    )
    enclosed_floor_area: List[EnclosedFloorArea] = field(
        default_factory=list,
        metadata={
            "name": "enclosedFloorArea",
            "type": "Element",
        },
    )
    enrollment: List[Enrollment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exterior_entrance_to_the_public: List[ExteriorEntranceToThePublic] = field(
        default_factory=list,
        metadata={
            "name": "exteriorEntranceToThePublic",
            "type": "Element",
        },
    )
    fixed_film_trickle_filtration_process: List[
        FixedFilmTrickleFiltrationProcess
    ] = field(
        default_factory=list,
        metadata={
            "name": "fixedFilmTrickleFiltrationProcess",
            "type": "Element",
        },
    )
    full_service_spa_floor_area: List[FullServiceSpaFloorArea] = field(
        default_factory=list,
        metadata={
            "name": "fullServiceSpaFloorArea",
            "type": "Element",
        },
    )
    area_of_all_walk_in_refrigeration_units: List[
        AreaOfAllWalkInRefrigerationUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "areaOfAllWalkInRefrigerationUnits",
            "type": "Element",
        },
    )
    length_of_all_open_closed_refrigeration_units: List[
        LengthOfAllOpenClosedRefrigerationUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "lengthOfAllOpenClosedRefrigerationUnits",
            "type": "Element",
        },
    )
    government_subsidized_housing: List[GovernmentSubsidizedHousing] = field(
        default_factory=list,
        metadata={
            "name": "governmentSubsidizedHousing",
            "type": "Element",
        },
    )
    grant_dollars: List[GrantDollars] = field(
        default_factory=list,
        metadata={
            "name": "grantDollars",
            "type": "Element",
        },
    )
    gym_center_floor_area: List[GymCenterFloorArea] = field(
        default_factory=list,
        metadata={
            "name": "gymCenterFloorArea",
            "type": "Element",
        },
    )
    gymnasium_floor_area: List[GymnasiumFloorArea] = field(
        default_factory=list,
        metadata={
            "name": "gymnasiumFloorArea",
            "type": "Element",
        },
    )
    has_computer_lab: List[HasComputerLab] = field(
        default_factory=list,
        metadata={
            "name": "hasComputerLab",
            "type": "Element",
        },
    )
    has_dining_hall: List[HasDiningHall] = field(
        default_factory=list,
        metadata={
            "name": "hasDiningHall",
            "type": "Element",
        },
    )
    has_laboratory: List[HasLaboratory] = field(
        default_factory=list,
        metadata={
            "name": "hasLaboratory",
            "type": "Element",
        },
    )
    hours_per_day_guests_onsite: List[HoursPerDayGuestsOnsite] = field(
        default_factory=list,
        metadata={
            "name": "hoursPerDayGuestsOnsite",
            "type": "Element",
        },
    )
    ice_events: List[IceEvents] = field(
        default_factory=list,
        metadata={
            "name": "iceEvents",
            "type": "Element",
        },
    )
    is_high_school: List[IsHighSchool] = field(
        default_factory=list,
        metadata={
            "name": "isHighSchool",
            "type": "Element",
        },
    )
    is_tertiary_care: List[IsTertiaryCare] = field(
        default_factory=list,
        metadata={
            "name": "isTertiaryCare",
            "type": "Element",
        },
    )
    it_energy_meter_configuration: List[ItEnergyMeterConfiguration] = field(
        default_factory=list,
        metadata={
            "name": "itEnergyMeterConfiguration",
            "type": "Element",
        },
    )
    laundry_facility: List[LaundryFacility] = field(
        default_factory=list,
        metadata={
            "name": "laundryFacility",
            "type": "Element",
        },
    )
    maximum_number_of_floors: List[MaximumNumberOfFloors] = field(
        default_factory=list,
        metadata={
            "name": "maximumNumberOfFloors",
            "type": "Element",
        },
    )
    maximum_resident_capacity: List[MaximumResidentCapacity] = field(
        default_factory=list,
        metadata={
            "name": "maximumResidentCapacity",
            "type": "Element",
        },
    )
    licensed_bed_capacity: List[LicensedBedCapacity] = field(
        default_factory=list,
        metadata={
            "name": "licensedBedCapacity",
            "type": "Element",
        },
    )
    months_in_use: List[MonthsInUse] = field(
        default_factory=list,
        metadata={
            "name": "monthsInUse",
            "type": "Element",
        },
    )
    months_main_indoor_ice_rink_in_use: List[MonthsMainIndoorIceRinkInUse] = (
        field(
            default_factory=list,
            metadata={
                "name": "monthsMainIndoorIceRinkInUse",
                "type": "Element",
            },
        )
    )
    number_of_bedrooms: List[NumberOfBedrooms] = field(
        default_factory=list,
        metadata={
            "name": "numberOfBedrooms",
            "type": "Element",
        },
    )
    number_of_cash_registers: List[NumberOfCashRegisters] = field(
        default_factory=list,
        metadata={
            "name": "numberOfCashRegisters",
            "type": "Element",
        },
    )
    number_of_commercial_refrigeration_units: List[
        NumberOfCommercialRefrigerationUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfCommercialRefrigerationUnits",
            "type": "Element",
        },
    )
    number_of_commercial_washing_machines: List[
        NumberOfCommercialWashingMachines
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfCommercialWashingMachines",
            "type": "Element",
        },
    )
    number_of_computers: List[NumberOfComputers] = field(
        default_factory=list,
        metadata={
            "name": "numberOfComputers",
            "type": "Element",
        },
    )
    number_of_concert_show_events_per_year: List[
        NumberOfConcertShowEventsPerYear
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfConcertShowEventsPerYear",
            "type": "Element",
        },
    )
    number_of_residential_living_units_low_rise_setting: List[
        NumberOfResidentialLivingUnitsLowRiseSetting
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfResidentialLivingUnitsLowRiseSetting",
            "type": "Element",
        },
    )
    number_of_fteworkers: List[NumberOfFteworkers] = field(
        default_factory=list,
        metadata={
            "name": "numberOfFTEWorkers",
            "type": "Element",
        },
    )
    number_of_guest_meals_served_per_year: List[
        NumberOfGuestMealsServedPerYear
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfGuestMealsServedPerYear",
            "type": "Element",
        },
    )
    number_of_laundry_hookups_in_all_units: List[
        NumberOfLaundryHookupsInAllUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfLaundryHookupsInAllUnits",
            "type": "Element",
        },
    )
    number_of_laundry_hookups_in_common_area: List[
        NumberOfLaundryHookupsInCommonArea
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfLaundryHookupsInCommonArea",
            "type": "Element",
        },
    )
    number_of_mri_machines: List[NumberOfMriMachines] = field(
        default_factory=list,
        metadata={
            "name": "numberOfMriMachines",
            "type": "Element",
        },
    )
    number_of_open_closed_refrigeration_units: List[
        NumberOfOpenClosedRefrigerationUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfOpenClosedRefrigerationUnits",
            "type": "Element",
        },
    )
    number_of_people: List[NumberOfPeople] = field(
        default_factory=list,
        metadata={
            "name": "numberOfPeople",
            "type": "Element",
        },
    )
    number_of_residential_lift_systems: List[
        NumberOfResidentialLiftSystems
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfResidentialLiftSystems",
            "type": "Element",
        },
    )
    number_of_residential_living_units: List[
        NumberOfResidentialLivingUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfResidentialLivingUnits",
            "type": "Element",
        },
    )
    number_of_residential_washing_machines: List[
        NumberOfResidentialWashingMachines
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfResidentialWashingMachines",
            "type": "Element",
        },
    )
    number_of_rooms: List[NumberOfRooms] = field(
        default_factory=list,
        metadata={
            "name": "numberOfRooms",
            "type": "Element",
        },
    )
    number_of_hotel_rooms: List[NumberOfHotelRooms] = field(
        default_factory=list,
        metadata={
            "name": "numberOfHotelRooms",
            "type": "Element",
        },
    )
    number_of_special_other_events_per_year: List[
        NumberOfSpecialOtherEventsPerYear
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfSpecialOtherEventsPerYear",
            "type": "Element",
        },
    )
    number_of_sporting_events_per_year: List[NumberOfSportingEventsPerYear] = (
        field(
            default_factory=list,
            metadata={
                "name": "numberOfSportingEventsPerYear",
                "type": "Element",
            },
        )
    )
    number_of_staffed_beds: List[NumberOfStaffedBeds] = field(
        default_factory=list,
        metadata={
            "name": "numberOfStaffedBeds",
            "type": "Element",
        },
    )
    number_of_surgical_operating_beds: List[NumberOfSurgicalOperatingBeds] = (
        field(
            default_factory=list,
            metadata={
                "name": "numberOfSurgicalOperatingBeds",
                "type": "Element",
            },
        )
    )
    number_of_walk_in_refrigeration_units: List[
        NumberOfWalkInRefrigerationUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfWalkInRefrigerationUnits",
            "type": "Element",
        },
    )
    number_of_weekdays_open: List[NumberOfWeekdaysOpen] = field(
        default_factory=list,
        metadata={
            "name": "numberOfWeekdaysOpen",
            "type": "Element",
        },
    )
    number_of_workers: List[NumberOfWorkers] = field(
        default_factory=list,
        metadata={
            "name": "numberOfWorkers",
            "type": "Element",
        },
    )
    number_of_indoor_ice_rinks: List[NumberOfIndoorIceRinks] = field(
        default_factory=list,
        metadata={
            "name": "numberOfIndoorIceRinks",
            "type": "Element",
        },
    )
    number_of_weekly_ice_resurfacing_for_all_rinks: List[
        NumberOfWeeklyIceResurfacingForAllRinks
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfWeeklyIceResurfacingForAllRinks",
            "type": "Element",
        },
    )
    number_of_curling_sheets: List[NumberOfCurlingSheets] = field(
        default_factory=list,
        metadata={
            "name": "numberOfCurlingSheets",
            "type": "Element",
        },
    )
    nutrient_removal: List[NutrientRemoval] = field(
        default_factory=list,
        metadata={
            "name": "nutrientRemoval",
            "type": "Element",
        },
    )
    on_site_laundry_facility: List[OnSiteLaundryFacility] = field(
        default_factory=list,
        metadata={
            "name": "onSiteLaundryFacility",
            "type": "Element",
        },
    )
    open_footage: List[OpenFootage] = field(
        default_factory=list,
        metadata={
            "name": "openFootage",
            "type": "Element",
        },
    )
    open_on_weekends: List[OpenOnWeekends] = field(
        default_factory=list,
        metadata={
            "name": "openOnWeekends",
            "type": "Element",
        },
    )
    owned_by: List[OwnedBy] = field(
        default_factory=list,
        metadata={
            "name": "ownedBy",
            "type": "Element",
        },
    )
    partially_enclosed_footage: List[PartiallyEnclosedFootage] = field(
        default_factory=list,
        metadata={
            "name": "partiallyEnclosedFootage",
            "type": "Element",
        },
    )
    percent_cooled: List[PercentCooled] = field(
        default_factory=list,
        metadata={
            "name": "percentCooled",
            "type": "Element",
        },
    )
    percent_heated: List[PercentHeated] = field(
        default_factory=list,
        metadata={
            "name": "percentHeated",
            "type": "Element",
        },
    )
    number_of_residential_living_units_mid_rise_setting: List[
        NumberOfResidentialLivingUnitsMidRiseSetting
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfResidentialLivingUnitsMidRiseSetting",
            "type": "Element",
        },
    )
    percent_of_gross_floor_area_that_is_common_space_only: List[
        PercentOfGrossFloorAreaThatIsCommonSpaceOnly
    ] = field(
        default_factory=list,
        metadata={
            "name": "percentOfGrossFloorAreaThatIsCommonSpaceOnly",
            "type": "Element",
        },
    )
    percent_office_cooled: List[PercentOfficeCooled] = field(
        default_factory=list,
        metadata={
            "name": "percentOfficeCooled",
            "type": "Element",
        },
    )
    percent_office_heated: List[PercentOfficeHeated] = field(
        default_factory=list,
        metadata={
            "name": "percentOfficeHeated",
            "type": "Element",
        },
    )
    total_ice_rink_surface_area_for_all_rinks: List[
        TotalIceRinkSurfaceAreaForAllRinks
    ] = field(
        default_factory=list,
        metadata={
            "name": "totalIceRinkSurfaceAreaForAllRinks",
            "type": "Element",
        },
    )
    plant_design_flow_rate: List[PlantDesignFlowRate] = field(
        default_factory=list,
        metadata={
            "name": "plantDesignFlowRate",
            "type": "Element",
        },
    )
    pool_location: List[PoolLocation] = field(
        default_factory=list,
        metadata={
            "name": "poolLocation",
            "type": "Element",
        },
    )
    pool_size: List[PoolSize] = field(
        default_factory=list,
        metadata={
            "name": "poolSize",
            "type": "Element",
        },
    )
    number_of_residential_living_units_high_rise_setting: List[
        NumberOfResidentialLivingUnitsHighRiseSetting
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfResidentialLivingUnitsHighRiseSetting",
            "type": "Element",
        },
    )
    resident_population: List[ResidentPopulation] = field(
        default_factory=list,
        metadata={
            "name": "residentPopulation",
            "type": "Element",
        },
    )
    school_district: List[SchoolDistrict] = field(
        default_factory=list,
        metadata={
            "name": "schoolDistrict",
            "type": "Element",
        },
    )
    seating_capacity: List[SeatingCapacity] = field(
        default_factory=list,
        metadata={
            "name": "seatingCapacity",
            "type": "Element",
        },
    )
    single_store: List[SingleStore] = field(
        default_factory=list,
        metadata={
            "name": "singleStore",
            "type": "Element",
        },
    )
    total_gross_floor_area: List[TotalGrossFloorArea] = field(
        default_factory=list,
        metadata={
            "name": "totalGrossFloorArea",
            "type": "Element",
        },
    )
    estimates_applied: List[EstimatesApplied] = field(
        default_factory=list,
        metadata={
            "name": "estimatesApplied",
            "type": "Element",
        },
    )
    ups_system_redundancy: List[UpsSystemRedundancy] = field(
        default_factory=list,
        metadata={
            "name": "upsSystemRedundancy",
            "type": "Element",
        },
    )
    size_of_electronic_score_boards: List[SizeOfElectronicScoreBoards] = field(
        default_factory=list,
        metadata={
            "name": "sizeOfElectronicScoreBoards",
            "type": "Element",
        },
    )
    spectator_seating_capacity: List[SpectatorSeatingCapacity] = field(
        default_factory=list,
        metadata={
            "name": "spectatorSeatingCapacity",
            "type": "Element",
        },
    )
    supplemental_heating: List[SupplementalHeating] = field(
        default_factory=list,
        metadata={
            "name": "supplementalHeating",
            "type": "Element",
        },
    )
    student_seating_capacity: List[StudentSeatingCapacity] = field(
        default_factory=list,
        metadata={
            "name": "studentSeatingCapacity",
            "type": "Element",
        },
    )
    surgery_center_floor_area: List[SurgeryCenterFloorArea] = field(
        default_factory=list,
        metadata={
            "name": "surgeryCenterFloorArea",
            "type": "Element",
        },
    )
    weekly_operating_hours: List[WeeklyOperatingHours] = field(
        default_factory=list,
        metadata={
            "name": "weeklyOperatingHours",
            "type": "Element",
        },
    )
    percent_used_for_cold_storage: List[PercentUsedForColdStorage] = field(
        default_factory=list,
        metadata={
            "name": "percentUsedForColdStorage",
            "type": "Element",
        },
    )
    gross_floor_area_used_for_food_preparation: List[
        GrossFloorAreaUsedForFoodPreparation
    ] = field(
        default_factory=list,
        metadata={
            "name": "grossFloorAreaUsedForFoodPreparation",
            "type": "Element",
        },
    )
    gross_floor_area_hotel_conference_space: List[
        GrossFloorAreaHotelConferenceSpace
    ] = field(
        default_factory=list,
        metadata={
            "name": "grossFloorAreaHotelConferenceSpace",
            "type": "Element",
        },
    )
    clear_height: List[ClearHeight] = field(
        default_factory=list,
        metadata={
            "name": "clearHeight",
            "type": "Element",
        },
    )
    number_of_sterilization_units: List[NumberOfSterilizationUnits] = field(
        default_factory=list,
        metadata={
            "name": "numberOfSterilizationUnits",
            "type": "Element",
        },
    )
    common_entrance: List[CommonEntrance] = field(
        default_factory=list,
        metadata={
            "name": "commonEntrance",
            "type": "Element",
        },
    )
    number_of_cooking_equipment_units: List[NumberOfCookingEquipmentUnits] = (
        field(
            default_factory=list,
            metadata={
                "name": "numberOfCookingEquipmentUnits",
                "type": "Element",
            },
        )
    )
    number_of_warming_heating_equipment_units: List[
        NumberOfWarmingHeatingEquipmentUnits
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfWarmingHeatingEquipmentUnits",
            "type": "Element",
        },
    )
    ceiling_height: List[CeilingHeight] = field(
        default_factory=list,
        metadata={
            "name": "ceilingHeight",
            "type": "Element",
        },
    )
    average_number_of_vehicles_in_inventory: List[
        AverageNumberOfVehiclesInInventory
    ] = field(
        default_factory=list,
        metadata={
            "name": "averageNumberOfVehiclesInInventory",
            "type": "Element",
        },
    )
    delivery_facility: List[DeliveryFacility] = field(
        default_factory=list,
        metadata={
            "name": "deliveryFacility",
            "type": "Element",
        },
    )
    number_of_letters_packages_per_year: List[
        NumberOfLettersPackagesPerYear
    ] = field(
        default_factory=list,
        metadata={
            "name": "numberOfLettersPackagesPerYear",
            "type": "Element",
        },
    )
    custom_use_detail1: List[CustomUseDetail1] = field(
        default_factory=list,
        metadata={
            "name": "customUseDetail1",
            "type": "Element",
        },
    )
    custom_use_detail2: List[CustomUseDetail2] = field(
        default_factory=list,
        metadata={
            "name": "customUseDetail2",
            "type": "Element",
        },
    )
    precision_controls_for_temperature_and_humidity: List[
        PrecisionControlsForTemperatureAndHumidity
    ] = field(
        default_factory=list,
        metadata={
            "name": "precisionControlsForTemperatureAndHumidity",
            "type": "Element",
        },
    )
    gross_floor_area_that_is_exhibit_space: List[
        GrossFloorAreaThatIsExhibitSpace
    ] = field(
        default_factory=list,
        metadata={
            "name": "grossFloorAreaThatIsExhibitSpace",
            "type": "Element",
        },
    )
    links: Optional[LinksType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
