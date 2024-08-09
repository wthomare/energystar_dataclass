from dataclasses import dataclass

from test_fixtures.primer.common.gross_floor_area import (
    GrossFloorAreaType,
    OptionalFloorAreaType,
)

from test_fixtures.primer.property_use.characteristic_type import (
    AmountOfLaundryProcessedAnnuallyType,
    CeilingHeightUnitsType,
    ClearHeightUnitsType,
    CoolingEquipmentRedundancyType,
    CustomUseDetailsType,
    HoursPerDayGuestsOnsiteType,
    ItEnergyConfigurationType,
    LengthOfAllOpenClosedRefrigerationUnitsType,
    MonthsInUseType,
    NumberOfWeekdaysType,
    NumberOfWeeklyIceResurfacingType,
    OnsiteLaundryType,
    OwnedByType,
    PercentCooledType,
    PercentHeatedType,
    PercentOfficeCooledType,
    PercentOfficeHeatedType,
    PlantDesignFlowRateType,
    PoolSizeType,
    PoolType,
    ResidentPopulationType,
    UpsSystemRedundancyType,
    UseDecimalType,
    UseIntegerType,
    UseStringType,
    UseYesNoType,
)


@dataclass
class AmountOfLaundryProcessedAnnually(AmountOfLaundryProcessedAnnuallyType):
    """
    Quantity of laundry processed at the property.
    """

    class Meta:
        name = "amountOfLaundryProcessedAnnually"


@dataclass
class AreaOfAllWalkInRefrigerationUnits(OptionalFloorAreaType):
    """Area of all walk-in refrigeration/freezer units - include only commercial type units that a person actually walks into to retrieve goods.  See numberOfWalkInRefrigerationUnits for more information."""

    class Meta:
        name = "areaOfAllWalkInRefrigerationUnits"


@dataclass
class AverageEffluentBiologicalOxygenDemand(UseDecimalType):
    """
    The concentration of effluent Biological Oxygen Demand (BOD5) at a wastewater
    treatment plant.
    """

    class Meta:
        name = "averageEffluentBiologicalOxygenDemand"


@dataclass
class AverageInfluentBiologicalOxygenDemand(UseDecimalType):
    """
    The concentration of influent Biological Oxygen Demand (BOD5) at a wastewater
    treatment plant.
    """

    class Meta:
        name = "averageInfluentBiologicalOxygenDemand"


@dataclass
class AverageNumberOfResidents(UseDecimalType):
    """
    Annual average number of residents at the property.
    """

    class Meta:
        name = "averageNumberOfResidents"


@dataclass
class AverageNumberOfVehiclesInInventory(UseDecimalType):
    """
    The average number of vehicles in inventory, not including vehicles housed at
    off-site locations.
    """

    class Meta:
        name = "averageNumberOfVehiclesInInventory"


@dataclass
class CeilingHeight(CeilingHeightUnitsType):
    """
    The maximum vertical distance measured from floor to ceiling.
    """

    class Meta:
        name = "ceilingHeight"


@dataclass
class ClearHeight(ClearHeightUnitsType):
    """
    The distance measured from the floor to the lowest overhead obstruction for the
    majority of the warehouse space.
    """

    class Meta:
        name = "clearHeight"


@dataclass
class CommonEntrance(UseYesNoType):
    """Indicates presence of common entrance: Yes and No are 2 options and 1 or 0 is used."""

    class Meta:
        name = "commonEntrance"


@dataclass
class CompletelyEnclosedFootage(GrossFloorAreaType):
    """
    Area of parking garage that is completely enclosed.
    """

    class Meta:
        name = "completelyEnclosedFootage"


@dataclass
class CookingFacilities(UseYesNoType):
    """
    Whether there are Cooking Facilities.
    """

    class Meta:
        name = "cookingFacilities"


@dataclass
class CoolingEquipmentRedundancy(CoolingEquipmentRedundancyType):
    """
    Level of redundancy for the cooling equipment in a Data Center.
    """

    class Meta:
        name = "coolingEquipmentRedundancy"


