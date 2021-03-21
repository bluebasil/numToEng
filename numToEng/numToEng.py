import argparse
import math

NEGATIVE = 'negative'
ZERO = 'Zero'
EXCEPTIONS = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fivteen',
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

def process_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("number")
    num = parser.parse_args().number
    return int(num)

def _process_num(num):
    if num == 0:
        return ''

    words = []

    num_log = int(math.log(num, 10))

    if num_log == 0:
        if num in NUM_CONSTANTS:
            words.append(NUM_CONSTANTS[num][0])
    elif num_log == 1:
        if num in EXCEPTIONS:
            words.append(EXCEPTIONS[num])
        else:
            words.append(NUM_CONSTANTS[int(num / 10)][1])
            words.append(_process_num(num % 10))
    elif num_log == 2:
        words.append(NUM_CONSTANTS[int(num / 10 ** 2)][0])
        words.append(LOG_CONSTANTS[2])
        substring = _process_num(num % 10 ** 2)
        if not substring == "":
            words.append("and")
            words.append(substring)
    elif num_log >= 3:
        base_num_log = num_log - (num_log % 3)

        words.append(_process_num(int(num / 10 ** base_num_log)))
        words.append(LOG_CONSTANTS[base_num_log])
        words.append(_process_num(num % 10 ** base_num_log))

    return ' '.join(words)



def numToEng(num):
    """
    Number to English String
    """

    words = []

    # negative
    if num == 0:
        return ZERO
    elif num < 0:
        words.append(NEGATIVE)
        num *= -1

    words.append(_process_num(num))

    return ' '.join(words).capitalize()



if __name__ == '__main__':
    print(numToEng(process_args()))