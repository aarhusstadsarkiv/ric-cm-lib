from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.things.thing import Thing
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText

__all__ = [
    "Coordinates",
    "Place",
]


@dataclass
class Coordinates(Thing):
    latitude: float
    longitude: float
    height: float | None
    standard: str | None


@dataclass
class Place(Thing):
    coordinates: Coordinates
    history: FreeText | ModelBasedText
    location: FreeText
    place_type: controlled_values.PlaceType