@dataclass
class CustomUseDetail1(CustomUseDetailsType):
    """
    Custom Use Detail #1.
    """

    class Meta:
        name = "customUseDetail1"


@dataclass
class CustomUseDetail2(CustomUseDetailsType):
    """
    Custom Use Detail #2.
    """

    class Meta:
        name = "customUseDetail2"


@dataclass
class DeliveryFacility(UseYesNoType):
    """
    Denotes if a facility delivers mail products directly from the building to
    offsite customers at their residence or place of business.
    """

    class Meta:
        name = "deliveryFacility"


@dataclass
class EnclosedFloorArea(OptionalFloorAreaType):
    """
    Total enclosed floor area at a Stadium/Arena.
    """

    class Meta:
        name = "enclosedFloorArea"


@dataclass
class Enrollment(UseDecimalType):
    class Meta:
        name = "enrollment"


@dataclass
class EstimatesApplied(UseYesNoType):
    """
    Whether Data Center IT energy estimates are applied.
    """

    class Meta:
        name = "estimatesApplied"


@dataclass
class ExteriorEntranceToThePublic(UseYesNoType):
    """
    Whether there is an Exterior Entrance to the Public.
    """

    class Meta:
        name = "exteriorEntranceToThePublic"


@dataclass
class FixedFilmTrickleFiltrationProcess(UseYesNoType):
    """
    Whether there is a Fixed Film Trickle Filtration Process.
    """

    class Meta:
        name = "fixedFilmTrickleFiltrationProcess"


@dataclass
class FullServiceSpaFloorArea(OptionalFloorAreaType):
    """
    Floor area associated with a Full Service Spa.
    """

    class Meta:
        name = "fullServiceSpaFloorArea"


@dataclass
class GovernmentSubsidizedHousing(UseYesNoType):
    """
    Whether this is housing that is subsidized by the local, state, or Federal
    government.
    """

    class Meta:
        name = "governmentSubsidizedHousing"


@dataclass
class GrantDollars(UseDecimalType):
    class Meta:
        name = "grantDollars"


@dataclass
class GrossFloorAreaHotelConferenceSpace(OptionalFloorAreaType):
    """The Gross Floor Area that is Hotel Conference Space is the total size of all
    conference spaces.

    This will be a subset of Gross Floor Area for the property.
    """

    class Meta:
        name = "grossFloorAreaHotelConferenceSpace"


@dataclass
class GrossFloorAreaThatIsExhibitSpace(OptionalFloorAreaType):
    """The Gross Floor Area refers to the total area used for public collection
    display areas.

    It is a subset of the total Gross Floor Area. It should not include
    outdoor public collection display areas.
    """

    class Meta:
        name = "grossFloorAreaThatIsExhibitSpace"


@dataclass
class GrossFloorAreaUsedForFoodPreparation(OptionalFloorAreaType):
    """The Gross Floor Area Used for Food Preparation is the total size of all
    large/commercial kitchen areas used for the storage and preparation of food.

    This will be a subset of Gross Floor Area for the property.
    """

    class Meta:
        name = "grossFloorAreaUsedForFoodPreparation"


@dataclass
class GymCenterFloorArea(OptionalFloorAreaType):
    """
    Floor area associated with a Gym/Fitness Center.
    """

    class Meta:
        name = "gymCenterFloorArea"


@dataclass
class GymnasiumFloorArea(OptionalFloorAreaType):
    """
    Floor area associated with a gymnasium at a K12 School.
    """

    class Meta:
        name = "gymnasiumFloorArea"


@dataclass
class HasComputerLab(UseYesNoType):
    """
    Whether there is a Computer Lab.
    """

    class Meta:
        name = "hasComputerLab"


@dataclass
class HasDiningHall(UseYesNoType):
    """
    Whether there is a Dining Hall.
    """

    class Meta:
        name = "hasDiningHall"


@dataclass
class HasLaboratory(UseYesNoType):
    """
    Presence of a laboratory (Yes/No).
    """

    class Meta:
        name = "hasLaboratory"


