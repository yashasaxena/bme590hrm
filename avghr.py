import numpy as np
import sys
import HR_peakdetect

min_to_sec = 60
num_arg = 3


def hr_averaging(time_array, mv_array, averaging_time):

    try:
        num_arg == sys.argv
    except ValueError:
        print("Please input the correct number of arguments")

    try:
        averaging_time = complex(averaging_time)
        averaging_time = averaging_time.real
    except ValueError:
        print("Your averaging_time input is not a number, please input a number.")

    averaging_time_sec = averaging_time * min_to_sec
    HR_peakdetect()
    avg_index = (np.abs(time_array - averaging_time_sec)).argmin()

    mv_array_sliced = mv_array[:avg_index]

    average_hr_val = (len(mv_array_sliced))/averaging_time

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
