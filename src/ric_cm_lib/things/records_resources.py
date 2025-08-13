from dataclasses import dataclass

from ric_cm_lib import controlled_values
from ric_cm_lib.types import FreeText, ModelBasedText

from .thing import Thing

__all__ = [
    "Record",
    "RecordPart",
    "RecordSet",
]


@dataclass
class RecordResource(Thing):
    authenticity_note: (
        FreeText | ModelBasedText | None
    )  # https://www.ica.org/standards/RiC/ontology#authenticityNote
    classification: (
        controlled_values.ClassificationType | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#classification
    conditions_of_access: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#conditionsOfAccess
    conditions_of_use: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#conditionsOfUse
    content_type: (
        controlled_values.ContentType
    )  # https://www.ica.org/standards/RiC/ontology#ContentType
    history: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#history
    integrity_note: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#integrityNote
    language: (
        controlled_values.Language
    )  # https://www.ica.org/standards/RiC/ontology#Language
    legal_status: (
        controlled_values.LegalStatus
    )  # https://www.ica.org/standards/RiC/ontology#LegalStatus
    record_resource_extent: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#recordResourceExtent
    scope_and_content: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#scopeAndContent
    state: (
        controlled_values.RecordState
    )  # https://www.ica.org/standards/RiC/ontology#RecordState
    structure: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#structure


@dataclass
class RecordSet(RecordResource):
    accruals: (
        FreeText | ModelBasedText
    )  # https://www.ica.org/standards/RiC/ontology#accruals
    record_set_type: (
        controlled_values.RecordSetType
    )  # https://www.ica.org/standards/RiC/ontology#RecordSetType


@dataclass
class Record(RecordResource):
    documentary_form_type: (
        controlled_values.DocumentaryFormType
    )  # https://www.ica.org/standards/RiC/ontology#DocumentaryFormType


@dataclass
class RecordPart(RecordResource):
    documentary_form_type: (
        controlled_values.DocumentaryFormType
    )  # https://www.ica.org/standards/RiC/ontology#DocumentaryFormType
