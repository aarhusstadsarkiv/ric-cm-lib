from typing import Literal

from . import agents
from . import dates
from . import events
from . import instantiations
from . import places
from . import records_resources
from . import rules
from .thing import Thing

__all__ = [
    "EntityDomain",
    "Thing",
    "agents",
    "dates",
    "events",
    "instantiations",
    "places",
    "records_resources",
    "rules",
]

EntityDomain: type = Literal[
    "Activity",
    "CorporateBody",
    "Date",
    "Event",
    "Family",
    "Instantiation",
    "Mandate",
    "Mechanism",
    "Person",
    "Place",
    "Position",
    "Record",
    "RecordPart",
    "RecordSet",
    "Rule",
]
