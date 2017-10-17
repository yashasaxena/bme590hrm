import pytest
import Diagnosis as d


def test_tachylim_valid():
    """
    .. function:: test_tachylim_valid():
    Test if the tachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        x = d.Diagnosis(80, -1)


def test_tachystring():
    """
    .. function:: test_tachystring():
    Test if the tachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        x = d.Diagnosis(100, "word")


def test_tachy_present():
    """
    .. function:: test_tachy_present():
    Test to see if tachycardia is present
    """
    x = d.Diagnosis(120, 100)
    assert x.tachy_result is True


def test_tachy_not_present():
    """
    .. function:: test_tachy_not_present():
    Test to see if tachycardia is not present
    """
    x = d.Diagnosis(80, 100)
    assert x.tachy_result is False


def test_brachylim_valid():
    """
    .. function:: test_brachylim_valid():
    Test if the brachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        x = d.Diagnosis(80, 100, -1)


def test_brachystring():
    """
    .. function:: test_brachystring():
    Test if the brachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        x = d.Diagnosis(80, 100, "word")


def test_brachy_present():
    """
    .. function:: test_brachy_present():
    Test to see if brachycardia is present
    """
    x = d.Diagnosis(40, 100, 60)
    assert x.brachy_result is True


def test_brachy_not_present():
    """
    .. function:: test_brachy_not_present():
    Test to see if brachycardia is not present
    """
    x = d.Diagnosis(80, 100, 60)
    assert x.brachy_result is False

