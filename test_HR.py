import HR_allfuncs as hr
import numpy as np
import pytest


#create a sine wave array to test peak finder, instant heart rate function
# f = 1 hz, T = 1000 ms
# time step will be 1 ms (0.001 s), t array goes from 0 to 10,000 ms (10 s)
# expected peaks should be 10

t = np.arange(0, 10, 0.001)
signal = abs(np.sin(t*np.pi)**3)

#combine t and sin_vals arrays
array_test = np.column_stack((t, signal))
array_test_time = hr.HR_peakdetect(array_test)

# unit test peak detection
def test_peakdetect():
    """
    .. function:: test_peakdetect():
    Tests if the number of peaks for a defined sine wave is returned by peak detection function
    """
    assert len(hr.HR_peakdetect(array_test)) == 10

def test_instHR():
    """
        .. function:: test_instHR():
        Tests if instant heart rate calculated is equal to T * 60s/min
    """
    assert int(round(hr.instHR(array_test_time))) == 60
