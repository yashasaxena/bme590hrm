import numpy as np


class Processing:

   def __init__(self):
       self.t = []

   def ecg_peakdetect(self, data_array):
    """ Returns a time array of times where peak was detected

    :param data_array: a 2-d array with time and voltage values
    :rtype: array
    """
        # peak detection function based on variable threshold method
        diff_filter = 0.125 * np.array([2, 1, -1, -2])
        # differentiation process/bandpass filter window, baseline correction
        pre_processing = data_array[:, 1]
        pre_processing = np.convolve(pre_processing, diff_filter, 'same')

        max_peak = np.max(pre_processing)
        threshold = max_peak - 0.5 * max_peak
        peakind = []
        time_array = []
        time_array_clean = []

        for c in range(0, len(pre_processing)):
            if pre_processing[c] >= threshold:
                peakind.append(c)
                time_array.append(data_array[c, 0])

        time_differences = np.diff(time_array)

        for d in range(0, len(time_differences)):
            if time_differences[d] > 0.3:
                time_array_clean.append(time_array[d])

        time_array_clean.append(time_array[-1])

        self.t = time_array_clean