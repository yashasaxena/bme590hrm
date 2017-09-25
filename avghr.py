import numpy as np
import sys
import HR_peakdetect
import datavalidation_code
from fractions import Fraction

min_to_sec = 60
num_arg = 1


def hr_averaging(averaging_time):

    """
    .. function:: hr_averaging(averaging_time)

    Calculate the average HR based upon ECG data.

    :param averaging_time: time period (in min) used to calculate average HR
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
    hr_data = datavalidation_code.dataextraction("ecg_data.csv")
    orig_time_data = hr_data[:, 0]
    max_acq_time = max(orig_time_data)

    # check if averaging time is longer than ECG acq time
    if averaging_time_sec > max_acq_time:
        print("Your averaging time is longer than the ECG acquisition time, try a new value")
        raise ValueError
    else:
        pass

    # perform peak detection
    time_list = HR_peakdetect.HR_peakdetect(hr_data)
    print(len(time_list))
    time_array = np.asarray(time_list)

    final_ind = 0
    final_min = abs(time_array[0] - averaging_time_sec)
    XXX = []
    test_pos = np.argwhere(min(abs(time_array - averaging_time_sec)))
    print(test_pos)

    for i in range(0, len(time_array)):

        min_val = abs(time_array[i] - averaging_time_sec)
        print(min_val)

        if min_val < final_min:
            final_min = min_val
            final_ind = i

    print(final_ind)
    # final_ind = np.argwhere(min(abs(time_array - averaging_time_sec)))
    # avg_index = (np.abs(time_array - averaging_time_sec)).argmin()

    time_array_sliced = time_array[:final_ind+1]
    print(len(time_array_sliced))
    average_hr_val = int(round((len(time_array_sliced))/averaging_time))
    print(average_hr_val)
    return average_hr_val


def tachy(average_hr_val, tachy_limit=100):
    """
    .. function:: tachy(average_hr_val, tachy_limit)

    Determine if tachycardia occured during ECG acquisition.

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
        return False
    else:
        return True


def brachy(average_hr_val, brachy_limit=60):
    """
    .. function:: brachy(average_hr_val, brachy_limit)

    Determine if brachycardia occured during ECG acquisition.

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
        return False

    else:
        return True
