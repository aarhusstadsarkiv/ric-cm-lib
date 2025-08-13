from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText

from .thing import Thing

__all__ = [
    "Record",
    "RecordPart",
    "RecordSet",
]


@dataclass
class RecordResource(Thing):
    authenticity_note: FreeText | ModelBasedText | None
    classification: controlled_values.ClassificationType | ModelBasedText
    conditions_of_access: FreeText | ModelBasedText
    conditions_of_use: FreeText | ModelBasedText
    content_type: controlled_values.ContentType
    history: FreeText | ModelBasedText
    integrity_note: FreeText | ModelBasedText
    language: controlled_values.Language
    legal_status: controlled_values.LegalStatus
    record_resource_extent: FreeText | ModelBasedText
    scope_and_content: FreeText | ModelBasedText
    state: controlled_values.RecordState
    structure: FreeText | ModelBasedText


@dataclass
class RecordSet(RecordResource):
    accruals: FreeText | ModelBasedText
    record_set_type: controlled_values.RecordSetType


@dataclass
class Record(RecordResource):
    documentary_form_type: controlled_values.DocumentaryFormType


@dataclass
class RecordPart(RecordResource):
    documentary_form_type: controlled_values.DocumentaryFormType
