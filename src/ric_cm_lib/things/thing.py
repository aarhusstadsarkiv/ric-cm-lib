from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText
from ric_cm_lib.types import RuleBasedText

__all__ = ["Thing"]

class Thing:
    identifier: FreeText | ModelBasedText | RuleBasedText  # https://www.ica.org/standards/RiC/ontology#identifier
    name: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#name
    general_description: FreeText  # https://www.ica.org/standards/RiC/ontology#generalDescription