# -*- coding: utf-8 -*-


class TengwarDescription(object):

    consonansts = [
        u"t", u"p", u"ť", u"k",
        u"d", u"b", u"ď", u"g",
        u"c", u"-", u"č", u"-",
        u"dz", u"-", u"dž", u"-",
        u"s", u"f", u"š", u"h",
        u"z", u"v", u"ž", u"ch",
        u"n", u"m", u"ň", u"-",
        u"-", u"u", u"j", u"-",
        u"r", u"ř", u"l", u"ľ",
    ]

    vowels = [
        u"a", u"e", u"i", u"o", u"u", u"y"
    ]

    long_vowels = [
        u"á", u"é", u"í", u"ó", u"ú / ů", u"ý"
    ]

    additional = [
        (u"hR", u"ě"),
    ]


charset = u"a á b c č d ď e é ě f g h ch i í j k l m n ň o ó p q r ř s t ť u ú ů v w x y ý z ž"


transcription_map = [
    (u"qu", u"kŭ"),
    (u"q", u"k"),
    (u"wh", u"ŭ"),
    (u"ph", u"f"),
    (u"w", u"v"),
    (u"x", u"ks"),

    (u"ě", u"je"),
    (u"ů", u"ú"),

    (u"au", u"aŭ"),
    (u"eu", u"eŭ"),
    (u"ou", u"oŭ"),

    (u"ch", u"x"),
    (u"dz", u"ʣ"),
    (u"dž", u"ʤ"),
]
