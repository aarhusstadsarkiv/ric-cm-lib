from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.types import ModelBasedText, RuleBasedText

from .thing import Thing

__all__ = ["Date"]


@dataclass
class Date(Thing):
    date_qualifier: (
        controlled_values.DateQualifier
    )  # https://www.ica.org/standards/RiC/ontology#dateQualifier
    date_type: (
        controlled_values.DateType
    )  # https://www.ica.org/standards/RiC/ontology#DateType
    expressed_date: (
        ModelBasedText  # https://www.ica.org/standards/RiC/ontology#expressedDate
    )
    normalized_date: (
        RuleBasedText  # https://www.ica.org/standards/RiC/ontology#normalizedDateValue
    )
