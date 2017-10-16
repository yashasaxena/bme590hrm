import numpy as np
from scipy import signal
import csv

HR_data = np.array([0, 0])  # initialize a matrix to store data

# Open CSV
# filename = 'ecg_data.csv'


def dataextraction(filename):

    """ Opens CSV file, converts all numbers to float type, then creates an array to append rows """
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
    HR_data = np.delete(HR_data, 0, axis=0)

    return HR_data


# DATA VALIDATION
def columncheck(filename):  # checks number of columns



    """ Confirms that data is arranged in 2 columns

        :rtype: Error raised if data structure is incorrect

    """

    with open(filename) as HR:
        csv_HR = csv.reader(HR)
        for row in csv_HR:
            if len(row) != 2:
                raise TypeError('Data is not organized in 2 columns, please check and try again.')
    a = 1
    return a

# def headercheck(filename):  # checks presence of headers
#    with open(filename) as HR:
#        csv_HR = csv.reader(HR)
#        header_row = next(csv_HR)
#        if (type(header_row[0]) != str) or (type(header_row[1]) != str):
#            raise ValueError('Data headers are not present, please check and try again.')
#   b=1
#   return b


def datatypecheck(filename):  # checks float/int
    """ Confirms there are no strings in the data

        :rtype: Error raised if data type is incorrect
    """
    datafile = dataextraction(filename)
    # csv_HR = csv.reader(HR)
    # next(csv_HR)
    # for row in csv_HR:
    for x in range(0, len(datafile)):
        if type(datafile[x, 1] == str):
            raise TypeError('Data is not of correct type, please check and try again')
    c = 1
    return c


def datapracticality(filename):  # checks that the signal range will make sense

    """ Confirms that the signal is within an expected range (below 10mV)

        :rtype: Error raised if mV values exceed 10mV
    """
    datafile=dataextraction(filename)
    #csv_HR = csv.reader(HR)
    #next(csv_HR)
    #for row in csv_HR:
    for x in range(0,len(datafile)):
        if datafile[x,1]>=10: #check mV range for typical ECG Data
            raise TypeError('Data seems irregular, please check and try again')
    d = 1
    return d
# HR.close()


def HR_peakdetect(data_array):
    """ Returns a time array of times where peak was detected

    :param data_array: a 2-d array with time and voltage values
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

    return time_array
