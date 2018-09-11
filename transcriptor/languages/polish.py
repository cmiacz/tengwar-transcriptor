# -*- coding: utf-8 -*-


class TengwarDescription(object):

    consonansts = [
        u"t", u"p", u"-", u"k",
        u"d", u"b", u"-", u"g",
        u"c", u"-", u"cz", u"-",
        u"dz", u"-", u"dż", u"-",
        u"s", u"f", u"sz", u"h",
        u"z", u"w", u"ż", u"ch",
        u"n", u"m", u"-", u"-",
        u"-", u"u", u"j / i", u"-",
        u"r", u"rz", u"ł", u"l",
    ]

    vowels = [
        u"a", u"e", u"i", u"o", u"u", u"y"
    ]

    palatalization = [
        u"ja / ia", u"je / ie", u"ji", u"jo / io", u"ju / iu", u"´ (ć ń ś ź)"
    ]

    additional = [
        (u"`ë", u"ę"), (u"~ë", u"ą"), (u"~M", u"ó"),
    ]


charset = u"a ą b c ch cz ć d dz dż e ę f g h i j k l ł m n ń o ó p r rz s sz ś t u w y z ź ż"


transcription_map = [
    (u"qu", u"kŭ"),
    (u"q", u"k"),
    (u"wh", u"ŭ"),
    (u"ph", u"f"),
    (u"w", u"v"),
    (u"x", u"ks"),

    (u"au", u"aŭ"),
    (u"eu", u"eŭ"),
    (u"ou", u"oŭ"),

    (u"cj", u"c’j"),
    (u"nj", u"n’j"),
    (u"sj", u"s’j"),
    (u"zj", u"z’j"),

    (u"ć", u"c´"),
    (u"ś", u"s´"),
    (u"ź", u"z´"),
    (u"ń", u"n´"),

    (u"ia", u"ja"),
    (u"ią", u"ją"),
    (u"ie", u"je"),
    (u"ię", u"ję"),
    (u"io", u"jo"),
    (u"iu", u"ju"),
    (u"ió", u"jó"),

    (u"ch", u"x"),
    (u"cz", u"č"),
    (u"dz", u"ʣ"),
    (u"dż", u"ʤ"),
    (u"sz", u"š"),
    (u"rz", u"ř"),
    (u"ż", u"ž"),
    (u"ó", u"ú"),

    (u"l", u"ľ"),
    (u"ł", u"l"),
]
