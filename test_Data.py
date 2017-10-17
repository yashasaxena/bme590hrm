import Data as Alternative_Data
import numpy as np
import pytest

def test_column_number():
    with pytest.raises(TypeError):
        x = Alternative_Data.Data('FaultyData_UnitTest.csv')
        x.column_check()


def test_value_type():
    with pytest.raises(TypeError):
        x = Alternative_Data.Data('FaultyData_UnitTest.csv')
        x.value_type()

def test_value_range():
    with pytest.raises(ValueError):
        x = Alternative_Data.Data('FaultyData_UnitTest.csv')
        x.value_range()

def test_data_is_good():
    good_test_data = Alternative_Data.Data('GoodData_UnitTest.csv')
    good_test_data.column_check()
    good_test_data.value_type()
    good_test_data.value_range()
    assert good_test_data.column_check_result is True
    assert good_test_data.value_type_result is True
    assert good_test_data.value_range_result is True