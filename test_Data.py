import pytest
import Data as D


def test_columns():
    """ unit test to throw an error if the data is not consistently in 2 columns"""
    with pytest.raises(TypeError):
        x = D.Data('FaultyData_UnitTest.csv')
        x.column_check('FaultyData_UnitTest.csv')


def test_datatype():
    """ unit test to throw an error if any data is string type"""
    with pytest.raises(ValueError):
        x = D.Data('FaultyData_UnitTest.csv')
        x.type_check()


def test_valuerange():
    """ unit test to throw an error if the data is above 10mV"""
    with pytest.raises(ValueError):
        x = D.Data('FaultyData_UnitTest.csv')
        x.practicality_check()


def test_dataisgood():
    """ unit test to make sure that all data passes
    columncheck():, typecheck():, and practicality():
    and that no error is thrown when data behaves as expected"""
    x = D.Data('FaultyData_UnitTest.csv')
    assert x.column_check("ecg_data.csv")==1
    assert x.type_check()==1
    assert x.practicality_check()==1