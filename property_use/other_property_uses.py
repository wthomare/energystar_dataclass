from dataclasses import dataclass, field
from typing import Optional

from test_fixtures.primer.common.audit import LogType
from test_fixtures.primer.property_use.characteristics import (
    NumberOfComputers,
    NumberOfWorkers,
    TotalGrossFloorArea,
    WeeklyOperatingHours,
)


@dataclass
class OtherType:
    class Meta:
        name = "otherType"

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
    use_details: Optional["OtherType.UseDetails"] = field(
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
        weekly_operating_hours: Optional[WeeklyOperatingHours] = field(
            default=None,
            metadata={
                "name": "weeklyOperatingHours",
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
        number_of_workers: Optional[NumberOfWorkers] = field(
            default=None,
            metadata={
                "name": "numberOfWorkers",
                "type": "Element",
            },
        )


@dataclass
class AdultEducation(OtherType):
    """
    Buildings used primarily for providing adult students with continuing
    education, workforce development, or professional development outside of the
    college or university setting.
    """

    class Meta:
        name = "adultEducation"


@dataclass
class AmbulatorySurgicalCenter(OtherType):
    """
    Health care facilities that provide same-day surgical care, including
    diagnostic and preventive procedures.
    """

    class Meta:
        name = "ambulatorySurgicalCenter"


@dataclass
class Aquarium(OtherType):
    """
    Buildings used to provide aquatic habitat primarily to live animals and which
    may include public or private viewing areas and  educational programs.
    """

    class Meta:
        name = "aquarium"


@dataclass
class BarNightclub(OtherType):
    """
    Buildings used primarily for social/entertainment purposes, and is
    characterized by most of the revenue being generated from the sale of beverages
    instead of food.
    """

    class Meta:
        name = "barNightclub"


@dataclass
class BowlingAlley(OtherType):
    """
    Buildings used for public or private, recreational or professional bowling.
    """

    class Meta:
        name = "bowlingAlley"


@dataclass
class Casino(OtherType):
    """
    Buildings primarily used to conduct gambling activities including both
    electronic and live table games.
    """

    class Meta:
        name = "casino"


@dataclass
class ConventionCenter(OtherType):
    """
    Buildings used primarily for large conferences, exhibitions, and similar
    events.
    """

    class Meta:
        name = "conventionCenter"


@dataclass
class EnclosedMall(OtherType):
    """
    Buildings that house multiple stores, often “anchored” by one or more
    department stores, and with interior walkways.
    """

    class Meta:
        name = "enclosedMall"


@dataclass
class EnergyPowerStation(OtherType):
    """
    Buildings containing machinery and/or associated equipment for generating
    electricity or district heat (steam, hot water, or chilled water) from a raw
    fuel, including fossil fuel power plants, traditional district heat power
    plants, combined heat and power plants,  nuclear reactors, hydroelectric dams,
    or facilities associated with a solar or wind farm.
    """

    class Meta:
        name = "energyPowerStation"


@dataclass
class FastFoodRestaurant(OtherType):
    """Buildings used for the preparation and sale of ready-to-eat food.

    Also known as Quick Service Restaurant.
    """

    class Meta:
        name = "fastFoodRestaurant"


@dataclass
class FireStation(OtherType):
    """
    Buildings used to provide emergency response services associated with fires.
    """

    class Meta:
        name = "fireStation"


@dataclass
class FitnessCenterHealthClubGym(OtherType):
    """
    Buildings used for recreational or professional athletic training and related
    activities.
    """

    class Meta:
        name = "fitnessCenterHealthClubGym"


@dataclass
class FoodService(OtherType):
    """
    Buildings used for preparation and sale of food and beverages, but which do not
    meet the definition of Restaurant, Cafeteria, or Bar/Nightclub.
    """

    class Meta:
        name = "foodService"


@dataclass
class Laboratory(OtherType):
    """
    Buildings that provide controlled conditions in which scientific research,
    measurement, and experiments are performed or practical science is taught.
    """

    class Meta:
        name = "laboratory"


@dataclass
class LifestyleCenter(OtherType):
    """
    A mixed use commercial development that includes retail stores and leisure
    amenities, where individual retail stores typically contain an entrance
    accessible from the outside and are not connected by internal walkways.
    """

    class Meta:
        name = "lifestyleCenter"


@dataclass
class ManufacturingIndustrialPlant(OtherType):
    """
    Buildings used for manufacturing or assembling goods.
    """

    class Meta:
        name = "manufacturingIndustrialPlant"


@dataclass
class MovieTheater(OtherType):
    """
    Buildings used for public or private film screenings.
    """

    class Meta:
        name = "movieTheater"


@dataclass
class Other(OtherType):
    """
    Buildings that do not fall within any of the available property use categories
    in Portfolio Manager.
    """

    class Meta:
        name = "other"


@dataclass
class OtherEducation(OtherType):
    """
    Buildings used for religious, community, or other educational purposes not
    described in the available property uses in Portfolio Manager (i.e. educational
    purposes other than adult education, college/university, K-12 school, pre-
    school/daycare and vocational schools).
    """

    class Meta:
        name = "otherEducation"


@dataclass
class OtherEntertainmentPublicAssembly(OtherType):
    """
    Buildings whose primary use is for entertainment or public gatherings and that
    do not meet the definition of any other property use defined in Portfolio
    Manager.
    """

    class Meta:
        name = "otherEntertainmentPublicAssembly"


@dataclass
class OtherLodgingResidential(OtherType):
    """
    Buildings used for residential  purposes other than those described in the
    available property uses in Portfolio Manager (i.e. residential other than
    multifamily residential, single family home, senior care community, residence
    hall/dormitory, barracks, prison/incarceration, or hotel).
    """

    class Meta:
        name = "otherLodgingResidential"


@dataclass
class OtherMall(OtherType):
    """
    Buildings containing a collection of stores whose purpose is the sale of goods,
    but which do not fit into the enclosed mall, lifestyle center, or strip mall
    property types.
    """

    class Meta:
        name = "otherMall"


@dataclass
class OtherPublicServices(OtherType):
    """
    Buildings used by public-sector organizations to provide public services other
    than those described in the available property uses in Portfolio Manager (i.e.
    services other than offices, courthouses, drinking water treatment and
    distribution plants, fire stations, libraries, mailing centers or post offices,
    police stations, prisons or incarceration facilities, social or meeting halls,
    transportation terminals or stations, or wastewater treatment plants).
    """

    class Meta:
        name = "otherPublicServices"


@dataclass
class OtherRecreation(OtherType):
    """
    Buildings primarily used for recreation that do not meet the definition of any
    other property use defined in Portfolio Manager.
    """

    class Meta:
        name = "otherRecreation"


@dataclass
class OtherRestaurantBar(OtherType):
    """
    Buildings used for preparation and sale of ready-to-eat food and beverages, but
    which does not fit into the fast food restaurant, restaurant, or bar/nightclub
    property types.
    """

    class Meta:
        name = "otherRestaurantBar"


@dataclass
class OtherServices(OtherType):
    """
    Buildings in which primarily services are offered, but which does not fit into
    the Personal Services or Repair Services property types.
    """

    class Meta:
        name = "otherServices"


@dataclass
class OtherSpecialityHospital(OtherType):
    """
    Long-term acute care hospitals, inpatient rehabilitation facilities, including
    Cancer Centers and Psychiatric and Substance Abuse Hospitals/Facilities.
    """

    class Meta:
        name = "otherSpecialityHospital"


@dataclass
class OtherTechnologyScience(OtherType):
    """
    Buildings used for science and technology related services other than
    Laboratories and Data Centers.
    """

    class Meta:
        name = "otherTechnologyScience"


@dataclass
class OtherUtility(OtherType):
    """
    Buildings used by a utility for some purpose other than general office or
    energy/power generation.
    """

    class Meta:
        name = "otherUtility"


@dataclass
class OutpatientRehabilitationPhysicalTherapy(OtherType):
    """
    Buildings used to provide diagnosis and treatment for rehabilitation and
    physical therapy.
    """

    class Meta:
        name = "outpatientRehabilitationPhysicalTherapy"


@dataclass
class PerformingArts(OtherType):
    """
    Buildings used for public or private artistic or musical performances.
    """

    class Meta:
        name = "performingArts"


@dataclass
class PersonalServices(OtherType):
    """Buildings used to sell services rather than physical goods.

    Examples include dry cleaners, salons, spas, etc.
    """

    class Meta:
        name = "personalServices"


@dataclass
class PoliceStation(OtherType):
    """
    Buildings used for federal, state, or local police forces and their associated
    office space.
    """

    class Meta:
        name = "policeStation"


@dataclass
class PreschoolDaycare(OtherType):
    """
    Buildings used for educational programs or daytime supervision/recreation for
    young children before they attend Kindergarten.
    """

    class Meta:
        name = "preschoolDaycare"


@dataclass
class Prison(OtherType):
    """
    Prison/Incarceration federal, state, local, or private-sector Buildings used
    for the detention of persons awaiting trial or convicted of crimes.
    """

    class Meta:
        name = "prison"


@dataclass
class RaceTrack(OtherType):
    """
    Buildings used primarily to hold racing events such as vehicle races,
    track/field races, horse races, and/or dog-races.
    """

    class Meta:
        name = "raceTrack"


@dataclass
class RepairServices(OtherType):
    """Buildings in which some type of repair service is provided.

    Examples include vehicle service or repair shops, shoe repair,
    jewelry repair, locksmiths, etc.
    """

    class Meta:
        name = "repairServices"


@dataclass
class Restaurant(OtherType):
    """Buildings used for preparation and sale of ready-to-eat food and beverages,
    but which do not fit in the fast food property type.

    (Fast casual, casual, and fine dining restaurants).
    """

    class Meta:
        name = "restaurant"


@dataclass
class RollerRink(OtherType):
    """
    Buildings used primarily for roller-skating, inline skating/rollerblading, or
    skateboarding.
    """

    class Meta:
        name = "rollerRink"


@dataclass
class SocialMeetingHall(OtherType):
    """
    Buildings primarily used for public or private gatherings.
    """

    class Meta:
        name = "socialMeetingHall"


@dataclass
class StripMall(OtherType):
    """
    Buildings comprising more than one retail store, restaurant, or other business,
    in an open-air configuration where each establishment has an exterior entrance
    to the public and there are no internal walkways.
    """

    class Meta:
        name = "stripMall"


@dataclass
class TransportationTerminalStation(OtherType):
    """
    Buildings used primarily for accessing public or private transportation.
    """

    class Meta:
        name = "transportationTerminalStation"


@dataclass
class UrgentCareClinicOtherOutpatient(OtherType):
    """
    Buildings used to treat patients, usually on an unscheduled, walk-in basis, who
    have an injury or illness that requires immediate care but is not serious
    enough to warrant a visit to an emergency department.
    """

    class Meta:
        name = "urgentCareClinicOtherOutpatient"


@dataclass
class VeterinaryOffice(OtherType):
    """
    Buildings used for the medical care and treatment of animals.
    """

    class Meta:
        name = "veterinaryOffice"


@dataclass
class VocationalSchool(OtherType):
    """
    Vocational School Buildings primarily designed to teach skilled trades to
    students, including trade and technical schools.
    """

    class Meta:
        name = "vocationalSchool"


@dataclass
class Zoo(OtherType):
    """
    Buildings used primarily to provide habitat to live animals and which may
    include public or private viewing and educational programs.
    """

    class Meta:
        name = "zoo"
