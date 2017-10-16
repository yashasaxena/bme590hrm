import numpy as np
from scipy import signal
import csv
from fractions import Fraction
import sys


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


class Vitals:

    # num_arg = 3
    MIN_TO_SEC = 60

    def __init__(self, averaging_time, time_array):
        self.avg_hr_val = None
        self.inst_hr_val = None
        self.averaging_time = averaging_time
        self.time_array = time_array

    def hr_averaging(self):

        """
        .. function:: hr_averaging(averaging_time, tachy_limit = 100, brachy_limit = 60)

        Calculate the average HR based upon ECG data.


        :rtype: integer value of average HR
        """

        # check for valid num_args
        """
        try:
            num_arg == sys.argv
        except TypeError:
            print("Please input the correct number of arguments") 
        """
        # check if the averaging time was inputted as a fraction and convert to float
        try:
            test_fraction = Fraction(Vitals.averaging_time)
            Vitals.averaging_time = float(Fraction(test_fraction))
        except ValueError:
            print("That is not a valid fraction, float, or int")
            raise ValueError
        except ZeroDivisionError:
            print("You cannot divide by zero")
            raise ZeroDivisionError
        # check for non-zero averaging time
        if Vitals.averaging_time <= 0:
            print("Your averaging time input must be greater than zero.")
            raise ValueError

        # attempt to convert averaging time to float if it isn't a fraction
        try:
            Vitals.averaging_time = float(Vitals.averaging_time)
        except TypeError:
            print("Your averaging time input is not a a valid number, please input a number.")

        averaging_time_sec = Vitals.averaging_time * Vitals.MIN_TO_SEC

        # find the total acquisition time
        max_acq_time = max(Vitals.time_array)

        # check if averaging time is longer than the ECG acquisition time
        if averaging_time_sec > max_acq_time:
            print("Your averaging time is longer than the ECG acquisition time, try a new value")
            raise ValueError

        final_ind = 0
        final_min = abs(Vitals.time_array[0] - averaging_time_sec)
        # XXX = []
        # test_pos = np.argwhere(min(abs(time_array - averaging_time_sec)))
        # print(test_pos)

        for i in range(0, len(Vitals.time_array)):

            min_val = abs(Vitals.time_array[i] - averaging_time_sec)
            if min_val < final_min:
                final_min = min_val
                final_ind = i

        # final_ind = np.argwhere(min(abs(time_array - averaging_time_sec)))
        # avg_index = (np.abs(time_array - averaging_time_sec)).argmin()

        time_array_sliced = Vitals.time_array[:final_ind+1]
        self.avg_hr_val = int(round((len(time_array_sliced))/Vitals.averaging_time))
        dt_first_beat = Vitals.time_array[2] - Vitals.time_array[1]
        self.inst_hr_val = Vitals.MIN_TO_SEC * 1 / dt_first_beat


class Diagnosis:

    def __init__(self, average_hr_val, tachy_limit=100, brachy_limit=60):
        self.average_hr_val = average_hr_val
        self.tachy_limit = tachy_limit
        self.brachy_limit = brachy_limit
        self.tachy_result = None
        self.brachy_result = None

    def tachy(self):

        """
        .. function:: tachy(self)

        Determine if tachycardia occurred during ECG acquisition.

        :rtype: bool (True if tachycardia is  present, False if tachycardia is not present)
        """

        # Ensure the brachycardia limit is above 0
        if Diagnosis.tachy_limit <= 0:
            print("Your tachycardia limit must be greater than zero.")
            raise ValueError
        # Convert the brachycardia limit to type float
        try:
            Diagnosis.tachy_limit = float(Diagnosis.tachy_limit)
        except ValueError:
            print("Your tachycardia threshold input is not a number, please input a number.")
        # Evaluate whether tachycardia is present based upon the average HR value calculated previously
        if Diagnosis.average_hr_val > Diagnosis.tachy_limit:
            print("Tachycardia was found!")

            self.tachy_result = True
        else:
            self.tachy_result = False

    def brachy(self):

        """
        .. function:: brachy(average_hr_val, brachy_limit)

        Determine if brachycardia occurred during ECG acquisition.

        :rtype: bool (True if brachycardia is present, False if brachycardia is not present)
        """
        # Ensure the brachycardia limit is above 0
        if Diagnosis.brachy_limit <= 0:
            print("Your brachycardia limit must be greater than zero.")
            raise ValueError
        # Convert the brachycardia limit to type float
        try:
            Diagnosis.brachy_limit = float(Diagnosis.brachy_limit)
        except ValueError:
            print("Your brachycardia threshold input is not a number, please input a number.")
        # Evaluate whether brachycardia is present based upon the average HR value calculated previously
        if Diagnosis.average_hr_val < Diagnosis.brachy_limit:
            print("Brachycardia was found!")
            self.brachy_result = True

        else:
            self.brachy_result = False
