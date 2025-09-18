from dataclasses import dataclass
from enum import Enum
from typing import Literal
from typing import Optional

from ric_cm_lib import things
from ric_cm_lib.types import FreeText
from ric_cm_lib.types import ModelBasedText
from ric_cm_lib.types import RuleBasedText

__all__ = [
    "Relation",
    "RelationType",
]


class RelationType(Enum):
    """
    :ivar R001: RiC-R001
    :ivar R002: RiC-R002
    :ivar R002i: RiC-R002i
    :ivar R003: RiC-R003
    :ivar R003i: RiC-R003i
    :ivar R004: RiC-R004
    :ivar R004i: RiC-R004i
    :ivar R005: RiC-R005
    :ivar R005i: RiC-R005i
    :ivar R006: RiC-R006
    :ivar R006i: RiC-R006i
    :ivar R007: RiC-R007
    :ivar R007i: RiC-R007i
    :ivar R008: RiC-R008
    :ivar R008i: RiC-R008i
    :ivar R009: RiC-R009
    :ivar R009i: RiC-R009i
    :ivar R010: RiC-R010
    :ivar R010i: RiC-R010i
    :ivar R011: RiC-R011
    :ivar R011i: RiC-R011i
    :ivar R012: RiC-R012
    :ivar R012i: RiC-R012i
    :ivar R013: RiC-R013
    :ivar R013i: RiC-R013i
    :ivar R014: RiC-R014
    :ivar R014i: RiC-R014i
    :ivar R015: RiC-R015
    :ivar R015i: RiC-R015i
    :ivar R016: RiC-R016
    :ivar R016i: RiC-R016i
    :ivar R017: RiC-R017
    :ivar R017i: RiC-R017i
    :ivar R018: RiC-R018
    :ivar R018i: RiC-R018i
    :ivar R019: RiC-R019
    :ivar R019i: RiC-R019i
    :ivar R020: RiC-R020
    :ivar R020i: RiC-R020i
    :ivar R021: RiC-R021
    :ivar R021i: RiC-R021i
    :ivar R022: RiC-R022
    :ivar R023: RiC-R023
    :ivar R024: RiC-R024
    :ivar R024i: RiC-R024i
    :ivar R025: RiC-R025
    :ivar R025i: RiC-R025i
    :ivar R026: RiC-R026
    :ivar R026i: RiC-R026i
    :ivar R027: RiC-R027
    :ivar R027i: RiC-R027i
    :ivar R028: RiC-R028
    :ivar R028i: RiC-R028i
    :ivar R029: RiC-R029
    :ivar R029i: RiC-R029i
    :ivar R030: RiC-R030
    :ivar R030i: RiC-R030i
    :ivar R031: RiC-R031
    :ivar R031i: RiC-R031i
    :ivar R032: RiC-R032
    :ivar R032i: RiC-R032i
    :ivar R033: RiC-R033
    :ivar R033i: RiC-R033i
    :ivar R034: RiC-R034
    :ivar R035: RiC-R035
    :ivar R036: RiC-R036
    :ivar R036i: RiC-R036i
    :ivar R037: RiC-R037
    :ivar R037i: RiC-R037i
    :ivar R038: RiC-R038
    :ivar R038i: RiC-R038i
    :ivar R039: RiC-R039
    :ivar R039i: RiC-R039i
    :ivar R040: RiC-R040
    :ivar R040i: RiC-R040i
    :ivar R041: RiC-R041
    :ivar R041i: RiC-R041i
    :ivar R042: RiC-R042
    :ivar R042i: RiC-R042i
    :ivar R043: RiC-R043
    :ivar R044: RiC-R044
    :ivar R045: RiC-R045
    :ivar R045i: RiC-R045i
    :ivar R046: RiC-R046
    :ivar R047: RiC-R047
    :ivar R048: RiC-R048
    :ivar R049: RiC-R049
    :ivar R050: RiC-R050
    :ivar R050i: RiC-R050i
    :ivar R051: RiC-R051
    :ivar R052: RiC-R052
    :ivar R053: RiC-R053
    :ivar R053i: RiC-R053i
    :ivar R054: RiC-R054
    :ivar R054i: RiC-R054i
    :ivar R055: RiC-R055
    :ivar R055i: RiC-R055i
    :ivar R056: RiC-R056
    :ivar R056i: RiC-R056i
    :ivar R057: RiC-R057
    :ivar R057i: RiC-R057i
    :ivar R058: RiC-R058
    :ivar R058i: RiC-R058i
    :ivar R059: RiC-R059
    :ivar R059i: RiC-R059i
    :ivar R060: RiC-R060
    :ivar R060i: RiC-R060i
    :ivar R061: RiC-R061
    :ivar R061i: RiC-R061i
    :ivar R062: RiC-R062
    :ivar R062i: RiC-R062i
    :ivar R063: RiC-R063
    :ivar R063i: RiC-R063i
    :ivar R064: RiC-R064
    :ivar R064i: RiC-R064i
    :ivar R065: RiC-R065
    :ivar R065i: RiC-R065i
    :ivar R066: RiC-R066
    :ivar R066i: RiC-R066i
    :ivar R067: RiC-R067
    :ivar R067i: RiC-R067i
    :ivar R068: RiC-R068
    :ivar R068i: RiC-R068i
    :ivar R069: RiC-R069
    :ivar R069i: RiC-R069i
    :ivar R070: RiC-R070
    :ivar R070i: RiC-R070i
    :ivar R071: RiC-R071
    :ivar R071i: RiC-R071i
    :ivar R072: RiC-R072
    :ivar R072i: RiC-R072i
    :ivar R073: RiC-R073
    :ivar R073i: RiC-R073i
    :ivar R074: RiC-R074
    :ivar R074i: RiC-R074i
    :ivar R075: RiC-R075
    :ivar R075i: RiC-R075i
    :ivar R076: RiC-R076
    :ivar R076i: RiC-R076i
    :ivar R077: RiC-R077
    :ivar R078: RiC-R078
    :ivar R079: RiC-R079
    :ivar R079i: RiC-R079i
    :ivar R080: RiC-R080
    :ivar R080i: RiC-R080i
    :ivar R081: RiC-R081
    :ivar R081i: RiC-R081i
    :ivar R082: RiC-R082
    :ivar R082i: RiC-R082i
    :ivar R083: RiC-R083
    :ivar R083i: RiC-R083i
    :ivar R084: RiC-R084
    :ivar R084i: RiC-R084i
    :ivar R085: RiC-R085
    :ivar R085i: RiC-R085i
    :ivar R086: RiC-R086
    :ivar R086i: RiC-R086i
    """

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
    R043 = 43
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
    R080 = 80
    R080i = -80
    R081 = 81
    R081i = -81
    R082 = 82
    R082i = -82
    R083 = 83
    R083i = -83
    R084 = 84
    R084i = -84
    R085 = 85
    R085i = -85
    R086 = 86
    R086i = -86

    @property
    def inverse(self) -> Optional["RelationType"]:
        return _inverse.get(self)

    @property
    def narrower(self) -> list["RelationType"]:
        return _narrow.get(self, [])

    @property
    def broader(self) -> list["RelationType"]:
        return _broad.get(self, [])

    @property
    def tree(self) -> list["RelationType"]:
        tree = [self]
        while parents := tree[0].broader:
            tree.insert(0, sorted(parents, key=lambda r: r.value)[0])
        return tree


