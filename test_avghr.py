import pytest
import HR_allfuncs as hr
import numpy as np

# create a sine wave array to test peak finder, instant heart rate function
# f = 1 hz, T = 1000 ms
# time step will be 1 ms (0.001 s), t array goes from 0 to 10,000 ms (10 s)
# expected peaks should be 10

t = np.arange(0, 60, 0.001)
signal = abs(np.sin(t*np.pi)**3)

# combine t and sin_vals arrays
array_test = np.column_stack((t, signal))
array_test_time = hr.HR_peakdetect(array_test)
"""

unit tests for average HR code

"""


def test_numinputs():
    """
    .. function:: test_numinputs():
    Test if the number of inputs for hr_averaging() is valid, otherwise throw error
    """
    with pytest.raises(TypeError):
        hr.hr_averaging()


def test_nonzero_avgingtime():
    """
    .. function:: test_nonzero_avgingtime():
    Test if the averaging time is a non-zero and positive number, otherwise throw error
    """
    with pytest.raises(ValueError):
        hr.hr_averaging(0, array_test_time)


def test_validlen_avgingtime():
    """
    .. function:: test_validlen_avgingtime():
    Test if the averaging time less than or equal to the length of ECG acquisition time, otherwise throw error
    """
    with pytest.raises(ValueError):
        hr.hr_averaging(15, array_test_time)


def test_isnumber_avgingtime():
    """
    .. function:: test_isnumber_avgingtime():
    Test if the averaging time is a number, otherwise throw error
    """
    with pytest.raises(ValueError):
        hr.hr_averaging("word", array_test_time)


def test_fraction_divby0():
    """
    .. function:: test_fraction_divby0():
    Test if the averaging time is a valid fraction, throw error if zero division occurs
    """
    with pytest.raises(ZeroDivisionError):
        hr.hr_averaging('1/0', array_test_time)


def test_fraction_validsyntax():
    """
    .. function:: test_fraction_validsyntax():
    Test if the averaging time uses valid fraction syntax
    """
    with pytest.raises(ValueError):
        hr.hr_averaging('1/2/3', array_test_time)


def test_avghr_withfraction():
    """
    .. function:: test_avghr_withfraction():
    Test if the avghr function calculates the correct avg HR using a fraction
    """
    assert hr.hr_averaging('1/4', array_test_time) == 60


def test_avghr_with_float_as_string():
    """
    .. function:: test_avghr_with_float_as_string():
    Test if the avghr function calculates the correct avg HR using a decimal value passed as a string
    """
    assert hr.hr_averaging('.3', array_test_time) == 60


def test_avghr_with_float():
    """
    .. function:: test_avghr_with_float():
    Test if the avghr function calculates the correct avg HR using a decimal value
    """
    assert hr.hr_averaging(.333, array_test_time) == 60


def test_tachylim_valid():
    """
    .. function:: test_tachylim_valid():
    Test if the tachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        hr.tachy(80, -1)


def test_tachystring():
    """
    .. function:: test_tachystring():
    Test if the tachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        hr.tachy("word")


def test_tachy_present():
    """
    .. function:: test_tachy_present():
    Test to see if tachycardia is present
    """
    assert hr.tachy(200, tachy_limit=100) is True


def test_tachy_not_present():
    """
    .. function:: test_tachy_not_present():
    Test to see if tachycardia is not present
    """
    assert hr.tachy(80, tachy_limit=100) is False


def test_brachylim_valid():
    """
    .. function:: test_brachylim_valid():
    Test if the brachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        hr.brachy(80, -1)


def test_brachystring():
    """
    .. function:: test_brachystring():
    Test if the brachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        hr.brachy(80, "word")


def test_brachy_present():
    """
    .. function:: test_brachy_present():
    Test to see if brachycardia is present
    """
    assert hr.brachy(30, brachy_limit=60) is True


def test_brachy_not_present():
    """
    .. function:: test_brachy_not_present():
    Test to see if brachycardia is not present
    """
    assert hr.brachy(65, brachy_limit=60) is False
