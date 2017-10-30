import numpy as np


class Processing:

    def __init__(self):
        self.t = []

    def ecg_peakdetect(self, data_array):
        """ Returns a time array of times where peak was detected
        :param data_array: a 2-d array with time and voltage values
        :rtype: 1-d array
        """
        pre_processing = data_array[:, 1]
        # peak detection function based on variable threshold method
        diff_filter = 0.125 * np.array([2, 1, -1, -2])
        # differentiation process/bandpass filter window, baseline correction

        pre_processing = np.convolve(pre_processing, diff_filter, 'same')

        # thresholding detection method based on baseline corrected peaks
        n_2secs = int(round(len(data_array[:, 0]) / 2000)) - 1

        max_array = []
        for j in range(0, n_2secs):
            temp = pre_processing[j * 2000:(j * 2000 + 2000)]
            max_array.append(np.nanmax(temp))

        max_peak = np.median(max_array)
        threshold = max_peak - 0.5 * max_peak
        peakind = []
        time_array = []
        time_array_clean = []

        for c in range(0, len(pre_processing)):
            if pre_processing[c] >= threshold:
                peakind.append(c)
                time_array.append(data_array[c, 0])

        time_differences = np.diff(time_array)

        # accounting for peaks that may have been tripled at a t step by convolution
        for d in range(0, len(time_differences)):
            if time_differences[d] > 0.3:
                time_array_clean.append(time_array[d])

        # filling in last time value because np.diff cuts off 1 t value
        time_array_clean.append(time_array[-1])

        self.t = time_array_clean
