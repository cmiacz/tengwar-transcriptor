# -*- coding: utf-8 -*-


class TengwarDescription(object):

    consonansts = [
        u"т", u"п", u"-", u"к",
        u"д", u"б", u"-", u"г",
        u"ц", u"-", u"ч", u"-",
        u"-", u"-", u"дж", u"-",
        u"с", u"ф", u"ш", u"-",
        u"з", u"в", u"ж", u"х",
        u"н", u"м", u"-", u"-",
        u"-", u"-", u"й", u"-",
        u"р", u"-", u"л", u"-",
    ]

    vowels = [
        u"а", u"э/е", u"и", u"о", u"у", u"ы"
    ]

    palatalization = [
        u"я", u"е", u"-", u"ё", u"ю", u"ь", u"ъ"
    ]


charset = u"а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я"


transcription_map = [
    (u"а", u"a"),
    (u"б", u"b"),
    (u"в", u"v"),
    (u"г", u"g"),
    (u"д", u"d"),
    (u"е", u"je"),
    (u"ё", u"jo"),
    (u"ж", u"ž"),
    (u"з", u"z"),
    (u"и", u"i"),
    (u"й", u"j"),
    (u"к", u"k"),
    (u"л", u"l"),
    (u"м", u"m"),
    (u"н", u"n"),
    (u"о", u"o"),
    (u"п", u"p"),
    (u"р", u"r"),
    (u"с", u"s"),
    (u"т", u"t"),
    (u"у", u"u"),
    (u"ф", u"f"),
    (u"х", u"x"),
    (u"ц", u"c"),
    (u"ч", u"č"),
    (u"ш", u"š"),
    (u"щ", u"šč"),
    (u"ъ", u"’"),
    (u"ы", u"y"),
    (u"ь", u"´"),
    (u"э", u"e"),
    (u"ю", u"ju"),
    (u"я", u"ja"),

    (u"lje", u"le"),
    (u"žje", u"že"),
    (u"cje", u"ce"),
    (u"čje", u"če"),
    (u"šje", u"še"),

    (u"dž", u"ʤ"),
]
