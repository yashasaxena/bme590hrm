import pytest
import avghr

"""

unit tests for average HR code

"""


def test_numinputs():
    """
    .. function:: test_numinputs():
    Test if the number of inputs for hr_averaging() is valid, otherwise throw error
    """
    with pytest.raises(TypeError):
        avghr.hr_averaging()


def test_nonzero_avgingtime():
    """
    .. function:: test_nonzero_avgingtime():
    Test if the averaging time is a non-zero and positive number, otherwise throw error
    """
    with pytest.raises(ValueError):
        avghr.hr_averaging(0)


def test_validlen_avgingtime():
    """
    .. function:: test_validlen_avgingtime():
    Test if the averaging time less than or equal to the length of ECG acquisition time, otherwise throw error
    """
    with pytest.raises(ValueError):
        avghr.hr_averaging(15)


def test_isnumber_avgingtime():
    """
    .. function:: test_isnumber_avgingtime():
    Test if the averaging time is a number, otherwise throw error
    """
    with pytest.raises(ValueError):
        avghr.hr_averaging("word")


def test_fraction_divby0():
    """
    .. function:: test_fraction_divby0():
    Test if the averaging time is a valid fraction, throw error if zero division occurs
    """
    with pytest.raises(ZeroDivisionError):
        avghr.hr_averaging('1/0')


def test_fraction_validsyntax():
    """
    .. function:: test_fraction_validsyntax():
    Test if the averaging time uses valid fraction syntax
    """
    with pytest.raises(ValueError):
        avghr.hr_averaging('1/2/3')


def test_avghr_withfraction():
    """
    .. function:: test_avghr_withfraction():
    Test if the avghr function calculates the correct avg HR using a fraction
    """
    assert(avghr.hr_averaging('1/4'), 90)


def test_avghr_with_float_as_string():
    """
    .. function:: test_avghr_with_float_as_string():
    Test if the avghr function calculates the correct avg HR using a decimal value passed as a string
    """
    assert(avghr.hr_averaging('.3'), 90)


def test_avghr_with_float():
    """
    .. function:: test_avghr_with_float():
    Test if the avghr function calculates the correct avg HR using a decimal value
    """
    assert(avghr.hr_averaging(.333), 90)


def test_tachylim_valid():
    """
    .. function:: test_tachylim_valid():
    Test if the tachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        avghr.tachy(80, -1)


def test_tachystring():
    """
    .. function:: test_tachystring():
    Test if the tachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        avghr.tachy("word")


def test_tachy_present():
    """
    .. function:: test_tachy_present():
    Test to see if tachycardia is present
    """
    assert(avghr.tachy(200),  False)


def test_tachy_not_present():
    """
    .. function:: test_tachy_not_present():
    Test to see if tachycardia is not present
    """
    assert(avghr.tachy(80),  True)


def test_brachylim_valid():
    """
    .. function:: test_brachylim_valid():
    Test if the brachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        avghr.brachy(80, -1)


def test_brachystring():
    """
    .. function:: test_brachystring():
    Test if the brachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        avghr.brachy("word")


def test_brachy_present():
    """
    .. function:: test_brachy_present():
    Test to see if brachycardia is present
    """
    assert(avghr.brachy(30), False)


def test_brachy_not_present():
    """
    .. function:: test_brachy_not_present():
    Test to see if brachycardia is not present
    """
    assert (avghr.brachy(65), True)
