import pytest
import Vitals as v
import numpy as np
import Processing as p
import Data as d
import HR_allfuncs as hr

# create a sine wave array to test peak finder, instant heart rate function
# f = 1 hz, T = 1000 ms
# time step will be 1 ms (0.001 s), t array goes from 0 to 10,000 ms (10 s)
# expected peaks should be 10

# t = np.arange(0, 60, 0.001)
# signal = abs(np.sin(t*np.pi)**3)
#
# # combine t and signal arrays
# array_test = np.column_stack((t, signal))
# array_test_time = hr.HR_peakdetect(array_test)



"""

unit tests for average HR code

"""

test_data = d.Data('test_data5.csv')
test_data.extraction()
processed_data = p.Processing()
processed_data.ecg_peakdetect(test_data.HR_data)
array_test_time = processed_data.t


def test_nonzero_avgingtime():
    """
    .. function:: test_nonzero_avgingtime():
    Test if the averaging time is a non-zero and positive number, otherwise throw error
    """

    with pytest.raises(ValueError):
        x = v.Vitals(0, array_test_time)


def test_validlen_avgingtime():
    """
    .. function:: test_validlen_avgingtime():
    Test if the averaging time less than or equal to the length of ECG acquisition time, otherwise throw error
    """

    with pytest.raises(ValueError):
        x = v.Vitals(15, array_test_time)


def test_isnumber_avgingtime():
    """
    .. function:: test_isnumber_avgingtime():
    Test if the averaging time is a number, otherwise throw error

    with pytest.raises(ValueError):
        x = v.Vitals("word", array_test_time)"""


def test_fraction_divby0():
    """
    .. function:: test_fraction_divby0():
    Test if the averaging time is a valid fraction, throw error if zero division occurs
    """

    with pytest.raises(ZeroDivisionError):
        x = v.Vitals('1/0', array_test_time)


def test_fraction_validsyntax():
    """
    .. function:: test_fraction_validsyntax():
    Test if the averaging time uses valid fraction syntax
    """

    with pytest.raises(ValueError):
        x = v.Vitals('1/2/3', array_test_time)


def test_avghr_withfraction():
    """
    .. function:: test_avghr_withfraction():
    Test if the avghr function calculates the correct avg HR using a fraction
    """
    x = v.Vitals('5/60', array_test_time)
    assert x.avg_hr_val == 84


def test_avghr_with_float_as_string():
    """
    .. function:: test_avghr_with_float_as_string():
    Test if the avghr function calculates the correct avg HR using a decimal value passed as a string
    """
    x = v.Vitals('.083333333', array_test_time)
    assert x.avg_hr_val == 84

def test_avghr_with_float():
    """
    .. function:: test_avghr_with_float():
    Test if the avghr function calculates the correct avg HR using a decimal value
    """

    x = v.Vitals(0.083333333, array_test_time)

    assert x.avg_hr_val == 84
