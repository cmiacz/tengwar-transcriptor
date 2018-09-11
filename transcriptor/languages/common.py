# -*- coding: utf-8 -*-


class TengwarDescription(object):

    consonansts = [
        u"t  т",
        u"p  п",
        u"ť  ћ",
        u"k  к",
        u"d  д",
        u"b  б",
        u"ď  ђ",
        u"g  г / ґ",
        u"c  ц",
        u"-",
        u"č / cz  ч",
        u"-",
        u"dz  ѕ",
        u"-",
        u"dž / dż  џ",
        u"-",
        u"s  с",
        u"f  ф",
        u"š / sz  ш",
        u"h  г",
        u"z  з",
        u"v / w  в",
        u"ž / ż  ж",
        u"ch  х",
        u"n  н",
        u"m  м",
        u"ň  њ",
        u"-",
        u"-",
        u"u  ў",
        u"j  й",
        u"-",
        u"r  р",
        u"ř  -",
        u"l / ł  л",
        u"ľ / l  љ",
    ]

    vowels = [
        u"a  а",
        u"e  е / э",
        u"i  и / i",
        u"o  о",
        u"u  y",
        u"y  ы / и"
    ]

    long_vowels = [
        u"á", u"é", u"í", u"ó", u"ú", u"ý"
    ]

    palatalization = [
        u"ja  я",
        u"je  е / є",
        u"ji  ї",
        u"jo  ë",
        u"ju  ю",
        u"´  ь",
        u"’  ъ",
    ]

    additional = [
        (u"`ë", u"ę"),
        (u"~ë", u"ą"),
    ]


transcription_map = []
