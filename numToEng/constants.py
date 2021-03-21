NEGATIVE = 'negative'
ZERO = 'zero'
AND = 'and'
TEEN_EXCEPTIONS = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
NUM_CONSTANTS = {
    1: ('one', 'ten'),
    2: ('two', 'twenty'),
    3: ('three', 'thirty'),
    4: ('four', 'forty'),
    5: ('five', 'fifty'),
    6: ("six", 'sixty'),
    7: ('seven', 'seventy'),
    8: ('eight', 'eighty'),
    9: ('nine', 'ninety')
}

# Source: https://www.thoughtco.com/zeros-in-million-billion-trillion-2312346
LOG_CONSTANTS = {
    2: 'hundred',
    3: 'thousand',
    6: 'million',
    9: 'billion',
    12: 'trillion',
    15: 'quadrillion',
    18: 'quintillion',
    21: 'sextillion',
    24: 'septillion',
    27: 'octillion',
    30: 'nonillion',
    33: 'decillion',
    36: 'undecillion',
    39: 'duodecillion',
    42: 'tredecillion',
    45: 'quatttuor-decillion',
    48: 'quindecillion',
    51: 'sexdecillion',
    54: 'septen-decillion',
    57: 'octodecillion',
    60: 'novemdecillion',
    63: 'vigintillion'
}

MAX_LOG = 63
