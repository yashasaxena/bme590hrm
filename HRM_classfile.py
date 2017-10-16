import numpy as np
from scipy import signal
import csv
from fractions import Fraction
import sys

min_to_sec = 60
num_arg = 3


class Data:
    def __init__(self, filename):
        self.HR_data = np.array([0, 0])
        self.extraction(filename)

    def extraction(self, filename):
        """ Opens CSV file, converts all numbers to float type,
        then creates an array to append rows

        :param filename: csv file with HR data
        :rtype: HR_data as the matrix for data analysis """

        try:
            self.column_check(filename)
        except:
            #  placeholder

        with open(filename) as HR:
            csv_hr = csv.reader(HR)
            next(csv_hr)
            for row in csv_hr:
                if len(row) != 2:
                    time = float(row[0])
                    signal = float(row[1])
                self.HR_data = np.vstack([self.HR_data, [time, signal]])

        HR.close()
        self.HR_data = np.delete(self.HR_data, 0, axis=0)

        return self.HR_data

    def column_check(self, filename):
        """ Confirms that data is arranged in 2 columns

        :param filename: csv file with HR data
        :rtype: Error raised if data structure is incorrect
        """

        with open(filename) as HR:
            csv_hr = csv.reader(HR)
            for row in csv_hr:
                if len(row) != 2:
                    raise TypeError('Data is not organized in 2 columns, '
                                    'please check and try again.')
        a = 1
        return a

    def type_check(self, filename):

        """ Confirms there are no strings in the data

        :param filename: csv file with HR data
        :rtype: Error raised if data type is incorrect
        """

        datafile = self.HR_data;
        for x in range(0, len(datafile)):
            if type(datafile[x, 1]) == str:
                raise TypeError('Data is not of correct type, '
                                'please check and try again')
        c = 1
        return c

    def practicality_check(self, filename):
        """ Confirms that the signal is within an
        expected range (below 10mV)

        :param filename: csv file with HR data
        :rtype: Error raised if mV values exceed 10mV
        """

        datafile = Data.extraction(self, filename)
        for x in range(0, len(datafile)):
            if datafile[x, 1] >= 10:
                raise TypeError('Data seems irregular, '
                                'please check and try again')
        d = 1
        return d


class Processing:
    def __init__(self):
        self.t = []

    def ecg_peakdetect(self, data_array):
        """ Peak detection function returning a
        time array of times when peak was detected

        :param data_array: a 2-d array with time
        and voltage values
        :rtype: array
        """
        # peak detection function based
        # on variable threshold method
        diff_filter = 0.125 * np.array([2, 1, -1, -2])
        # differentiation process
        # window, baseline correction
        pre_processing = data_array[:, 1]
        pre_processing = np.convolve(pre_processing,
                                     diff_filter, 'same')
        # inverting data because negative
        # peaks have less peak noise surrounding them
        inverted_data = np.multiply(-1, pre_processing)
        # heart rates to test, lower spectrum to higher spectrum
        rates = np.array(range(40, 200)) / 60
        t_step = data_array[1, 0] - data_array[0, 0]
        # sampling frequency that provides number of steps in 1 second
        fs = int(1 / t_step)
        peakind = signal.find_peaks_cwt(inverted_data, fs / rates / 10)

        time_array = []

        for c in range(0, len(peakind)):
            y = peakind[c]
            time_array.append(data_array[y, 0])

        self.t = time_array


class Vitals:

    def __init__(self):
        self.avg_hr_val = float
        self.inst_hr_val = float

    def hr_averaging(self, averaging_time, time_array):
        num_arg = 3
        min_to_sec = 60
        """ Calculate the average HR based upon ECG data.

        :param averaging_time: time period (in min) used
        to calculate average HR
        :param time_array: the time_array after peak_detect has been called
        :rtype: integer value of average HR
        """

        # check for valid num_args
        try:
            num_arg == sys.argv
        except TypeError:
            print("Please input the correct number of arguments")
        try:
            test_fraction = Fraction(averaging_time)
            averaging_time = float(Fraction(test_fraction))
        except ValueError:
            print("That is not a valid fraction, float, or int")
            raise ValueError
        except ZeroDivisionError:
            print("You cannot divide by zero")
            raise ZeroDivisionError
        # check for non-zero averaging time
        if averaging_time <= 0:
            print("Your averaging time input must be greater than zero.")
            raise ValueError
        # convert averaging time to float
        try:
            averaging_time = float(averaging_time)
        except TypeError:
            print("Your averaging time input is not a a "
                  "valid number, please input a number.")

        averaging_time_sec = averaging_time * min_to_sec

        # extract hr data from .csv file
        max_acq_time = max(time_array)

        # check if averaging time is longer than ECG acq time
        if averaging_time_sec > max_acq_time:
            print("Your averaging time is longer than the "
                  "ECG acquisition time, try a new value")
            raise ValueError
        else:
            pass

        final_ind = 0
        final_min = abs(time_array[0] - averaging_time_sec)
        # XXX = []
        # test_pos = np.argwhere(min(abs(time_array - averaging_time_sec)))
        # print(test_pos)

        for i in range(0, len(time_array)):

            min_val = abs(time_array[i] - averaging_time_sec)
            if min_val < final_min:
                final_min = min_val
                final_ind = i

        # final_ind = np.argwhere(min(abs(time_array - averaging_time_sec)))
        # avg_index = (np.abs(time_array - averaging_time_sec)).argmin()

        time_array_sliced = time_array[:final_ind+1]
        self.avg_hr_val = int(
            round((len(time_array_sliced))/averaging_time))
        dt_first_beat = time_array[2] - time_array[1]
        self.inst_hr_val = min_to_sec * 1 / dt_first_beat


class Diagnosis:
    def __init__(self):
        self.tachy_result = bool
        self.brachy_result = bool

    def tachy(self, average_hr_val, tachy_limit=100):
        """ Determine if tachycardia occurred during ECG acquisition.

        :param average_hr_val: average HR value calculated from hr_averaging()
        :param tachy_limit: tachycardia limit to be specified
        :rtype: bool (True if tachycardia is not present,
        False if tachycardia is present)
        """

        # check for non-zero averaging time
        if tachy_limit <= 0:
            print("Your tachycardia limit must be greater than zero.")
            raise ValueError

        try:
            tachy_limit = complex(tachy_limit)
            tachy_limit = tachy_limit.real
        except ValueError:
            print("Your tachycardia threshold input "
                  "is not a number, please input a number.")

        if average_hr_val > tachy_limit:
            print("Tachycardia was found!")

            self.tachy_result = True
        else:
            self.tachy_result = False

    def brachy(self, average_hr_val, brachy_limit=60):

        """ Determine if brachycardia occurred during ECG acquisition.

        :param average_hr_val: average HR value calculated from hr_averaging()
        :param brachy_limit: brachycardia limit to be specified
        :rtype: bool (True if brachycardia is not present, F
        alse if brachycardia is present)
        """

        if brachy_limit <= 0:
            print("Your brachycardia limit must be greater than zero.")
            raise ValueError
        try:
            brachy_limit = complex(brachy_limit)
            brachy_limit = brachy_limit.real
        except ValueError:
            print("Your brachycardia threshold input is not a number, "
                  "please input a number.")

        if average_hr_val < brachy_limit:
            print("Brachycardia was found!")
            self.brachy_result = True

        else:
            self.brachy_result = False
