import pytest
import filename.py

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

#test that the headers are present
def testheader():
    with pytest.raises(TypeError):
        filename.funcname(FaultyData_UnitTest.csv)

#test that the data type after the first row is all float/int
def testdatatype():
    with pytest.raises(TypeError):
        filename.funcname(FaultyData_UnitTest.csv)

#test that the data is correctly in 2 columns
def testcolumns():
    with pytest.raises(TypeError):
        filename.funcname(FaultyData_UnitTest.csv)

#test that the data values are within a practical range
def testvaluerange():
    with pytest.raises(TypeError):
        filename.funcname(FaultyData_UnitTest.csv)

# test that the read data was parsed correctly into numpy arrays
def testnumpyarray():
    with pytest.raises(TypeError):
        filename.funcname(FaultyData_UnitTest.csv)


#def teststring():
    #with pytest.raises(TypeError):
     #   sumfxn2.summation_func('a', 'b')