_inverse: dict[RelationType, RelationType] = {
    RelationType.R002i: RelationType.R002,
    RelationType.R003i: RelationType.R003,
    RelationType.R004i: RelationType.R004,
    RelationType.R005i: RelationType.R005,
    RelationType.R006i: RelationType.R006,
    RelationType.R007i: RelationType.R007,
    RelationType.R008i: RelationType.R008,
    RelationType.R009i: RelationType.R009,
    RelationType.R010i: RelationType.R010,
    RelationType.R011i: RelationType.R011,
    RelationType.R012i: RelationType.R012,
    RelationType.R013i: RelationType.R013,
    RelationType.R014i: RelationType.R014,
    RelationType.R015i: RelationType.R015,
    RelationType.R016i: RelationType.R016,
    RelationType.R017i: RelationType.R017,
    RelationType.R018i: RelationType.R018,
    RelationType.R019i: RelationType.R019,
    RelationType.R020i: RelationType.R020,
    RelationType.R021i: RelationType.R021,
    RelationType.R024i: RelationType.R024,
    RelationType.R025i: RelationType.R025,
    RelationType.R026i: RelationType.R026,
    RelationType.R027i: RelationType.R027,
    RelationType.R028i: RelationType.R028,
    RelationType.R029i: RelationType.R029,
    RelationType.R030i: RelationType.R030,
    RelationType.R031i: RelationType.R031,
    RelationType.R032i: RelationType.R032,
    RelationType.R033i: RelationType.R033,
    RelationType.R036i: RelationType.R036,
    RelationType.R037i: RelationType.R037,
    RelationType.R038i: RelationType.R038,
    RelationType.R039i: RelationType.R039,
    RelationType.R040i: RelationType.R040,
    RelationType.R041i: RelationType.R041,
    RelationType.R042i: RelationType.R042,
    RelationType.R045i: RelationType.R045,
    RelationType.R050i: RelationType.R050,
    RelationType.R053i: RelationType.R053,
    RelationType.R054i: RelationType.R054,
    RelationType.R055i: RelationType.R055,
    RelationType.R056i: RelationType.R056,
    RelationType.R057i: RelationType.R057,
    RelationType.R058i: RelationType.R058,
    RelationType.R059i: RelationType.R059,
    RelationType.R060i: RelationType.R060,
    RelationType.R061i: RelationType.R061,
    RelationType.R062i: RelationType.R062,
    RelationType.R063i: RelationType.R063,
    RelationType.R064i: RelationType.R064,
    RelationType.R065i: RelationType.R065,
    RelationType.R066i: RelationType.R066,
    RelationType.R067i: RelationType.R067,
    RelationType.R068i: RelationType.R068,
    RelationType.R069i: RelationType.R069,
    RelationType.R070i: RelationType.R070,
    RelationType.R071i: RelationType.R071,
    RelationType.R072i: RelationType.R072,
    RelationType.R073i: RelationType.R073,
    RelationType.R074i: RelationType.R074,
    RelationType.R075i: RelationType.R075,
    RelationType.R076i: RelationType.R076,
    RelationType.R079i: RelationType.R079,
    RelationType.R080i: RelationType.R080,
    RelationType.R081i: RelationType.R081,
    RelationType.R082i: RelationType.R082,
    RelationType.R083i: RelationType.R083,
    RelationType.R084i: RelationType.R084,
    RelationType.R085i: RelationType.R085,
    RelationType.R086i: RelationType.R086,
    RelationType.R002: RelationType.R002i,
    RelationType.R003: RelationType.R003i,
    RelationType.R004: RelationType.R004i,
    RelationType.R005: RelationType.R005i,
    RelationType.R006: RelationType.R006i,
    RelationType.R007: RelationType.R007i,
    RelationType.R008: RelationType.R008i,
    RelationType.R009: RelationType.R009i,
    RelationType.R010: RelationType.R010i,
    RelationType.R011: RelationType.R011i,
    RelationType.R012: RelationType.R012i,
    RelationType.R013: RelationType.R013i,
    RelationType.R014: RelationType.R014i,
    RelationType.R015: RelationType.R015i,
    RelationType.R016: RelationType.R016i,
    RelationType.R017: RelationType.R017i,
    RelationType.R018: RelationType.R018i,
    RelationType.R019: RelationType.R019i,
    RelationType.R020: RelationType.R020i,
    RelationType.R021: RelationType.R021i,
    RelationType.R024: RelationType.R024i,
    RelationType.R025: RelationType.R025i,
    RelationType.R026: RelationType.R026i,
    RelationType.R027: RelationType.R027i,
    RelationType.R028: RelationType.R028i,
    RelationType.R029: RelationType.R029i,
    RelationType.R030: RelationType.R030i,
    RelationType.R031: RelationType.R031i,
    RelationType.R032: RelationType.R032i,
    RelationType.R033: RelationType.R033i,
    RelationType.R036: RelationType.R036i,
    RelationType.R037: RelationType.R037i,
    RelationType.R038: RelationType.R038i,
    RelationType.R039: RelationType.R039i,
    RelationType.R040: RelationType.R040i,
    RelationType.R041: RelationType.R041i,
    RelationType.R042: RelationType.R042i,
    RelationType.R045: RelationType.R045i,
    RelationType.R050: RelationType.R050i,
    RelationType.R053: RelationType.R053i,
    RelationType.R054: RelationType.R054i,
    RelationType.R055: RelationType.R055i,
    RelationType.R056: RelationType.R056i,
    RelationType.R057: RelationType.R057i,
    RelationType.R058: RelationType.R058i,
    RelationType.R059: RelationType.R059i,
    RelationType.R060: RelationType.R060i,
    RelationType.R061: RelationType.R061i,
    RelationType.R062: RelationType.R062i,
    RelationType.R063: RelationType.R063i,
    RelationType.R064: RelationType.R064i,
    RelationType.R065: RelationType.R065i,
    RelationType.R066: RelationType.R066i,
    RelationType.R067: RelationType.R067i,
    RelationType.R068: RelationType.R068i,
    RelationType.R069: RelationType.R069i,
    RelationType.R070: RelationType.R070i,
    RelationType.R071: RelationType.R071i,
    RelationType.R072: RelationType.R072i,
    RelationType.R073: RelationType.R073i,
    RelationType.R074: RelationType.R074i,
    RelationType.R075: RelationType.R075i,
    RelationType.R076: RelationType.R076i,
    RelationType.R079: RelationType.R079i,
    RelationType.R080: RelationType.R080i,
    RelationType.R081: RelationType.R081i,
    RelationType.R082: RelationType.R082i,
    RelationType.R083: RelationType.R083i,
    RelationType.R084: RelationType.R084i,
    RelationType.R085: RelationType.R085i,
    RelationType.R086: RelationType.R086i,
}
_narrow: dict[RelationType, list[RelationType]] = {
    RelationType.R001: [
        RelationType.R002,
        RelationType.R008,
        RelationType.R019,
        RelationType.R022,
        RelationType.R025,
        RelationType.R026,
        RelationType.R033,
        RelationType.R034,
        RelationType.R036,
        RelationType.R044,
        RelationType.R057,
        RelationType.R062,
        RelationType.R068,
        RelationType.R074,
    ],
    RelationType.R002: [
        RelationType.R003,
        RelationType.R004,
        RelationType.R005,
        RelationType.R006,
        RelationType.R007,
        RelationType.R024,
        RelationType.R085i,
    ],
    RelationType.R003: [],
    RelationType.R004: [],
    RelationType.R005: [],
    RelationType.R006: [],
    RelationType.R007: [],
    RelationType.R008: [
        RelationType.R009,
    ],
    RelationType.R009: [
        RelationType.R010,
        RelationType.R011,
        RelationType.R012,
        RelationType.R013,
        RelationType.R014,
        RelationType.R016,
    ],
    RelationType.R010: [],
    RelationType.R011: [],
    RelationType.R012: [],
    RelationType.R013: [],
    RelationType.R014: [
        RelationType.R015,
    ],
    RelationType.R015: [],
    RelationType.R016: [
        RelationType.R017,
    ],
    RelationType.R017: [
        RelationType.R018,
    ],
    RelationType.R018: [],
    RelationType.R019: [
        RelationType.R020,
        RelationType.R021,
    ],
    RelationType.R020: [],
    RelationType.R022: [
        RelationType.R003,
        RelationType.R003i,
        RelationType.R013,
        RelationType.R013i,
        RelationType.R023,
        RelationType.R024,
        RelationType.R024i,
    ],
    RelationType.R023: [
        RelationType.R010,
        RelationType.R010i,
        RelationType.R011,
        RelationType.R011i,
        RelationType.R012,
        RelationType.R012i,
    ],
    RelationType.R024: [],
    RelationType.R025: [],
    RelationType.R026: [
        RelationType.R027,
        RelationType.R028,
        RelationType.R031,
        RelationType.R032,
    ],
    RelationType.R027: [
        RelationType.R079,
    ],
    RelationType.R028: [
        RelationType.R029,
        RelationType.R030,
    ],
    RelationType.R029: [],
    RelationType.R030: [],
    RelationType.R031: [],
    RelationType.R032: [],
    RelationType.R033: [],
    RelationType.R034: [
        RelationType.R004,
        RelationType.R004i,
        RelationType.R035,
        RelationType.R014,
        RelationType.R014i,
    ],
    RelationType.R035: [],
    RelationType.R036: [
        RelationType.R037,
        RelationType.R038,
        RelationType.R040,
        RelationType.R041,
    ],
    RelationType.R037: [],
    RelationType.R038: [
        RelationType.R039,
    ],
    RelationType.R039: [],
    RelationType.R040: [],
    RelationType.R041: [
        RelationType.R042,
    ],
    RelationType.R042: [],
    RelationType.R043: [],
    RelationType.R044: [
        RelationType.R045,
        RelationType.R045i,
        RelationType.R046,
        RelationType.R016,
        RelationType.R016i,
        RelationType.R047,
        RelationType.R050,
        RelationType.R050i,
        RelationType.R051,
        RelationType.R054,
        RelationType.R054i,
        RelationType.R055,
        RelationType.R055i,
        RelationType.R056,
        RelationType.R056i,
    ],
    RelationType.R045: [
        RelationType.R005,
        RelationType.R041,
    ],
    RelationType.R046: [],
    RelationType.R047: [
        RelationType.R017,
        RelationType.R017i,
        RelationType.R048,
        RelationType.R049,
    ],
    RelationType.R048: [],
    RelationType.R049: [],
    RelationType.R050: [],
    RelationType.R051: [
        RelationType.R052,
        RelationType.R053,
        RelationType.R053i,
    ],
    RelationType.R052: [],
    RelationType.R053: [],
    RelationType.R054: [],
    RelationType.R055: [],
    RelationType.R056: [],
    RelationType.R057: [
        RelationType.R006,
        RelationType.R006i,
        RelationType.R058,
        RelationType.R061,
        RelationType.R084i,
    ],
    RelationType.R058: [
        RelationType.R059,
        RelationType.R060,
    ],
    RelationType.R059: [],
    RelationType.R060: [],
    RelationType.R061: [
        RelationType.R033i,
    ],
    RelationType.R062: [
        RelationType.R063,
        RelationType.R064,
        RelationType.R065,
        RelationType.R066,
        RelationType.R067,
    ],
    RelationType.R063: [],
    RelationType.R064: [],
    RelationType.R065: [],
    RelationType.R066: [],
    RelationType.R067: [],
    RelationType.R068: [
        RelationType.R069,
        RelationType.R071,
        RelationType.R073,
        RelationType.R084,
        RelationType.R085,
        RelationType.R085i,
        RelationType.R086,
    ],
    RelationType.R069: [
        RelationType.R070,
        RelationType.R080,
        RelationType.R081,
        RelationType.R082,
    ],
    RelationType.R070: [],
    RelationType.R071: [
        RelationType.R072,
    ],
    RelationType.R072: [],
    RelationType.R073: [],
    RelationType.R074: [
        RelationType.R007,
        RelationType.R007i,
        RelationType.R075,
        RelationType.R076,
        RelationType.R077,
        RelationType.R078,
    ],
    RelationType.R075: [],
    RelationType.R076: [],
    RelationType.R077: [],
    RelationType.R078: [],
    RelationType.R079: [],
    RelationType.R080: [],
    RelationType.R081: [],
    RelationType.R082: [
        RelationType.R083,
    ],
    RelationType.R083: [],
    RelationType.R084: [],
    RelationType.R085: [],
    RelationType.R086: [],
}
_broad: dict[RelationType, list[RelationType]] = {
    RelationType.R002: [RelationType.R001],
    RelationType.R003: [RelationType.R002, RelationType.R022],
    RelationType.R003i: [RelationType.R022],
    RelationType.R004: [RelationType.R002, RelationType.R034],
    RelationType.R004i: [RelationType.R034],
    RelationType.R005: [RelationType.R002, RelationType.R045],
    RelationType.R006: [RelationType.R002, RelationType.R057],
    RelationType.R006i: [RelationType.R057],
    RelationType.R007: [RelationType.R002, RelationType.R074],
    RelationType.R007i: [RelationType.R074],
    RelationType.R008: [RelationType.R001],
    RelationType.R009: [RelationType.R008],
    RelationType.R010: [RelationType.R009, RelationType.R023],
    RelationType.R010i: [RelationType.R023],
    RelationType.R011: [RelationType.R009, RelationType.R023],
    RelationType.R011i: [RelationType.R023],
    RelationType.R012: [RelationType.R009, RelationType.R023],
    RelationType.R012i: [RelationType.R023],
    RelationType.R013: [RelationType.R009, RelationType.R022],
    RelationType.R013i: [RelationType.R022],
    RelationType.R014: [RelationType.R009, RelationType.R034],
    RelationType.R014i: [RelationType.R034],
    RelationType.R015: [RelationType.R014],
    RelationType.R016: [RelationType.R009, RelationType.R044],
    RelationType.R016i: [RelationType.R044],
    RelationType.R017: [RelationType.R016, RelationType.R047],
    RelationType.R017i: [RelationType.R047],
    RelationType.R018: [RelationType.R017],
    RelationType.R019: [RelationType.R001],
    RelationType.R020: [RelationType.R019],
    RelationType.R021: [RelationType.R019],
    RelationType.R022: [RelationType.R001],
    RelationType.R023: [RelationType.R022],
    RelationType.R024: [RelationType.R002, RelationType.R022],
    RelationType.R024i: [RelationType.R022],
    RelationType.R025: [RelationType.R001],
    RelationType.R026: [RelationType.R001],
    RelationType.R027: [RelationType.R026],
    RelationType.R028: [RelationType.R026],
    RelationType.R029: [RelationType.R028],
    RelationType.R030: [RelationType.R028],
    RelationType.R031: [RelationType.R026],
    RelationType.R032: [RelationType.R026],
    RelationType.R033: [RelationType.R001],
    RelationType.R033i: [RelationType.R061],
    RelationType.R034: [RelationType.R001],
    RelationType.R035: [RelationType.R034],
    RelationType.R036: [RelationType.R001],
    RelationType.R037: [RelationType.R036],
    RelationType.R038: [RelationType.R036],
    RelationType.R039: [RelationType.R038],
    RelationType.R040: [RelationType.R036],
    RelationType.R041: [RelationType.R036, RelationType.R045],
    RelationType.R042: [RelationType.R041],
    RelationType.R044: [RelationType.R001],
    RelationType.R045: [RelationType.R044],
    RelationType.R045i: [RelationType.R044],
    RelationType.R046: [RelationType.R044],
    RelationType.R047: [RelationType.R044],
    RelationType.R048: [RelationType.R047],
    RelationType.R049: [RelationType.R047],
    RelationType.R050: [RelationType.R044],
    RelationType.R050i: [RelationType.R044],
    RelationType.R051: [RelationType.R044],
    RelationType.R052: [RelationType.R051],
    RelationType.R053: [RelationType.R051],
    RelationType.R053i: [RelationType.R051],
    RelationType.R054: [RelationType.R044],
    RelationType.R054i: [RelationType.R044],
    RelationType.R055: [RelationType.R044],
    RelationType.R055i: [RelationType.R044],
    RelationType.R056: [RelationType.R044],
    RelationType.R056i: [RelationType.R044],
    RelationType.R057: [RelationType.R001],
    RelationType.R058: [RelationType.R057],
    RelationType.R059: [RelationType.R058],
    RelationType.R060: [RelationType.R058],
    RelationType.R061: [RelationType.R057],
    RelationType.R062: [RelationType.R001],
    RelationType.R063: [RelationType.R062],
    RelationType.R064: [RelationType.R062],
    RelationType.R065: [RelationType.R062],
    RelationType.R066: [RelationType.R062],
    RelationType.R067: [RelationType.R062],
    RelationType.R068: [RelationType.R001],
    RelationType.R069: [RelationType.R068],
    RelationType.R070: [RelationType.R069],
    RelationType.R071: [RelationType.R068],
    RelationType.R072: [RelationType.R071],
    RelationType.R073: [RelationType.R068],
    RelationType.R074: [RelationType.R001],
    RelationType.R075: [RelationType.R074],
    RelationType.R076: [RelationType.R074],
    RelationType.R077: [RelationType.R074],
    RelationType.R078: [RelationType.R074],
    RelationType.R079: [RelationType.R027],
    RelationType.R080: [RelationType.R069],
    RelationType.R081: [RelationType.R069],
    RelationType.R082: [RelationType.R069],
    RelationType.R083: [RelationType.R082],
    RelationType.R084: [RelationType.R068],
    RelationType.R084i: [RelationType.R057],
    RelationType.R085: [RelationType.R068],
    RelationType.R085i: [RelationType.R002, RelationType.R068],
    RelationType.R086: [RelationType.R068],
}


@dataclass
class Relation:
    certainty_of_relation: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#relationCertainty
    date_of_relation: FreeText | ModelBasedText | RuleBasedText  # RA02
    description_of_relation: FreeText  # RA03
    identifier_of_relation: FreeText | ModelBasedText | RuleBasedText  # RA04
    source_of_relation: FreeText | ModelBasedText  # https://www.ica.org/standards/RiC/ontology#relationSource
    place_of_relation: str  # RA06

    relation_type: RelationType
    domain_type: things.EntityDomain | Literal["Relation"]
    domain_identifier: str
    target_type: things.EntityDomain | Literal["Relation"]
    target_identifier: str
