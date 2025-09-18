from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.types import ModelBasedText
from ric_cm_lib.types import RuleBasedText

from .thing import Thing

__all__ = ["Date"]


@dataclass
class Date(Thing):
    date_qualifier: controlled_values.DateQualifier
    date_type: controlled_values.DateType
    expressed_date: ModelBasedText
    normalized_date: RuleBasedText
