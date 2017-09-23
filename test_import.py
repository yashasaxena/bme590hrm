import pytest
import unittest
import datavalidation_code

import numpy
import sys

# import iPython
# import pytest
# import "pytest-cov"
# import "pytest-pep8"

"""
Test 1 - test  test that you are parsing the read data correctly into numpy arrays, which would be a good test.
2. 
3. 
"""

#test that the data is correctly in 2 columns
def testcolumns():
    with pytest.raises(TypeError):
        datavalidation_code.columncheck('FaultyData_UnitTest.csv')


#test that the headers are present
#def testheader():
#    with pytest.raises(ValueError):
#        datavalidation_code.headercheck('FaultyData_UnitTest.csv')

#test that the data type after the first row is all float/int
def testdatatype():
    with pytest.raises(ValueError):
        datavalidation_code.datatypecheck('FaultyData_UnitTest.csv')

#test that the data values are within a practical range
def testvaluerange():
    with pytest.raises(ValueError):
        datavalidation_code.datapracticality('FaultyData_UnitTest.csv')

def testdataisgood():
    assert datavalidation_code.columncheck("ecg_data.csv")==1
    assert datavalidation_code.datatypecheck("ecg_data.csv")==1
    assert datavalidation_code.datapracticality("ecg_data.csv")==1