from ric_cm_lib import controlled_values
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText

from .thing import Thing

__all__ = ["Instantiation"]


class Instantiation(Thing):
    authenticity_note: FreeText | ModelBasedText | None  # https://www.ica.org/standards/RiC/ontology#authenticityNote
    carrier_extent: FreeText | ModelBasedText | None  # https://www.ica.org/standards/RiC/ontology#CarrierExtent
    carrier_type: controlled_values.CarrierType  # https://www.ica.org/standards/RiC/ontology#CarrierType
    conditions_of_access: FreeText | ModelBasedText
    conditions_of_use: FreeText | ModelBasedText
    history: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#history
    instantiation_extent: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#instantiationExtent
    physical_characteristics_note: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#physicalCharacteristicsNote
    production_technique: FreeText | controlled_values.ProductionTechnique  # https://www.ica.org/standards/RiC/ontology#productionTechnique
    quality_of_representation_note: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#qualityOfRepresentationNote
    representation_type: controlled_values.RepresentationType  # https://www.ica.org/standards/RiC/ontology#RepresentationType
    structure: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#instantiationStructure
