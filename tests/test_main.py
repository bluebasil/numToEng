import pytest
import numToEng
from numToEng import main
from decimal import *


def test_max_number():
    expected_output = "Nine hundred and ninety nine vigintillion nine hundred and ninety nine novemdecillion nine hundred and ninety nine octodecillion nine hundred and ninety nine septen-decillion nine hundred and ninety nine sexdecillion nine hundred and ninety nine quindecillion nine hundred and ninety nine quatttuor-decillion nine hundred and ninety nine tredecillion nine hundred and ninety nine duodecillion nine hundred and ninety nine undecillion nine hundred and ninety nine decillion nine hundred and ninety nine nonillion nine hundred and ninety nine octillion nine hundred and ninety nine septillion nine hundred and ninety nine sextillion nine hundred and ninety nine quintillion nine hundred and ninety nine quadrillion nine hundred and ninety nine trillion nine hundred and ninety nine billion nine hundred and ninety nine million nine hundred and ninety nine thousand nine hundred and ninety nine"
    input_number = 10**66-1
    assert expected_output == main.number_to_english(input_number)


def test_min_number():
    expected_output = "Negative nine hundred and ninety nine vigintillion nine hundred and ninety nine novemdecillion nine hundred and ninety nine octodecillion nine hundred and ninety nine septen-decillion nine hundred and ninety nine sexdecillion nine hundred and ninety nine quindecillion nine hundred and ninety nine quatttuor-decillion nine hundred and ninety nine tredecillion nine hundred and ninety nine duodecillion nine hundred and ninety nine undecillion nine hundred and ninety nine decillion nine hundred and ninety nine nonillion nine hundred and ninety nine octillion nine hundred and ninety nine septillion nine hundred and ninety nine sextillion nine hundred and ninety nine quintillion nine hundred and ninety nine quadrillion nine hundred and ninety nine trillion nine hundred and ninety nine billion nine hundred and ninety nine million nine hundred and ninety nine thousand nine hundred and ninety nine"
    input_number = -10**66+1
    assert expected_output == main.number_to_english(input_number)


def test_overflow():
    input_number = 10**66
    with pytest.raises(OverflowError):
        main.number_to_english(input_number)


def test_zero():
    expected_output = "Zero"
    input_number = 0
    assert expected_output == main.number_to_english(input_number)


def test_negative():
    expected_output = "Negative one"
    input_number = -1
    assert expected_output == main.number_to_english(input_number)


def test_thirteen():
    expected_output = "Thirteen"
    input_number = 13
    assert expected_output == main.number_to_english(input_number)


def test_eighty_five():
    expected_output = "Eighty five"
    input_number = 85
    assert expected_output == main.number_to_english(input_number)


def test_thousands():
    expected_output = "Five thousand two hundred and thirty seven"
    input_number = 5237
    assert expected_output == main.number_to_english(input_number)


def test_skip_logs():
    expected_output = "Two million six hundred"
    input_number = 2000600
    assert expected_output == main.number_to_english(input_number)


def test_skip_hundreds():
    expected_output = "Two million and sixty six"
    input_number = 2000066
    assert expected_output == main.number_to_english(input_number)


def test_log_precision():
    expected_output = "One quadrillion"
    input_number = 10**15
    assert expected_output == main.number_to_english(input_number)