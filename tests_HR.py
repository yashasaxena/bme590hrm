import HR_allfuncs as hr
import math
import numpy as np
import pytest


#create a sine wave array to test peak finder, instant heart rate function
# f = 1 hz, T = 1000 ms
# time step will be 1 ms (0.001 s), t array goes from 0 to 10,000 ms (10 s)
# expected peaks should be 10

t = np.arange(0, 10, 0.001)
sin_vals = []
pi = math.pi
for x in range(0,len(t)):
    sin_vals[x] = math.sin(2*pi*t[x])

#combine t and sin_vals arrays
array_test = np.concatenate((t,sin_vals),axis=0)
array_test_time = hr.HR_peakdetect(array_test)

# unit test peak detection
def test_peakdetect():
    assert hr.HR_peakdetect(array_test) == 10

def test_instHR():
    assert hr.instHR(array_test_time) == 60
