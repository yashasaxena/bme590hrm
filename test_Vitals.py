import pytest
import Vitals
import Processing
import Data
import numpy as np

"""

Unit tests for Vitals class

"""

test_data = Data.Data('test_data5.csv')
test_data.extraction()
full_time_array = test_data.hr_data[:,0]
processed_data = Processing.Processing()
processed_data.ecg_peakdetect(test_data.hr_data)
array_test_time = processed_data.t

t = np.arange(0, 60, 0.001)
signal = abs(np.sin(t*np.pi)**3)

# combine t and signal arrays
sine_array_test = np.column_stack((t, signal))
sine_data = Processing.Processing()
sine_data.ecg_peakdetect(sine_array_test)
sine_array_test_time = sine_data.t


def test_nonzero_avgingtime():
    """
    .. function:: test_nonzero_avgingtime():
    Test if the averaging time is a non-zero and positive number,
    otherwise throw error
    """

    with pytest.raises(ValueError):
        Vitals.Vitals(0, array_test_time, full_time_array)


def test_validlen_avgingtime():
    """
    .. function:: test_validlen_avgingtime():
    Test if the averaging time less than or equal to the length of ECG
    acquisition time, otherwise throw error
    """

    with pytest.raises(ValueError):
        Vitals.Vitals(15, array_test_time, full_time_array)


def test_isnumber_avgingtime():
    """
    .. function:: test_isnumber_avgingtime():
    Test if the averaging time is a number, otherwise throw error
    """

    with pytest.raises(ValueError):
        Vitals.Vitals("word", array_test_time, full_time_array)


def test_fraction_divby0():
    """
    .. function:: test_fraction_divby0():
    Test if the averaging time is a valid fraction, throw error if zero
    division occurs
    """

    with pytest.raises(ZeroDivisionError):
        Vitals.Vitals('1/0', array_test_time, full_time_array)


def test_fraction_validsyntax():
    """
    .. function:: test_fraction_validsyntax():
    Test if the averaging time uses valid fraction syntax
    """

    with pytest.raises(ValueError):
        Vitals.Vitals('1/2/3', array_test_time, full_time_array)


def test_avghr_withfraction():
    """
    .. function:: test_avghr_withfraction():
    Test if the avghr function calculates the correct avg HR using a fraction
    """
    x = Vitals.Vitals('5/60', array_test_time, full_time_array)
    assert x.avg_hr_val == 84


def test_avghr_with_float_as_string():
    """
    .. function:: test_avghr_with_float_as_string():
    Test if the avghr function calculates the correct avg HR using a decimal
    value passed as a string
    """
    x = Vitals.Vitals('.083333333', array_test_time, full_time_array)
    assert x.avg_hr_val == 84


def test_avghr_with_float():
    """
    .. function:: test_avghr_with_float():
    Test if the avghr function calculates the correct avg HR using a
    decimal value
    """

    x = Vitals.Vitals(0.083333333, array_test_time, full_time_array)

    assert x.avg_hr_val == 84


def test_insthr():
    """
        .. function:: test_instHR():
        Tests if instant heart rate calculated is equal to T * 60s/min
    """
    x = Vitals.Vitals('5/60', sine_array_test_time, t)

    for i in range(0, len(x.inst_hr_array)):
        assert x.inst_hr_array[i] == 60