@dataclass
class HoursPerDayGuestsOnsite(HoursPerDayGuestsOnsiteType):
    """
    Number of hours per day a typical guest spends at the property (Less Than 15,
    15 To 19, More Than 20)
    """

    class Meta:
        name = "hoursPerDayGuestsOnsite"


@dataclass
class IceEvents(UseYesNoType):
    """
    Are there ice-related events such as Hockey, Skating, Ice Capades?
    """

    class Meta:
        name = "iceEvents"


@dataclass
class IsHighSchool(UseYesNoType):
    """
    Presence of a High School, as indicated by education of grades 10, 11, and/or
    12 (Yes/No).
    """

    class Meta:
        name = "isHighSchool"


@dataclass
class IsTertiaryCare(UseYesNoType):
    """
    Presence of tertiary medical care, specialized care beyond a typical secondary
    level, such as Level 1 trauma centers, organ transplant, or prenatal intensive
    care units (Yes/No).
    """

    class Meta:
        name = "isTertiaryCare"


@dataclass
class ItEnergyMeterConfiguration(ItEnergyConfigurationType):
    """
    The IT Energy Configuration/location of IT Energy meters at a data center.
    """

    class Meta:
        name = "itEnergyMeterConfiguration"


@dataclass
class LaundryFacility(OnsiteLaundryType):
    """
    Type of laundry processed at the property (linens, Terry, Linens &amp; Terry)
    """

    class Meta:
        name = "laundryFacility"


@dataclass
class LengthOfAllOpenClosedRefrigerationUnits(
    LengthOfAllOpenClosedRefrigerationUnitsType
):
    """Length of all open or closed Refrigeration or Freezer cases that are used
    for the sale or storage of perishable goods.

    Include display-type refrigerated open or closed cases and cabinets,
    as well as display-type freezer units. These are typically found on
    the sales floor.   See numberOfOpenClosedRefrigerationUnits for more
    information.
    """

    class Meta:
        name = "lengthOfAllOpenClosedRefrigerationUnits"


@dataclass
class LicensedBedCapacity(UseDecimalType):
    """Licensed Bed Capacity is the total number of beds that your hospital is
    licensed to have in operation.

    This may be more than your Staffed Beds, which are those that are
    set up and ready for use.
    """

    class Meta:
        name = "licensedBedCapacity"


@dataclass
class MaximumNumberOfFloors(UseIntegerType):
    """
    Maximum number of floors in the tallest building at the property.
    """

    class Meta:
        name = "maximumNumberOfFloors"


@dataclass
class MaximumResidentCapacity(UseDecimalType):
    """
    Maximum capacity of residents, based on the design of the facility.
    """

    class Meta:
        name = "maximumResidentCapacity"


@dataclass
class MonthsInUse(MonthsInUseType):
    """
    Number of months per year the property is in use.
    """

    class Meta:
        name = "monthsInUse"


@dataclass
class MonthsMainIndoorIceRinkInUse(MonthsInUseType):
    """
    Number of months per year the property is in use.
    """

    class Meta:
        name = "monthsMainIndoorIceRinkInUse"


@dataclass
class NumberOfBedrooms(UseDecimalType):
    """
    Number of bedrooms.
    """

    class Meta:
        name = "numberOfBedrooms"


@dataclass
class NumberOfCashRegisters(UseDecimalType):
    """
    Number of cash registers.
    """

    class Meta:
        name = "numberOfCashRegisters"


@dataclass
class NumberOfCommercialRefrigerationUnits(UseDecimalType):
    """
    Number of Commercial Refrigeration/Freezer cases, including any open or closed
    commercial type case, and including any walk-in units.
    """

    class Meta:
        name = "numberOfCommercialRefrigerationUnits"


@dataclass
class NumberOfCommercialWashingMachines(UseDecimalType):
    """Number of commercial-type washing machines.

    (This does not include residential or coin-operated machines)
    """

    class Meta:
        name = "numberOfCommercialWashingMachines"


