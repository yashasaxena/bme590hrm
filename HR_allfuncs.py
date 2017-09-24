import numpy as np
import scipy
from scipy import signal
import csv
import matplotlib.pyplot as plt


def dataextraction(filename):
    HR_data = np.array([0, 0])

    with open(filename) as HR:
        csv_HR = csv.reader(HR)
        #        data = list(csv_HR)
        #        N = len(data)
        next(csv_HR)
        for row in csv_HR:
            time = float(row[0])
            signal = float(row[1])
            HR_data = np.vstack([HR_data, [time, signal]])

    HR.close()
    HR_data = np.delete(HR_data, (0), axis=0)

    return HR_data


def HR_peakdetect(data_array):
    # peak detection function based on variable threshold method
    diff_filter = 0.125 * np.array([2, 1, -1, -2])
    # differentiation process window, baseline correction
    pre_processing = data_array[:, 1]
    pre_processing = np.convolve(pre_processing, diff_filter, 'same')
    # inverting data because negative peaks have less peak noise surrounding them
    inverted_data = np.multiply(-1, pre_processing)
    # heart rates to test, lower spectrum to higher spectrum
    rates = np.array(range(40, 200)) / 60
    t_step = data_array[1, 0] - data_array[0, 0]
    fs = int(1 / t_step)  # sampling frequency that provides number of steps in 1 second
    peakind = signal.find_peaks_cwt(inverted_data, fs / rates / 10)

    time_array = []

    for c in range(0, len(peakind)):
        y = peakind[c]
        time_array.append(data_array[y, 0])

    return time_array


def instHR(t_array):
    dt_first_beat = t_array[2] - t_array[1]

    instHR = 1/dt_first_beat * 60

    return instHR