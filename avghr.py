import numpy as np
import sys
import HR_peakdetect
import datavalidation_code

min_to_sec = 60
num_arg = 1


def hr_averaging(averaging_time):

    try:
        num_arg == sys.argv
    except TypeError:
        print("Please input the correct number of arguments")

    try:
        averaging_time = complex(averaging_time)
        averaging_time = averaging_time.real
    except ValueError:
        print("Your averaging_time input is not a number, please input a number.")

    hr_data = datavalidation_code.dataextraction("ecg_data.csv")

    time_list = HR_peakdetect.HR_peakdetect(hr_data)

    time_array = np.asarray(time_list)

    averaging_time_sec = averaging_time * min_to_sec

    avg_index = (np.abs(time_array - averaging_time_sec)).argmin()

    time_array_sliced = time_array[:avg_index]

    average_hr_val = (len(time_array_sliced))/averaging_time

    return average_hr_val


def tachy(average_hr_val, tachy_limit=100):

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