@dataclass
class NumberOfComputers(UseDecimalType):
    """
    Number of computers and servers at the property.
    """

    class Meta:
        name = "numberOfComputers"


@dataclass
class NumberOfConcertShowEventsPerYear(UseIntegerType):
    """
    Number of concert/show events per year.
    """

    class Meta:
        name = "numberOfConcertShowEventsPerYear"


@dataclass
class NumberOfCookingEquipmentUnits(UseIntegerType):
    """
    Number of cooking equipment units in a convenience store.
    """

    class Meta:
        name = "numberOfCookingEquipmentUnits"


@dataclass
class NumberOfCurlingSheets(UseIntegerType):
    """
    Number of ice sheets specifically for the purpose of the game of curling.
    """

    class Meta:
        name = "numberOfCurlingSheets"


@dataclass
class NumberOfDcFastEvChargingStations(UseDecimalType):
    """
    Number of DC Fast electric vehicle charging stations.
    """

    class Meta:
        name = "numberOfDcFastEvChargingStations"


@dataclass
class NumberOfFteworkers(UseDecimalType):
    """
    Number of full-time equivalent workers (total number of hours worked by all
    workers, divided by the standard hours in a full time shift).
    """

    class Meta:
        name = "numberOfFTEWorkers"


@dataclass
class NumberOfGuestMealsServedPerYear(UseIntegerType):
    """
    Total number of guest meals (also called meal covers) served each year.
    """

    class Meta:
        name = "numberOfGuestMealsServedPerYear"


@dataclass
class NumberOfHotelRooms(UseDecimalType):
    """
    Total number of rooms for a lodging type of property (hotel).
    """

    class Meta:
        name = "numberOfHotelRooms"


@dataclass
class NumberOfIndoorIceRinks(UseIntegerType):
    """Number of indoor ice rinks used for indoor hockey, ringette, public or
    figure skating.

    This does not include curling sheets.
    """

    class Meta:
        name = "numberOfIndoorIceRinks"


@dataclass
class NumberOfLaundryHookupsInAllUnits(UseIntegerType):
    """
    The total number of laundry hookups in all individual living units (counting
    hookups, whether or not there is a machine).
    """

    class Meta:
        name = "numberOfLaundryHookupsInAllUnits"


@dataclass
class NumberOfLaundryHookupsInCommonArea(UseIntegerType):
    """
    The total number of laundry hookups in all common areas (counting hookups,
    whether or not there is a machine).
    """

    class Meta:
        name = "numberOfLaundryHookupsInCommonArea"


@dataclass
class NumberOfLettersPackagesPerYear(UseIntegerType):
    """
    The number of letters and packages per year is the typical sum of mail products
    (such as lettermail, flyers, packages, parcels etc.) processed for outbound
    delivery in this facility in a 12 month period.
    """

    class Meta:
        name = "numberOfLettersPackagesPerYear"


@dataclass
class NumberOfLevelOneEvChargingStations(UseDecimalType):
    """
    Number of Level One electric vehicle charging stations.
    """

    class Meta:
        name = "numberOfLevelOneEvChargingStations"


@dataclass
class NumberOfLevelTwoEvChargingStations(UseDecimalType):
    """
    Number of Level Two electric vehicle charging stations.
    """

    class Meta:
        name = "numberOfLevelTwoEvChargingStations"


@dataclass
class NumberOfMriMachines(UseDecimalType):
    """
    Number of MRI Machines.
    """

    class Meta:
        name = "numberOfMriMachines"


@dataclass
class NumberOfOpenClosedRefrigerationUnits(UseDecimalType):
    """The Number of Open or Closed Refrigeration/Freezer Units is the count of
    open or closed cases that are used for the sale or storage of perishable goods.

    This includes display-type refrigerated open or closed cases and
    cabinets as well as display-type freezer units typically found on a
    sales floor. Each case or cabinet section, typically 4 to 12 feet in
    length, should be considered 1 unit. Include those cases located
    inside and immediately adjacent to the building. These units may be
    portable or permanent, and may have doors, plastic strips, or other
    flexible cover. This count should not include vending machines. If
    your property is in the design phase, use your best estimate for the
    intended conditions when the property is fully operational.
    """

    class Meta:
        name = "numberOfOpenClosedRefrigerationUnits"


