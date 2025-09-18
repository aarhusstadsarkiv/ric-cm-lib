from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText

from .thing import Thing

__all__ = ["Instantiation"]


@dataclass
class Instantiation(Thing):
    authenticity_note: FreeText | ModelBasedText | None
    carrier_extent: FreeText | ModelBasedText | None
    carrier_type: controlled_values.CarrierType
    conditions_of_access: FreeText | ModelBasedText
    conditions_of_use: FreeText | ModelBasedText
    history: FreeText | ModelBasedText
    instantiation_extent: FreeText | ModelBasedText
    physical_characteristics_note: FreeText | ModelBasedText
    production_technique: FreeText | controlled_values.ProductionTechnique
    quality_of_representation_note: FreeText | ModelBasedText
    representation_type: controlled_values.RepresentationType
    structure: FreeText | ModelBasedText
