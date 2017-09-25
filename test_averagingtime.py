import pytest
import numpy
import pytest_cov
import pytest_pep8
import unittest
import avghr
import sys

"""
unit tests to ensure averaging time input is valid

"""

def test_arguments():
    with pytest.raises(TypeError):
        avghr.hr_averaging(ecg_data.csv, 5)


def test_integer():
    assert(avghr.hr_averaging(4, 6), 3)


def test_floating():
    assert(avghr.summation_func(-4, 2), 0)


