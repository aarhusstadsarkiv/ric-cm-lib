from ric_cm_lib import controlled_values
from ric_cm_lib.things.thing import Thing
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText


class Agent(Thing):
    history: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#history
    language: controlled_values.Language  # https://www.ica.org/standards/RiC/ontology#Language
    legal_status: controlled_values.LegalStatus  # https://www.ica.org/standards/RiC/ontology#LegalStatus


class Person(Agent):
    demographic_group: controlled_values.DemographicGroup  # https://www.ica.org/standards/RiC/ontology#DemographicGroup
    occupation_type: controlled_values.OccupationType  # https://www.ica.org/standards/RiC/ontology#OccupationType


class Position(Agent):
    ...


class Mechanism(Agent):
    technical_characteristics: FreeText  # https://www.ica.org/standards/RiC/ontology#technicalCharacteristics
