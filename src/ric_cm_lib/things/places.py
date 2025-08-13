from ric_cm_lib import controlled_values
from ric_cm_lib.things.thing import Thing
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText

__all__ = [
    "Coordinates",
    "Place",
]


class Coordinates(Thing):
    latitude: float
    longitude: float
    height: float | None
    standard: str | None


class Place(Thing):
    coordinates: Coordinates  # https://www.ica.org/standards/RiC/ontology#Coordinates
    history: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#history
    location: FreeText  # https://www.ica.org/standards/RiC/ontology#location
    place_type: controlled_values.PlaceType  # https://www.ica.org/standards/RiC/ontology#PlaceType
