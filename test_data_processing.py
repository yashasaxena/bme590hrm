import pytest
import unittest
import datavalidation_code

import numpy
import sys

# import iPython
# import pytest
# import "pytest-cov"
# import "pytest-pep8"

#test that the data is correctly in 2 columns
def testcolumns():
    """ unit test to throw an error if the data is not consistently in 2 columns"""
    with pytest.raises(TypeError):
        datavalidation_code.columncheck('FaultyData_UnitTest.csv')

#test that the data type after the first row is all float/int
def testdatatype():
    """ unit test to throw an error if any data is string type"""
    with pytest.raises(ValueError):
        datavalidation_code.datatypecheck('FaultyData_UnitTest.csv')

#test that the data values are within a practical range
def testvaluerange():
    """ unit test to throw an error if the data is above 10mV"""
    with pytest.raises(ValueError):
        datavalidation_code.datapracticality('FaultyData_UnitTest.csv')

def testdataisgood():
    """ unit test to make sure that all data passes
    columncheck():, datatypecheck():, and datapracticality():
    and that no error is thrown when data behaves as expected"""
    assert datavalidation_code.columncheck("ecg_data.csv")==1
    assert datavalidation_code.datatypecheck("ecg_data.csv")==1
    assert datavalidation_code.datapracticality("ecg_data.csv")==1

#create a sine wave array to test peak finder, instant heart rate function
# f = 1 hz, T = 1000 ms
# time step will be 1 ms (0.001 s), t array goes from 0 to 10,000 ms (10 s)
# expected peaks should be 10

t = np.arange(0, 10, 0.001)
signal = abs(np.sin(t*np.pi)**3)

#combine t and sin_vals arrays
array_test = np.column_stack((t, signal))
array_test_time = hr.HR_peakdetect(array_test)

# unit test peak detection
def test_peakdetect():
    """
    .. function:: test_peakdetect():
    Tests if the number of peaks for a defined sine wave is returned by peak detection function
    """
    assert len(hr.HR_peakdetect(array_test)) == 10

def test_instHR():
    """
        .. function:: test_instHR():
        Tests if instant heart rate calculated is equal to T * 60s/min
    """
    assert int(round(hr.instHR(array_test_time))) == 60
