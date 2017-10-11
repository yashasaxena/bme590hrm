class processing:
# pseudocode for processing subclass
   def __init__(self):
       self.t = []

   def peakdetect(self, data_array):
    #       insert peak detect function here, which returns t_array
    """ Returns a time array of times where peak was detected

    :param data_array: a 2-d array with time and voltage values
    :rtype: array
    """
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

    self.t.append(time_array)
