import pytest

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
def testheader():
    with pytest.raises(TypeError):
        datavalidation_code.headercheck('FaultyData_UnitTest.csv')

#test that the data type after the first row is all float/int
def testdatatype():
    with pytest.raises(TypeError):
        datavalidation_code.datatypecheck('FaultyData_UnitTest.csv')

#test that the data values are within a practical range
def testvaluerange():
    with pytest.raises(TypeError):
        datavalidation_code.datapracticality('FaultyData_UnitTest.csv')

# test that the read data was parsed correctly into numpy arrays
def testnumpyarray():
    with pytest.raises(TypeError):
        datavalidation_code.dataextraction('FaultyData_UnitTest.csv')


#def teststring():
    #with pytest.raises(TypeError):
     #   sumfxn2.summation_func('a', 'b')

def main():
    print("Blah")
    with open('FaultyData_UnitTest.csv') as HR:
        csv_HR = csv.reader(HR)

    for row in csv_HR:
        print (row);