@dataclass
class NumberOfPeople(UseIntegerType):
    """
    Number of people living in the home.
    """

    class Meta:
        name = "numberOfPeople"


@dataclass
class NumberOfResidentialLiftSystems(UseDecimalType):
    """
    Number of residential electronic lift systems.
    """

    class Meta:
        name = "numberOfResidentialLiftSystems"


@dataclass
class NumberOfResidentialLivingUnits(UseDecimalType):
    """Total number of residential living units (apartments or condominiums) at the
    property.

    This value must equal the sum of the number of residential living
    units in a low-rise setting, mid-rise setting, and high-rise
    setting.  A 0.9 tolerance is allowed.
    """

    class Meta:
        name = "numberOfResidentialLivingUnits"


@dataclass
class NumberOfResidentialLivingUnitsHighRiseSetting(UseDecimalType):
    """
    Number of units located in individual buildings that are 10 or more stories in
    height, as well as units located in wings/portions of buildings that fall in
    this range (e.g. if Wing A is 10 stories and Wing B is 5 stories, only units in
    Wing A would be counted here).
    """

    class Meta:
        name = "numberOfResidentialLivingUnitsHighRiseSetting"


@dataclass
class NumberOfResidentialLivingUnitsLowRiseSetting(UseDecimalType):
    """
    Number of units located in individual buildings that are 1 to 4 stories in
    height, as well as units located wings/portions of larger buildings that fall
    in this height range (e.g. if Wing A is 6 stories and Wing B is 3 stories, only
    units in Wing B would be counted here).
    """

    class Meta:
        name = "numberOfResidentialLivingUnitsLowRiseSetting"


@dataclass
class NumberOfResidentialLivingUnitsMidRiseSetting(UseDecimalType):
    """
    Number of units located in individual buildings that are 5 to 9 stories in
    height, as well as units located wings/portions of larger buildings that fall
    in this height range (e.g. if Wing A is 6 stories and Wing B is 3 stories, only
    units in Wing A would be counted here).
    """

    class Meta:
        name = "numberOfResidentialLivingUnitsMidRiseSetting"


@dataclass
class NumberOfResidentialWashingMachines(UseDecimalType):
    """
    Number of residential-type washing machines.
    """

    class Meta:
        name = "numberOfResidentialWashingMachines"


@dataclass
class NumberOfRooms(UseDecimalType):
    """
    Total number of rooms for a lodging type of property (hotel, dormitory, etc).
    """

    class Meta:
        name = "numberOfRooms"


@dataclass
class NumberOfSpecialOtherEventsPerYear(UseIntegerType):
    """
    Number of special/other events per year at a stadium/arena (i.e. events that
    are neither concerts/shows nor athletic events).
    """

    class Meta:
        name = "numberOfSpecialOtherEventsPerYear"


@dataclass
class NumberOfSportingEventsPerYear(UseIntegerType):
    """
    Number of sporting/athletic events per year.
    """

    class Meta:
        name = "numberOfSportingEventsPerYear"


@dataclass
class NumberOfStaffedBeds(UseDecimalType):
    """
    Number of beds set up and staffed for use at a hospital.
    """

    class Meta:
        name = "numberOfStaffedBeds"


@dataclass
class NumberOfSterilizationUnits(UseDecimalType):
    """
    Number of working autoclaves and sterilizers in the building.
    """

    class Meta:
        name = "numberOfSterilizationUnits"


@dataclass
class NumberOfSurgicalOperatingBeds(UseDecimalType):
    """
    Number of beds associated with surgical operation at a medial office/outpatient
    healthcare facility.
    """

    class Meta:
        name = "numberOfSurgicalOperatingBeds"


