import pytest
import unittest
import HRM_classfile
import scipy

import numpy as np
import sys

# import iPython
# import pytest
# import "pytest-cov"
# import "pytest-pep8"

def test_columns():
    """ unit test to throw an error if the data is not consistently in 2 columns"""
    with pytest.raises(TypeError):
        x = HRM_classfile.Data()
        x.column_check('FaultyData_UnitTest.csv')

def test_datatype():
    """ unit test to throw an error if any data is string type"""
    with pytest.raises(ValueError):
        x = HRM_classfile.Data()
        x.type_check('FaultyData_UnitTest.csv')

def test_valuerange():
    """ unit test to throw an error if the data is above 10mV"""
    with pytest.raises(ValueError):
        x = HRM_classfile.Data()
        x.practicality_check('FaultyData_UnitTest.csv')

def test_dataisgood():
    """ unit test to make sure that all data passes
    columncheck():, typecheck():, and practicality():
    and that no error is thrown when data behaves as expected"""
    x = HRM_classfile.Data()
    assert x.column_check("ecg_data.csv")==1
    assert x.type_check("ecg_data.csv")==1
    assert x.practicality_check("ecg_data.csv")==1

# create a sine wave array to test peak finder, instant heart rate function
# f = 1 hz, T = 1000 ms
# time step will be 1 ms (0.001 s), t array goes from 0 to 10,000 ms (10 s)
# expected peaks should be 10

t = np.arange(0, 10, 0.001)
signal = abs(np.sin(t*np.pi)**3)

# combine t and sin_vals arrays
array_test = np.column_stack((t, signal))
# array_test_time = hr.HR_peakdetect(array_test)

# unit test peak detection
def test_peakdetect():
    """ Tests if the number of peaks for a defined sine wave is returned by peak detection function
    """
    x = HRM_classfile.Processing()
    peak_times = x.ecg_peakdetect(array_test)
    assert len(x.t) == 10

# def test_instHR():
#   """ Tests if instant heart rate calculated is equal to T * 60s/min
#    """
#    x = HRimport.Processing()
#    assert x.HRimport.ecg_peakdetect(int(round(hr.instHR(array_test_time))) == 60)
