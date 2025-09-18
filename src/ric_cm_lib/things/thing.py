from dataclasses import dataclass

from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText
from ric_cm_lib.types import RuleBasedText

__all__ = ["Thing"]


@dataclass
class Thing:
    identifier: FreeText | ModelBasedText | RuleBasedText
    name: FreeText | ModelBasedText
    general_description: FreeText
