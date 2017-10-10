import numpy as np
from scipy import signal
import csv
from fractions import Fraction
import sys

min_to_sec = 60
num_arg = 3
HR_data = np.array([0, 0])  # initialize a matrix to store data

#Open CSV
#filename = 'ecg_data.csv'

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
    HR_data = np.delete(HR_data, (0), axis=0)

    return HR_data


# DATA VALIDATION
def columncheck(filename): #checks number of columns


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

#def headearcheck(filename):  # checks presence of headers
#    with open(filename) as HR:
#        csv_HR = csv.reader(HR)
#        header_row = next(csv_HR)
#        if (type(heder_row[0]) != str) or (type(header_row[1]) != str):
#            raise ValueError('Data headers are not present, please check and try again.')
#   b=1
#   return b

def datatypecheck(filename):  # checks float/int

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
    d=1
    return d

#HR.close()


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


def instHR(t_array):
    """ Calculates instant heart rate from peak time array

        :param t_array: a 1-d list with time values of peaks
    """
    dt_first_beat = t_array[2] - t_array[1]

    instHR = 1/dt_first_beat * 60

    return instHR





def hr_averaging(averaging_time,time_array):

    """
    .. function:: hr_averaging(averaging_time, tachy_limit = 100, brachy_limit = 60)

    Calculate the average HR based upon ECG data.

    :param averaging_time: time period (in min) used to calculate average HR
    :param time_array: the time_array after peak_detect has been called
    :param brachy_limit: sets the brachycardia threshold limit, defaults to 100
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
        print("Your averaging time input is not a a valid number, please input a number.")

    averaging_time_sec = averaging_time * min_to_sec

    # extract hr data from .csv file
    max_acq_time = max(time_array)

    # check if averaging time is longer than ECG acq time
    if averaging_time_sec > max_acq_time:
        print("Your averaging time is longer than the ECG acquisition time, try a new value")
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
    average_hr_val = int(round((len(time_array_sliced))/averaging_time))
    return average_hr_val


def tachy(average_hr_val, tachy_limit):

    """ Detects if tachycardia occured during ECG acquisition.

    :param average_hr_val: average HR value calculated from hr_averaging()
    :param tachy_limit: tachycardia limit to be specified
    :rtype: bool (True if tachycardia is not present, False if tachycardia is present)
    """

    # check for non-zero averaging time
    if tachy_limit <= 0:
        print("Your tachycardia limit must be greater than zero.")
        raise ValueError

    try:
        tachy_limit = complex(tachy_limit)
        tachy_limit = tachy_limit.real
    except ValueError:
        print("Your tachycardia threshold input is not a number, please input a number.")

    if average_hr_val > tachy_limit:
        print("Tachycardia was found!")
        return True
    else:
        return False


def brachy(average_hr_val, brachy_limit):

    """ Detects if brachycardia occured during ECG acquisition.

    :param average_hr_val: average HR value calculated from hr_averaging()
    :param brachy_limit: brachycardia limit to be specified
    :rtype: bool (True if brachycardia is not present, False if brachycardia is present)
    """

    if brachy_limit <= 0:
        print("Your brachycardia limit must be greater than zero.")
        raise ValueError
    try:
        brachy_limit = complex(brachy_limit)
        brachy_limit = brachy_limit.real
    except ValueError:
        print("Your brachycardia threshold input is not a number, please input a number.")

    if average_hr_val < brachy_limit:
        print("Brachycardia was found!")
        return True

    else:
        return False
