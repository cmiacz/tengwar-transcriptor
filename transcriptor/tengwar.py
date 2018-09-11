# -*- coding: utf-8 -*-


LEFT = 0
CENTER = 1
RIGHT = 2
SEPARATE = 3
SPECIAL = 4


class Character(object):

    def __init__(self, variants, upper_tehta_pos, lower_tehta_pos):
        self.variants = variants
        self.upper_tehta_pos = upper_tehta_pos
        self.lower_tehta_pos = lower_tehta_pos

    def get_variant(self, previous_character):
        return self.variants[0]


class Tengwar(Character):

    def __init__(self, variant, upper_tehta_pos=SEPARATE, lower_tehta_pos=SEPARATE):
        Character.__init__(self, (variant,), upper_tehta_pos, lower_tehta_pos)


class UpperTehta(Character):

    def __init__(self, *variants):
        Character.__init__(self, variants, upper_tehta_pos=SEPARATE, lower_tehta_pos=SEPARATE)

    def get_variant(self, previous_character):
        return self.variants[previous_character.upper_tehta_pos]


class LowerTehta(Character):

    def __init__(self, *variants):
        Character.__init__(self, variants, upper_tehta_pos=SEPARATE, lower_tehta_pos=SEPARATE)

    def get_variant(self, previous_character):
        return self.variants[previous_character.lower_tehta_pos]


none_tengwar = Tengwar(u"")


tengwar_map = {
    u"t": Tengwar(u"1", CENTER, RIGHT),
    u"p": Tengwar(u"q", CENTER, RIGHT),
    u"ť": Tengwar(u"a", CENTER, LEFT),
    u"k": Tengwar(u"z", CENTER, LEFT),

    u"d": Tengwar(u"2", CENTER, CENTER),
    u"b": Tengwar(u"w", CENTER, CENTER),
    u"ď": Tengwar(u"s", CENTER, CENTER),
    u"g": Tengwar(u"x", CENTER, CENTER),

    u"c": Tengwar(u"!", RIGHT, RIGHT),
    u"č": Tengwar(u"A", LEFT, LEFT),

    u"ʣ": Tengwar(u"@", CENTER, CENTER),
    u"ʤ": Tengwar(u"S", LEFT, LEFT),

    u"s": Tengwar(u"3", RIGHT, CENTER),
    u"f": Tengwar(u"e", RIGHT, CENTER),
    u"š": Tengwar(u"d", LEFT, CENTER),
    u"x": Tengwar(u"c", LEFT, CENTER),

    u"z": Tengwar(u"4", CENTER, CENTER),
    u"v": Tengwar(u"r", CENTER, CENTER),
    u"ž": Tengwar(u"f", LEFT, CENTER),
    u"h": Tengwar(u"v", LEFT, CENTER),

    u"n": Tengwar(u"5", LEFT, LEFT),
    u"m": Tengwar(u"t", LEFT, LEFT),
    u"ň": Tengwar(u"g", LEFT, LEFT),

    u"ŭ": Tengwar(u"y", CENTER, CENTER),
    u"j": Tengwar(u"h", CENTER, CENTER),

    u"l": Tengwar(u"j", CENTER, SPECIAL),
    u"ľ": Tengwar(u"m", CENTER, SPECIAL),

    u"r": Tengwar(u"7", CENTER, SPECIAL),
    u"ř": Tengwar(u"u", CENTER, SPECIAL),

    u"a": UpperTehta(u"#", u"E", u"D", u"`C", u"C"),
    u"e": UpperTehta(u"$", u"R", u"F", u"`V", u"V"),
    u"ę": UpperTehta(u"è", u"é", u"ê", u"`ë", u"ë"),
    u"i": UpperTehta(u"%", u"T", u"G", u"`B", u"B"),
    u"o": UpperTehta(u"^", u"Y", u"H", u"`N", u"N"),
    u"u": UpperTehta(u"&", u"U", u"J", u"`M", u"M"),
    u"y": UpperTehta(u"Ô", u"Õ", u"Ö", u"`×", u"×"),
    u"´": LowerTehta(u"È", u"É", u"Ê", u"`Ë", u"L"),
    u"’": LowerTehta(u"Ì", u"Í", u"Î", u"`Ï", u"Ï"),

    u"á": Tengwar(u"~C"),
    u"ą": Tengwar(u"~ë"),
    u"é": Tengwar(u"~V"),
    u"í": Tengwar(u"~B"),
    u"ó": Tengwar(u"~N"),
    u"ú": Tengwar(u"~M"),
    u"ý": Tengwar(u"~×"),

    u"0": Tengwar(u"ð"),
    u"1": Tengwar(u"ñ"),
    u"2": Tengwar(u"ò"),
    u"3": Tengwar(u"ó"),
    u"4": Tengwar(u"ô"),
    u"5": Tengwar(u"õ"),
    u"6": Tengwar(u"ö"),
    u"7": Tengwar(u"÷"),
    u"8": Tengwar(u"ø"),
    u"9": Tengwar(u"ù"),

    u",": Tengwar(u"="),
    u".": Tengwar(u"--"),
    u"-": Tengwar(u"-"),
    u";": Tengwar(u"-"),
    u":": Tengwar(u"-"),
    u"?": Tengwar(u"À"),
    u"!": Tengwar(u"Á"),
    u'"': Tengwar(u"«"),
    u"(": Tengwar(u"›"),
    u"[": Tengwar(u"›"),
    u"{": Tengwar(u"›"),
    u")": Tengwar(u"›"),
    u"]": Tengwar(u"›"),
    u"}": Tengwar(u"›"),
}


def convert_to_tengwar(word):
    result = []
    prev = none_tengwar
    for char in word:
        tengwar = tengwar_map.get(char, none_tengwar)
        result.append(tengwar.get_variant(prev))
        prev = tengwar
    return "".join(result)


class TengwarTable(object):

    consonansts = [
        u"1", u"q", u"a", u"z",  # u"T",  u"P", u"Ť",  u"K",
        u"2", u"w", u"s", u"x",  # u"D",  u"B", u"Ď",  u"G",
        u"!", u"Q", u"A", u"Z",  # u"C",  u"-", u"Č",  u"-",
        u"@", u"W", u"S", u"X",  # u"DZ", u"-", u"DŽ", u"-",
        u"3", u"e", u"d", u"c",  # u"S",  u"F", u"Š",  u"H",
        u"4", u"r", u"f", u"x",  # u"Z",  u"V", u"Ž",  u"CH",
        u"5", u"t", u"g", u"b",  # u"N",  u"M", u"Ň",  u"-",
        u"6", u"y", u"h", u"n",  # u"-",  u"U", u"J",  u"-",
        u"7", u"u", u"j", u"m",  # u"R",  u"Ř", u"L",  u"Ľ",
    ]

    vowels = [
        u"`C", u"`V", u"`B", u"`N", u"`M", u"`×"  # u"A", u"E", u"I", u"O", u"U", u"Y"
    ]

    long_vowels = [
        u"~C", u"~V", u"~B", u"~N", u"~M", u"~×"  # u"Á", u"É", u"Í", u"Ó", u"Ú", u"Ý"
    ]

    palatalization = [
        u"hE", u"hR", u"hT", u"hY", u"hU", u"`Ë", u"`Ï"  # u"JA", u"JE", u"JI", u"JO", u"JU", u"Ь", u"Ъ"
    ]
