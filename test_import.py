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
    """"""
    """..function: testcolumns():
    unit test to throw an error if the data is not consistently in 2 columns"""
    with pytest.raises(TypeError):
        datavalidation_code.columncheck('FaultyData_UnitTest.csv')


#test that the headers are present
#def testheader():
#    with pytest.raises(ValueError):
#        datavalidation_code.headercheck('FaultyData_UnitTest.csv')

#test that the data type after the first row is all float/int
def testdatatype():
    """"""
    """..function: testdatatype():
    unit test to throw an error if any data is string type"""
    with pytest.raises(ValueError):
        datavalidation_code.datatypecheck('FaultyData_UnitTest.csv')

#test that the data values are within a practical range
def testvaluerange():
    """"""
    """..function: testvaluerange():
    unit test to throw an error if the data is above 10mV"""
    with pytest.raises(ValueError):
        datavalidation_code.datapracticality('FaultyData_UnitTest.csv')

def testdataisgood():
    """"""
    """..function: testdataisood():
    unit test to make sure that all data passes columncheck():, datatypecheck():, and datapracticality(): and that no error is thrown when data behaves as expected"""
    assert datavalidation_code.columncheck("ecg_data.csv")==1
    assert datavalidation_code.datatypecheck("ecg_data.csv")==1
    assert datavalidation_code.datapracticality("ecg_data.csv")==1