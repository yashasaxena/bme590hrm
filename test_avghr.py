import pytest
import numpy as np
import pytest_cov
import pytest_pep8
import unittest
import avghr
import sys
import math
import datavalidation_code

"""

unit tests for average HR code

"""

def test_numinputs():
    with pytest.raises(TypeError):
        avghr.hr_averaging()


def teststring():
    with pytest.raises(TypeError):
        avghr.hr_averaging("word")


def test_avghr():
    assert(avghr.hr_averaging((1/3)), 90)


def test_tachy_present():
    assert(avghr.tachy(200),  False)


def test_tachy_not_present():
    assert(avghr.tachy(80),  True)


def test_brachy_present():
    assert(avghr.brachy(30), False)


def test_brachy_not_present():
    assert (avghr.brachy(65), True)