@dataclass
class NumberOfWalkInRefrigerationUnits(UseDecimalType):
    """Number of walk-in refrigeration/freezer units - including only those commercial type units that you can completely enter to retrieve goods."""

    class Meta:
        name = "numberOfWalkInRefrigerationUnits"


@dataclass
class NumberOfWarmingHeatingEquipmentUnits(UseIntegerType):
    """
    Number of warming/heating equipment units in a convenience store.
    """

    class Meta:
        name = "numberOfWarmingHeatingEquipmentUnits"


@dataclass
class NumberOfWeekdaysOpen(NumberOfWeekdaysType):
    """Number of weekdays (Monday through Friday) the property is open.

    This will be an number between 0 and 5.
    """

    class Meta:
        name = "numberOfWeekdaysOpen"


@dataclass
class NumberOfWeeklyIceResurfacingForAllRinks(
    NumberOfWeeklyIceResurfacingType
):
    """Total number of floods in a week using ice resurfacing machines after
    typical ice rink use for all indoor hockey, ringette, public or figure skating
    ice rinks in the facility.

    This does not include curling sheet resurfacing or pebbling. For
    multiple rinks, sum the total number of weekly resurfacing for all
    rinks.
    """

    class Meta:
        name = "numberOfWeeklyIceResurfacingForAllRinks"


@dataclass
class NumberOfWorkers(UseDecimalType):
    """The total number of workers during the primary (largest shift) - this is only a total number of people in the building at a single time."""

    class Meta:
        name = "numberOfWorkers"


@dataclass
class NutrientRemoval(UseYesNoType):
    """
    Presence of a nutrient removal system at a wastewater treatment plant (Yes/No).
    """

    class Meta:
        name = "nutrientRemoval"


@dataclass
class OnSiteLaundryFacility(UseYesNoType):
    """
    Presence of an on-site Laundry Facility (Yes/No).
    """

    class Meta:
        name = "onSiteLaundryFacility"


@dataclass
class OpenFootage(GrossFloorAreaType):
    """
    Total area of open parking lots/areas.
    """

    class Meta:
        name = "openFootage"


@dataclass
class OpenOnWeekends(UseYesNoType):
    """
    Indication of regular activities that occur on either Saturday or Sunday
    (Yes/No).
    """

    class Meta:
        name = "openOnWeekends"


@dataclass
class OwnedBy(OwnedByType):
    """
    Indication of whether the property is owned by a private, not-for profit, or
    government organization.
    """

    class Meta:
        name = "ownedBy"


@dataclass
class PartiallyEnclosedFootage(GrossFloorAreaType):
    """
    Total area of all parking structures that are only partially enclosed (i.e.
    multi-level structures that only have partial walls).
    """

    class Meta:
        name = "partiallyEnclosedFootage"


@dataclass
class PercentCooled(PercentCooledType):
    """
    The percent of the property that can be cooled by mechanical cooling equipment.
    """

    class Meta:
        name = "percentCooled"


@dataclass
class PercentHeated(PercentHeatedType):
    """
    The percent of the property that can be heated by mechanical heating equipment.
    """

    class Meta:
        name = "percentHeated"


@dataclass
class PercentOfGrossFloorAreaThatIsCommonSpaceOnly(UseDecimalType):
    """
    The percent of the Gross Floor Area that is common space (not individual tenant
    areas)
    """

    class Meta:
        name = "percentOfGrossFloorAreaThatIsCommonSpaceOnly"


@dataclass
class PercentOfficeCooled(PercentOfficeCooledType):
    class Meta:
        name = "percentOfficeCooled"


@dataclass
class PercentOfficeHeated(PercentOfficeHeatedType):
    class Meta:
        name = "percentOfficeHeated"


@dataclass
class PercentUsedForColdStorage(UseIntegerType):
    """
    The total percentage of your property that is enclosed insulated storage space
    intended for the cooling or freezing of goods, merchandise, raw materials, or
    manufactured products in buildings (or portions of buildings), at or less than
    50 degrees F.
    """

    class Meta:
        name = "percentUsedForColdStorage"


