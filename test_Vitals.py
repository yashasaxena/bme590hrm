import pytest
import Vitals
import Processing
import numpy as np

"""

Unit tests for Vitals class

"""

t = np.arange(0, 60, 0.001)
t_midpoint = int(t.size / 2)
signal = abs(np.sin(t*np.pi)**3)

# combine t and signal arrays
sine_array_test = np.column_stack((t, signal))
sine_data = Processing.Processing()
sine_data.ecg_peakdetect(sine_array_test)
sine_array_test_time = sine_data.t


def test_nonzero_averaging_time():
    """
    .. function:: test_nonzero_averaging_time():
    Test if the averaging time is a non-zero and positive number,
    otherwise throw error
    """

    with pytest.raises(ValueError):
        Vitals.Vitals(0, sine_array_test_time, t)


def test_valid_len_averaging_time():
    """
    .. function:: test_valid_len_averaging_time():
    Test if the averaging time less than or equal to the length of ECG
    acquisition time, otherwise throw error
    """

    with pytest.raises(ValueError):
        Vitals.Vitals(15, sine_array_test_time, t)


def test_is_number_averaging_time():
    """
    .. function:: test_is_number_averaging_time():
    Test if the averaging time is a number, otherwise throw error
    """

    with pytest.raises(ValueError):
        Vitals.Vitals("word", sine_array_test_time, t)


def test_fraction_div_by_0():
    """
    .. function:: test_fraction_div_by_0():
    Test if the averaging time is a valid fraction, throw error if zero
    division occurs
    """

    with pytest.raises(ZeroDivisionError):
        Vitals.Vitals('1/0', sine_array_test_time, t)


def test_fraction_valid_syntax():
    """
    .. function:: test_fraction_valid_syntax():
    Test if the averaging time uses valid fraction syntax
    """

    with pytest.raises(ValueError):
        Vitals.Vitals('1/2/3', sine_array_test_time, t)


def test_avg_hr_with_fraction():
    """
    .. function:: test_avg_hr_with_fraction():
    Test if the avghr function calculates the correct avg HR using a fraction
    """
    x = Vitals.Vitals('5/60', sine_array_test_time, t)
    assert x.avg_hr_array[t_midpoint] == 60


def test_avg_hr_with_float_as_string():
    """
    .. function:: test_avg_hr_with_float_as_string():
    Test if the avghr function calculates the correct avg HR using a decimal
    value passed as a string
    """
    x = Vitals.Vitals('.33333333', sine_array_test_time, t)
    assert x.avg_hr_array[t_midpoint] == 60


def test_avg_hr_with_float():
    """
    .. function:: test_avg_hr_with_float():
    Test if the avghr function calculates the correct avg HR using a
    decimal value
    """

    x = Vitals.Vitals(0.33333333, sine_array_test_time, t)
    assert x.avg_hr_array[t_midpoint] == 60


def test_avg_hr_length():

    x = Vitals.Vitals(0.33333333, sine_array_test_time, t)
    assert len(x.avg_hr_array) == len(t)


def test_inst_hr_val():
    """
        .. function:: test_inst_hr_val():
        Tests if instant heart rate calculated is equal to T * 60s/min
    """
    x = Vitals.Vitals('5/60', sine_array_test_time, t)

    for i in range(0, len(x.inst_hr_array)):
        assert x.inst_hr_array[i] == 60


def test_inst_hr_length():
    """
        .. function:: test_inst_hr_length():
        Tests if instant heart rate array is correct length
    """
    x = Vitals.Vitals('5/60', sine_array_test_time, t)
    assert len(x.inst_hr_array) == len(t)
