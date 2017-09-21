import numpy as np
import scipy
from scipy import signal


def HR_peakdetect(data_array):
    # peak detection function based on variable threshold method
    diff_filter = 0.125*np.array([2,1,-1,-2])
    # differentiation process window
    pre_processing = data_array[:,1]
    pre_processing = np.convolve(data_array[:,1],diff_filter,'same')
    pre_processing = data_array[:, 1].astype(complex)
    # hilbert transform
    pre_processing = scipy.signal.hilbert(data_array[:,1])
    pre_processing = pre_processing.astype(float)
    data_array[:,1] = pre_processing
    # variable threshold
    first_peakind = signal.find_peaks_cwt(data_array[:,1],np.arange(1,len(data_array[:,1])))
    window_size = first_peakind[0]
    peakind = signal.find_peaks_cwt(data_array[:,1],np.arange(1,window_size))

    time_array = []
    for c in range(0,len(peakind)):
        y = peakind[c]
        time_array.append(data_array[y,0])

    return time_array









