from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.things.thing import Thing
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText


@dataclass
class Agent(Thing):
    history: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#history
    language: controlled_values.Language  # https://www.ica.org/standards/RiC/ontology#Language
    legal_status: controlled_values.LegalStatus  # https://www.ica.org/standards/RiC/ontology#LegalStatus


@dataclass
class Person(Agent):
    demographic_group: controlled_values.DemographicGroup  # https://www.ica.org/standards/RiC/ontology#DemographicGroup
    occupation_type: controlled_values.OccupationType  # https://www.ica.org/standards/RiC/ontology#OccupationType


@dataclass
class Position(Agent): ...


@dataclass
class Mechanism(Agent):
    technical_characteristics: FreeText  # https://www.ica.org/standards/RiC/ontology#technicalCharacteristics
