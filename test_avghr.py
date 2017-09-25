import pytest
import avghr

"""

unit tests for average HR code

"""

def test_numinputs():
    with pytest.raises(TypeError):
        avghr.hr_averaging()


def test_nonzero_avgingtime():
    with pytest.raises(ValueError):
        avghr.hr_averaging(0)


def test_validlen_avgingtime():
    with pytest.raises(ValueError):
        avghr.hr_averaging(15)

def test_isnumber_avgingtime():
    with pytest.raises(ValueError):
        avghr.hr_averaging("word")


def test_fraction_divby0():
    with pytest.raises(ZeroDivisionError):
        avghr.hr_averaging('1/0')

def test_fraction_validsyntax():
    with pytest.raises(ValueError):
        avghr.hr_averaging('1/2/3')


def test_avghr_withfraction():
    assert(avghr.hr_averaging('1/4'), 90)


def test_avghr_withfloat():
    assert(avghr.hr_averaging(.333), 90)


def test_tachylim_valid():
    with pytest.raises(ValueError):
        avghr.tachy(80, -1)


def test_tachystring():
    with pytest.raises(TypeError):
        avghr.tachy("word")


def test_tachy_present():
    assert(avghr.tachy(200),  False)


def test_tachy_not_present():
    assert(avghr.tachy(80),  True)


def test_brachylim_valid():
    with pytest.raises(ValueError):
        avghr.brachy(80,-1)

def test_brachystring():
    with pytest.raises(TypeError):
        avghr.brachy("word")

def test_brachy_present():
    assert(avghr.brachy(30), False)


def test_brachy_not_present():
    assert (avghr.brachy(65), True)




