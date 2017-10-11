import numpy as np
from scipy import signal
import csv
from fractions import Fraction
import sys

min_to_sec = 60
num_arg = 3
HR_data = np.array([0, 0])  # initialize a matrix to store data

class Data:
    def __init__(self):
        self.HR_data = []  # att used in peak detect

    def extraction(self, filename):
        #  need to fix the fxn name elsewhere - used to be called dataextraction
        """ Opens CSV file, converts all numbers to float type, then creates an array to append rows

        :rtype: HR_data as the matrix for data analysis """

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

    def columncheck(filename):
        """ Confirms that data is arranged in 2 columns

        :rtype: Error raised if data structure is incorrect
        """

        with open(filename) as HR:
            csv_HR = csv.reader(HR)
            for row in csv_HR:
                if len(row)!= 2:
                    raise TypeError('Data is not organized in 2 columns, please check and try again.')
        a=1
        return a

    def typecheck(filename):

        """ Confirms there are no strings in the data
            :rtype: Error raised if data type is incorrect
        """

        datafile = dataextraction(filename)
        #csv_HR = csv.reader(HR)
        #next(csv_HR)
        #for row in csv_HR:
        for x in range(0,len(datafile)):
            if (type(datafile[x,1])== str):
                raise TypeError('Data is not of correct type, please check and try again')
        c=1
        return c

    def datapracticality(filename):
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
        d=1
        return d

    HR.close()

    self.HR_data.append(HR_data)

class Processing:
# pseudocode for processing subclass
    def __init__(self):
        self.t = []

    def ecg_peakdetect(self, data_array):
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


