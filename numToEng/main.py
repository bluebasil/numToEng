import argparse
from numToEng.constants import *


def _process_args():
    """ Helper method to get the input number of the input parameters """
    parser = argparse.ArgumentParser(description="A toy package for converting numbers to written out English.")
    parser.add_argument("number", type=int, help="The number that you want to convert.  Number must be an Integer.  Number must be between -10^66 and 10^66, exclusive.")
    num = parser.parse_args().number
    return int(num)


def _floored_log10(input):
    """ Helper function for calculating the number of digits of very large numbers with infinite precision
    Parameters:
        input - must be an integer > 0
    Return:
        Returns an integer representing the log of the input
    """
    return len(str(input)) - 1


def _process_num(words, num, add_and=False):
    """ helper method to process a portion of the number
    Parameters:
        words - a list of strings, representing how much of the number has been process.
        num - a portion of the overall number, which should be converted to English and appended to words
        add_and - a boolean, representing if 'and' should be used to delineate this number if appropriate
    """
    if num == 0:
        return

    # math.log(num,10) and math.log10(num) lost precision when calculating log's >= 14.  Using Decimal, another potential option, had similar issues
    num_log = _floored_log10(num)

    # Only add 'and' if the final digit is in the ones or tens spot
    if add_and and num_log < 2:
        words.append(AND)

    if num_log == 0 and num in NUM_CONSTANTS:
        words.append(NUM_CONSTANTS[num][0])

    elif num_log == 1:
        if num in TEEN_EXCEPTIONS:
            words.append(TEEN_EXCEPTIONS[num])
        else:
            words.append(NUM_CONSTANTS[num // 10][1])
            _process_num(words, num % 10)

    elif num_log >= 2:
        # base_num_log will be a multiple of 3, except for when considering hundreds
        base_num_log = max(2, num_log - (num_log % 3))
        if base_num_log > MAX_LOG:
            raise OverflowError("Number too large.  Number must be between -10^66+1 and 10^66-1 inclusive")
        _process_num(words, num // 10 ** base_num_log)
        words.append(LOG_CONSTANTS[base_num_log])
        _process_num(words, num % 10 ** base_num_log, add_and=True)


def number_to_english(num):
    """ Number to English

    Parameters:
        num - An integer between -10^66 and 10^66 exclusive

    Returns:
        A string, with the number written out in plain english.
    """
    words = []

    if num == 0:
        return ZERO.capitalize()
    elif num < 0:
        words.append(NEGATIVE)
        num *= -1

    _process_num(words, num)

    return ' '.join(words).capitalize()


if __name__ == '__main__':
    print(number_to_english(_process_args()))
