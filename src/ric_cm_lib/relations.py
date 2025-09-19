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
    """
    :ivar R001: is related to
    :ivar R002: has or had part
    :ivar R002i: is or was part of
    :ivar R003: has or had constituent
    :ivar R003i: is or was constituent of
    :ivar R004: has or had component
    :ivar R004i: is or was component of
    :ivar R005: has or had subdivision
    :ivar R005i: is or was subdivision of
    :ivar R006: has or had subevent
    :ivar R006i: is or was subevent of
    :ivar R007: contains or contained
    :ivar R007i: is or was contained by
    :ivar R008: precedes or preceded
    :ivar R008i: follows or followed
    :ivar R009: precedes in time
    :ivar R009i: follows in time
    :ivar R010: is original of
    :ivar R010i: has original
    :ivar R011: is draft of
    :ivar R011i: has draft
    :ivar R012: has copy
    :ivar R012i: is copy of
    :ivar R013: has reply
    :ivar R013i: is reply to
    :ivar R014: has or had derived instantiation
    :ivar R014i: is or was derived from instantiation
    :ivar R015: migrated into
    :ivar R015i: migrated from
    :ivar R016: has successor
    :ivar R016i: is successor of
    :ivar R017: has descendant
    :ivar R017i: has ancestor
    :ivar R018: has child
    :ivar R018i: is child of
    :ivar R019: has or had subject
    :ivar R019i: is or was subject of
    :ivar R020: has or had main subject
    :ivar R020i: is or was main subject of
    :ivar R021: describes or described
    :ivar R021i: is or was described by
    :ivar R022: is record resource associated with record resource
    :ivar R023: has genetic link to record resource
    :ivar R024: includes or included
    :ivar R024i: is or was included in
    :ivar R025: has or had instantiation
    :ivar R025i: is or was instantiation of
    :ivar R026: has provenance
    :ivar R026i: is provenance of
    :ivar R027: has creator
    :ivar R027i: is creator of
    :ivar R028: has accumulator
    :ivar R028i: is accumulator of
    :ivar R029: has receiver
    :ivar R029i: is receiver of
    :ivar R030: has collector
    :ivar R030i: is collector of
    :ivar R031: has sender
    :ivar R031i: is sender of
    :ivar R032: has addressee
    :ivar R032i: is addressee of
    :ivar R033: documents
    :ivar R033i: documented by
    :ivar R034: is instantiation associated with instantiation
    :ivar R035: is functionally equivalent to
    :ivar R036: has or had authority over
    :ivar R036i: is or was under authority of
    :ivar R037: is or was owner of
    :ivar R037i: has or had owner
    :ivar R038: is or was manager of
    :ivar R038i: has or had manager
    :ivar R039: is or was holder of
    :ivar R039i:  has or had holder
    :ivar R040: is or was holder of intellectual property rights of
    :ivar R040i: has or had intellectual property rights holder
    :ivar R041: is or was controller of
    :ivar R041i: has or had controller
    :ivar R042: is or was leader of
    :ivar R042i: has or had leader
    :ivar R044: is agent associated with agent
    :ivar R045: has or had subordinate
    :ivar R045i: is or was subordinate to
    :ivar R046: has or had work relation with
    :ivar R047: has family association with
    :ivar R048: has sibling
    :ivar R049: has or had spouse
    :ivar R050: knows of
    :ivar R050i: known by
    :ivar R051: knows
    :ivar R052: has or had correspondent
    :ivar R053: has or had teacher
    :ivar R053i: has or had student
    :ivar R054: occupies or occupied
    :ivar R054i: is or was occupied by
    :ivar R055: has or had member
    :ivar R055i: is or was member of
    :ivar R056: exists or existed in
    :ivar R056i: has or had position
    :ivar R057: is event associated with
    :ivar R057i: is associated with event
    :ivar R058: has or had participant
    :ivar R058i: is or was participant in
    :ivar R059: affects or affected
    :ivar R059i: is or was affected by
    :ivar R060: is or was performed by
    :ivar R060i: performs or performed
    :ivar R061: results or resulted in
    :ivar R061i: results or resulted from
    :ivar R062: is rule associated with
    :ivar R062i: is associated with rule
    :ivar R063: regulates or regulated
    :ivar R063i: is or was regulated by
    :ivar R064: is or was expressed by
    :ivar R064i: expresses or expressed
    :ivar R065: issued by
    :ivar R065i: is responsible for issuing
    :ivar R066: is or was enforced by
    :ivar R066i: is or was responsible for enforcing
    :ivar R067: authorizes
    :ivar R067i: authorized by
    :ivar R068: is date associated with
    :ivar R068i: is associated with date
    :ivar R069: is beginning date of
    :ivar R069i: has beginning date
    :ivar R070: is birth date of
    :ivar R070i: has birth date
    :ivar R071: is end date of
    :ivar R071i: has end date
    :ivar R072: is death date of
    :ivar R072i: has death date
    :ivar R073: is modification date of
    :ivar R073i: has modification date
    :ivar R074: is place associated with
    :ivar R074i: is associated with place
    :ivar R075: is or was location of
    :ivar R075i: has or had location
    :ivar R076: is or was jurisdiction of
    :ivar R076i: has or had jurisdiction
    :ivar R077: is or was adjacent to
    :ivar R078: overlaps or overlapped
    :ivar R079: has author
    :ivar R079i: is author of
    :ivar R080: is creation date of
    :ivar R080i: has creation date
    :ivar R081: is or was creation date of all members of
    :ivar R081i: has or had all members with creation date
    :ivar R082: is or was creation date of some members of
    :ivar R082i: has or had some members with creation date
    :ivar R083: is or was creation date of most members of
    :ivar R083i: has or had most members with creation date
    :ivar R084: is date of occurrence of
    :ivar R084i: occurred at date
    :ivar R085: is within
    :ivar R085i: has within
    :ivar R086: intersects
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

    @property
    def inverse(self) -> "RelationType":
        return _inverse.get(self, self)

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

    @property
    def label(self) -> str:
        return _labels[self]


_labels: dict[RelationType, str] = {
    RelationType.R001: "is related to",
    RelationType.R002: "has or had part",
    RelationType.R002i: "is or was part of",
    RelationType.R003: "has or had constituent",
    RelationType.R003i: "is or was constituent of",
    RelationType.R004: "has or had component",
    RelationType.R004i: "is or was component of",
    RelationType.R005: "has or had subdivision",
    RelationType.R005i: "is or was subdivision of",
    RelationType.R006: "has or had subevent",
    RelationType.R006i: "is or was subevent of",
    RelationType.R007: "contains or contained",
    RelationType.R007i: "is or was contained by",
    RelationType.R008: "precedes or preceded",
    RelationType.R008i: "follows or followed",
    RelationType.R009: "precedes in time",
    RelationType.R009i: "follows in time",
    RelationType.R010: "is original of",
    RelationType.R010i: "has original",
    RelationType.R011: "is draft of",
    RelationType.R011i: "has draft",
    RelationType.R012: "has copy",
    RelationType.R012i: "is copy of",
    RelationType.R013: "has reply",
    RelationType.R013i: "is reply to",
    RelationType.R014: "has or had derived instantiation",
    RelationType.R014i: "is or was derived from instantiation",
    RelationType.R015: "migrated into",
    RelationType.R015i: "migrated from",
    RelationType.R016: "has successor",
    RelationType.R016i: "is successor of",
    RelationType.R017: "has descendant",
    RelationType.R017i: "has ancestor",
    RelationType.R018: "has child",
    RelationType.R018i: "is child of",
    RelationType.R019: "has or had subject",
    RelationType.R019i: "is or was subject of",
    RelationType.R020: "has or had main subject",
    RelationType.R020i: "is or was main subject of",
    RelationType.R021: "describes or described",
    RelationType.R021i: "is or was described by",
    RelationType.R022: "is record resource associated with record resource",
    RelationType.R023: "has genetic link to record resource",
    RelationType.R024: "includes or included",
    RelationType.R024i: "is or was included in",
    RelationType.R025: "has or had instantiation",
    RelationType.R025i: "is or was instantiation of",
    RelationType.R026: "has provenance",
    RelationType.R026i: "is provenance of",
    RelationType.R027: "has creator",
    RelationType.R027i: "is creator of",
    RelationType.R028: "has accumulator",
    RelationType.R028i: "is accumulator of",
    RelationType.R029: "has receiver",
    RelationType.R029i: "is receiver of",
    RelationType.R030: "has collector",
    RelationType.R030i: "is collector of",
    RelationType.R031: "has sender",
    RelationType.R031i: "is sender of",
    RelationType.R032: "has addressee",
    RelationType.R032i: "is addressee of",
    RelationType.R033: "documents",
    RelationType.R033i: "documented by",
    RelationType.R034: "is instantiation associated with instantiation",
    RelationType.R035: "is functionally equivalent to",
    RelationType.R036: "has or had authority over",
    RelationType.R036i: "is or was under authority of",
    RelationType.R037: "is or was owner of",
    RelationType.R037i: "has or had owner",
    RelationType.R038: "is or was manager of",
    RelationType.R038i: "has or had manager",
    RelationType.R039: "is or was holder of",
    RelationType.R039i: " has or had holder",
    RelationType.R040: "is or was holder of intellectual property rights of",
    RelationType.R040i: "has or had intellectual property rights holder",
    RelationType.R041: "is or was controller of",
    RelationType.R041i: "has or had controller",
    RelationType.R042: "is or was leader of",
    RelationType.R042i: "has or had leader",
    RelationType.R044: "is agent associated with agent",
    RelationType.R045: "has or had subordinate",
    RelationType.R045i: "is or was subordinate to",
    RelationType.R046: "has or had work relation with",
    RelationType.R047: "has family association with",
    RelationType.R048: "has sibling",
    RelationType.R049: "has or had spouse",
    RelationType.R050: "knows of",
    RelationType.R050i: "known by",
    RelationType.R051: "knows",
    RelationType.R052: "has or had correspondent",
    RelationType.R053: "has or had teacher",
    RelationType.R053i: "has or had student",
    RelationType.R054: "occupies or occupied",
    RelationType.R054i: "is or was occupied by",
    RelationType.R055: "has or had member",
    RelationType.R055i: "is or was member of",
    RelationType.R056: "exists or existed in",
    RelationType.R056i: "has or had position",
    RelationType.R057: "is event associated with",
    RelationType.R057i: "is associated with event",
    RelationType.R058: "has or had participant",
    RelationType.R058i: "is or was participant in",
    RelationType.R059: "affects or affected",
    RelationType.R059i: "is or was affected by",
    RelationType.R060: "is or was performed by",
    RelationType.R060i: "performs or performed",
    RelationType.R061: "results or resulted in",
    RelationType.R061i: "results or resulted from",
    RelationType.R062: "is rule associated with",
    RelationType.R062i: "is associated with rule",
    RelationType.R063: "regulates or regulated",
    RelationType.R063i: "is or was regulated by",
    RelationType.R064: "is or was expressed by",
    RelationType.R064i: "expresses or expressed",
    RelationType.R065: "issued by",
    RelationType.R065i: "is responsible for issuing",
    RelationType.R066: "is or was enforced by",
    RelationType.R066i: "is or was responsible for enforcing",
    RelationType.R067: "authorizes",
    RelationType.R067i: "authorized by",
    RelationType.R068: "is date associated with",
    RelationType.R068i: "is associated with date",
    RelationType.R069: "is beginning date of",
    RelationType.R069i: "has beginning date",
    RelationType.R070: "is birth date of",
    RelationType.R070i: "has birth date",
    RelationType.R071: "is end date of",
    RelationType.R071i: "has end date",
    RelationType.R072: "is death date of",
    RelationType.R072i: "has death date",
    RelationType.R073: "is modification date of",
    RelationType.R073i: "has modification date",
    RelationType.R074: "is place associated with",
    RelationType.R074i: "is associated with place",
    RelationType.R075: "is or was location of",
    RelationType.R075i: "has or had location",
    RelationType.R076: "is or was jurisdiction of",
    RelationType.R076i: "has or had jurisdiction",
    RelationType.R077: "is or was adjacent to",
    RelationType.R078: "overlaps or overlapped",
    RelationType.R079: "has author",
    RelationType.R079i: "is author of",
    RelationType.R080: "is creation date of",
    RelationType.R080i: "has creation date",
    RelationType.R081: "is or was creation date of all members of",
    RelationType.R081i: "has or had all members with creation date",
    RelationType.R082: "is or was creation date of some members of",
    RelationType.R082i: "has or had some members with creation date",
    RelationType.R083: "is or was creation date of most members of",
    RelationType.R083i: "has or had most members with creation date",
    RelationType.R084: "is date of occurrence of",
    RelationType.R084i: "occurred at date",
    RelationType.R085: "is within",
    RelationType.R085i: "has within",
    RelationType.R086: "intersects",
}
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
