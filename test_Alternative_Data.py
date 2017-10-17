import Alternative_Data
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
