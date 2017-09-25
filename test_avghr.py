import pytest
import numpy as np
import pytest_cov
import pytest_pep8
import unittest
import avghr
import sys
import math
import ecg_data.csv
import datavalidation

"""

unit tests for average HR code

"""

def test_avghr():
    assert(avghr.hr_averaging(ecg_data.csv), 30)


def test_tachy_present():
    assert(avghr.tachy(200),  False)


def test_tachy_not_present():
    assert(avghr.tachy(80),  True)


def test_brachy_present():
    assert(avghr.brachy(30), False)


def test_brachy_not_present():
    assert (avghr.brachy(65), True)



def test_averagingtime():
    with pytest.raises(ValueError):
        avghr.hr_averaging(t,y,)

def teststring():
    with pytest.raises(TypeError):
        avghr.hr_averaging(t,y, "word")
