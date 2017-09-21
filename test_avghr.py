import pytest
import numpy
import pytest_cov
import pytest_pep8
import unittest
import avghr


"""

unit tests for average HR code

"""


def test_avghr():
    assert(avghr.hr_averaging(time_array, mv_array, averaging_time), average_hr_val)


def test_tachy_present():
    assert(avghr.tachy(200),  False)

def test_tachy_not_present():
    assert(avghr.tachy(80),  True)

def test_brachy_present():
    assert(avghr.brachy(30), False)

def test_brachy_not_present():
    assert (avghr.brachy(65), True)