@dataclass
class PlantDesignFlowRate(PlantDesignFlowRateType):
    """
    The designed flow rate of a wastewater treatment plant (e.g. the capacity of
    the plant) in million gallons per day (MGD).
    """

    class Meta:
        name = "plantDesignFlowRate"


@dataclass
class PoolLocation(PoolType):
    """
    Indication of whether a pool is indoor or outdoor.
    """

    class Meta:
        name = "poolLocation"


@dataclass
class PoolSize(PoolSizeType):
    """
    Approximate size of a swimming pool (Short Course, Recreational, Olympic).
    """

    class Meta:
        name = "poolSize"


@dataclass
class PrecisionControlsForTemperatureAndHumidity(UseYesNoType):
    """Indicates presence of precise humidity and temperature control: Yes and No are 2 options and 1 or 0 is used."""

    class Meta:
        name = "precisionControlsForTemperatureAndHumidity"


@dataclass
class ResidentPopulation(ResidentPopulationType):
    """
    An indication of the type of residents living at the property, if applicable
    (e.g. student, military, senior, etc).
    """

    class Meta:
        name = "residentPopulation"


@dataclass
class SchoolDistrict(UseStringType):
    """
    The school district in which the school is located.
    """

    class Meta:
        name = "schoolDistrict"


@dataclass
class SeatingCapacity(UseDecimalType):
    """
    The seating capacity associated with the main areas of worship in a worship
    facility.
    """

    class Meta:
        name = "seatingCapacity"


@dataclass
class SingleStore(UseYesNoType):
    """
    Indication that a Retail Store is a single store (Yes/No).
    """

    class Meta:
        name = "singleStore"


@dataclass
class SizeOfElectronicScoreBoards(OptionalFloorAreaType):
    """
    The total size of electronic score boards at a stadium/arena.
    """

    class Meta:
        name = "sizeOfElectronicScoreBoards"


@dataclass
class SpectatorSeatingCapacity(UseDecimalType):
    """
    Number of ice sheets specifically for the purpose of the game of curling.
    """

    class Meta:
        name = "spectatorSeatingCapacity"


@dataclass
class StudentSeatingCapacity(UseDecimalType):
    """
    The number of students the school can accommodate (including portable
    classrooms).
    """

    class Meta:
        name = "studentSeatingCapacity"


@dataclass
class SupplementalHeating(UseYesNoType):
    """
    Presence of supplemental heating systems in a parking garage (Yes/No).
    """

    class Meta:
        name = "supplementalHeating"


@dataclass
class SurgeryCenterFloorArea(OptionalFloorAreaType):
    """
    The area within a medical office or outpatient healthcare property devoted to
    surgery.
    """

    class Meta:
        name = "surgeryCenterFloorArea"


@dataclass
class TotalGrossFloorArea(GrossFloorAreaType):
    class Meta:
        name = "totalGrossFloorArea"


@dataclass
class TotalIceRinkSurfaceAreaForAllRinks(OptionalFloorAreaType):
    """The indoor ice rink surface area is the total area covered by ice of all the
    ice rinks used for indoor hockey, ringette, public or figure skating and can be
    estimated by multiplying the length of the ice surface with the width of the
    ice surface and adding together the calculated area for each ice rink in the
    facility.

    This surface area does not include curling sheets.
    """

    class Meta:
        name = "totalIceRinkSurfaceAreaForAllRinks"


@dataclass
class UpsSystemRedundancy(UpsSystemRedundancyType):
    """
    Level of redundancy for the Uninterruptible Power Supply (UPS) system in a Data
    Center.
    """

    class Meta:
        name = "upsSystemRedundancy"


@dataclass
class WeeklyOperatingHours(UseDecimalType):
    """The total number of hours per week that the property is occupied by the
    majority of the employees.

    It does not include hours when the property is occupied only by
    maintenance, security, or other support personnel.
    """

    class Meta:
        name = "weeklyOperatingHours"
