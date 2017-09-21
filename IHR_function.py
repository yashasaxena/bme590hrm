import numpy as np

# Instant Heart Rate Function

def instHR(t_array):
    dt_first_beat = t_array[1] - t_array[0]

    instHR = 1/dt_first_beat * 60

    return instHR






