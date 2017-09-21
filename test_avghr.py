import pytest
import numpy
import pytest_cov
import pytest_pep8
import unittest

"""

unit tests for average HR code

"""


def test_avghr():
    assert(avghr(time, mV, avg_time), avghr_val)


def test_tachy():
    assert(tachy(200), False)


def test_brachy():
    assert(brachy(30), False)