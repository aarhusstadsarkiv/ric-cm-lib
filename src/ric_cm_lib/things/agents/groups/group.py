from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.things.agents.agent import Agent

__all__ = [
    "CorporateBody",
    "Family",
    "Group",
]


@dataclass
class Group(Agent):
    demographic_group: (
        controlled_values.DemographicGroup
    )  # https://www.ica.org/standards/RiC/ontology±#DemographicGroup


@dataclass
class Family(Group):
    family_type: controlled_values.FamilyType  # https://www.ica.org/standards/RiC/ontology#FamilyType


@dataclass
class CorporateBody(Group):
    corporate_body_type: (
        controlled_values.CorporateBodyType
    )  # https://www.ica.org/standards/RiC/ontology#CorporateBodyType
