from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText

from .thing import Thing

__all__ = [
    "Activity",
    "Event",
]


@dataclass
class Event(Thing):
    event_type: controlled_values.EventType  # https://www.ica.org/standards/RiC/ontology#EventType
    history: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#history


@dataclass
class Activity(Event):
    activity_type: controlled_values.ActivityType  # https://www.ica.org/standards/RiC/ontology#ActivityType
