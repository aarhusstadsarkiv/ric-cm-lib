from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText

from .thing import Thing

__all__ = [
    "Mandate",
    "Rule",
]


@dataclass
class Rule(Thing):
    history: FreeText | ModelBasedText
    rule_type: controlled_values.RuleType


@dataclass
class Mandate(Rule):
    mandate_type: controlled_values.MandateType
