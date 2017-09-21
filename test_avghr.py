import pytest
import sumfxn

import numpy

import sys
# import iPython
# import pytest
# # import "pytest-cov"
# import "pytest-pep8"

"""

unit tests for average HR code

"""


def test_avghr():
    assert(avghr(time, mV, avg_time), avghr_val)


def test_tachy():
    assert(tachy(200), False)


def test_brachy():
    assert(brachy(30), False)