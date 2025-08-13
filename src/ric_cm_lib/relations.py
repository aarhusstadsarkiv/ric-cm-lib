from dataclasses import dataclass
from enum import Enum
from typing import Literal

from ric_cm_lib import things
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText
from ric_cm_lib.types import RuleBasedText

__all__ = [
    "Relation",
    "RelationType",
]


class RelationType(Enum):
    R001 = 1
    R002 = 2
    R002i = -2
    R003 = 3
    R003i = -3
    R004 = 4
    R004i = -4
    R005 = 5
    R005i = -5
    R006 = 6
    R006i = -6
    R007 = 7
    R007i = -7
    R008 = 8
    R008i = -8
    R009 = 9
    R009i = -9
    R010 = 10
    R010i = -10
    R011 = 11
    R011i = -11
    R012 = 12
    R012i = -12
    R013 = 13
    R013i = -13
    R014 = 14
    R014i = -14
    R015 = 15
    R015i = -15
    R016 = 16
    R016i = -16
    R017 = 17
    R017i = -17
    R018 = 18
    R018i = -18
    R019 = 19
    R019i = -19
    R020 = 20
    R020i = -20
    R021 = 21
    R021i = -21
    R022 = 22
    R023 = 23
    R024 = 24
    R024i = -24
    R025 = 25
    R025i = -25
    R026 = 26
    R026i = -26
    R027 = 27
    R027i = -27
    R028 = 28
    R028i = -28
    R029 = 29
    R029i = -29
    R030 = 30
    R030i = -30
    R031 = 31
    R031i = -31
    R032 = 32
    R032i = -32
    R033 = 33
    R033i = -33
    R034 = 34
    R035 = 35
    R036 = 36
    R036i = -36
    R037 = 37
    R037i = -37
    R038 = 38
    R038i = -38
    R039 = 39
    R039i = -39
    R040 = 40
    R040i = -40
    R041 = 41
    R041i = -41
    R042 = 42
    R042i = -42
    R044 = 44
    R045 = 45
    R045i = -45
    R046 = 46
    R047 = 47
    R048 = 48
    R049 = 49
    R050 = 50
    R050i = -50
    R051 = 51
    R052 = 52
    R053 = 53
    R053i = -53
    R054 = 54
    R054i = -54
    R055 = 55
    R055i = -55
    R056 = 56
    R056i = -56
    R057 = 57
    R057i = -57
    R058 = 58
    R058i = -58
    R059 = 59
    R059i = -59
    R060 = 60
    R060i = -60
    R061 = 61
    R061i = -61
    R062 = 62
    R062i = -62
    R063 = 63
    R063i = -63
    R064 = 64
    R064i = -64
    R065 = 65
    R065i = -65
    R066 = 66
    R066i = -66
    R067 = 67
    R067i = -67
    R068 = 68
    R068i = -68
    R069 = 69
    R069i = -69
    R070 = 70
    R070i = -70
    R071 = 71
    R071i = -71
    R072 = 72
    R072i = -72
    R073 = 73
    R073i = -73
    R074 = 74
    R074i = -74
    R075 = 75
    R075i = -75
    R076 = 76
    R076i = -76
    R077 = 77
    R078 = 78
    R079 = 79
    R079i = -79


@dataclass
class Relation:
    certainty_of_relation: FreeText | ModelBasedText
    date_of_relation: FreeText | ModelBasedText | RuleBasedText  # RA02
    description_of_relation: FreeText  # RA03
    identifier_of_relation: FreeText | ModelBasedText | RuleBasedText  # RA04
    source_of_relation: FreeText | ModelBasedText
    place_of_relation: str  # RA06

    relation_type: RelationType
    domain_type: things.EntityDomain | Literal["Relation"]
    domain_identifier: str
    target_type: things.EntityDomain | Literal["Relation"]
    target_identifier: str
