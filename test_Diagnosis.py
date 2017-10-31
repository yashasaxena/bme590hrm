import pytest
import Diagnosis


def test_tachylim_valid():
    """
    .. function:: test_tachylim_valid():
    Test if the tachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        Diagnosis.Diagnosis([60, 70, 80], -1)


def test_tachystring():
    """
    .. function:: test_tachystring():
    Test if the tachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        Diagnosis.Diagnosis([60, 70, 80], "word")


def test_tachy_present():
    """
    .. function:: test_tachy_present():
    Test to see if tachycardia is present
    """
    x = Diagnosis.Diagnosis([120, 110, 140], 100)
    assert any(x.tachy_result) is True


def test_tachy_not_present():
    """
    .. function:: test_tachy_not_present():
    Test to see if tachycardia is not present
    """
    x = Diagnosis.Diagnosis([60, 70, 80], 100)
    assert not any(x.tachy_result) is True


def test_brachylim_valid():
    """
    .. function:: test_brachylim_valid():
    Test if the brachycardia limit is a valid threshold
    """
    with pytest.raises(ValueError):
        Diagnosis.Diagnosis([60, 70, 80], 100, -1)


def test_brachystring():
    """
    .. function:: test_brachystring():
    Test if the brachy_limit input is a valid number
    """
    with pytest.raises(TypeError):
        Diagnosis.Diagnosis([60, 70, 80], 100, "word")


def test_brachy_present():
    """
    .. function:: test_brachy_present():
    Test to see if brachycardia is present
    """
    x = Diagnosis.Diagnosis([120, 60, 40], 100, 60)
    assert any(x.brachy_result) is True


def test_brachy_not_present():
    """
    .. function:: test_brachy_not_present():
    Test to see if brachycardia is not present
    """
    x = Diagnosis.Diagnosis([120, 100, 80], 100, 60)
    assert not any(x.brachy_result) is True
