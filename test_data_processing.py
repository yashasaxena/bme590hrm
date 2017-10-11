import pytest
import unittest
import HRimport

import numpy as np
import sys

# import iPython
# import pytest
# import "pytest-cov"
# import "pytest-pep8"

#test that the data is correctly in 2 columns
def testcolumns():
    """ unit test to throw an error if the data is not consistently in 2 columns"""
    with pytest.raises(TypeError):
        x = HRimport.Data()  # will need to change file name, "Data" is the class
        x.columncheck('FaultyData_UnitTest.csv')  # will need to change file name, "Data" is the class
        # and "columncheck" is method

#test that the data type after the first row is all float/int
def testdatatype():
    """ unit test to throw an error if any data is string type"""
    with pytest.raises(ValueError):
        x = HRimport.Data()
        x.datatypecheck('FaultyData_UnitTest.csv')

#test that the data values are within a practical range
def testvaluerange():
    """ unit test to throw an error if the data is above 10mV"""
    with pytest.raises(ValueError):
        x = HRimport.Data()
        x.datapracticality('FaultyData_UnitTest.csv')

def testdataisgood():
    """ unit test to make sure that all data passes
    columncheck():, datatypecheck():, and datapracticality():
    and that no error is thrown when data behaves as expected"""
    x = HRimport.Data()
    assert x.columncheck("ecg_data.csv")==1
    assert x.datatypecheck("ecg_data.csv")==1
    assert x.datapracticality("ecg_data.csv")==1

#create a sine wave array to test peak finder, instant heart rate function
# f = 1 hz, T = 1000 ms
# time step will be 1 ms (0.001 s), t array goes from 0 to 10,000 ms (10 s)
# expected peaks should be 10

t = np.arange(0, 10, 0.001)
signal = abs(np.sin(t*np.pi)**3)

#combine t and sin_vals arrays
array_test = np.column_stack((t, signal))
#array_test_time = hr.HR_peakdetect(array_test)

# unit test peak detection
def test_peakdetect():
    """ Tests if the number of peaks for a defined sine wave is returned by peak detection function
    """
    x = HRimport.Processing()
    peak_times = x.ecg_peakdetect(array_test)
    assert len(x.t) == 10

#def test_instHR():
#   """ Tests if instant heart rate calculated is equal to T * 60s/min
#    """
#    x = HRimport.Processing()
#    assert x.HRimport.ecg_peakdetect(int(round(hr.instHR(array_test_time))) == 60)
