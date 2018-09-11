# -*- coding: utf-8 -*-


class TengwarDescription(object):

    consonansts = [
        u"т  t", u"п  p", u"ћ  ć", u"к  k",
        u"д  d", u"б  b", u"ђ  đ", u"г  g",
        u"ц  c", u"-", u"ч  č", u"-",
        u"-", u"-", u"џ  dž", u"-",
        u"с  s", u"ф  f", u"ш  š", u"-",
        u"з  z", u"в  v", u"ж  ž", u"х  h",
        u"н  n", u"м  m", u"њ  nj", u"-",
        u"-", u"-", u"j  j", u"-",
        u"р  r", u"-", u"л  l", u"љ  lj",
    ]

    vowels = [
        u"а  a", u"е  e", u"и  i", u"о  o", u"y  u"
    ]


charset = u"а б в г д ђ е ж з и ј к л љ м н њ о п р с т ћ у ф х ц ч џ ш"


transcription_map = [
    (u"а", u"a"),
    (u"б", u"b"),
    (u"в", u"v"),
    (u"г", u"g"),
    (u"д", u"d"),
    (u"ђ", u"ď"),
    (u"е", u"e"),
    (u"ж", u"ž"),
    (u"з", u"z"),
    (u"и", u"i"),
    (u"ј", u"j"),
    (u"к", u"k"),
    (u"л", u"l"),
    (u"љ", u"ľ"),
    (u"м", u"m"),
    (u"н", u"n"),
    (u"њ", u"ň"),
    (u"о", u"o"),
    (u"п", u"p"),
    (u"р", u"r"),
    (u"с", u"s"),
    (u"т", u"t"),
    (u"ћ", u"ť"),
    (u"у", u"u"),
    (u"ф", u"f"),
    (u"х", u"x"),
    (u"ц", u"c"),
    (u"ч", u"č"),
    (u"џ", u"ʤ"),
    (u"ш", u"š"),

    (u"ć", u"ť"),
    (u"đ", u"ď"),
    (u"h", u"x"),
    (u"dž", u"ʤ"),
    (u"lj", u"ľ"),
    (u"nj", u"ň"),
]
