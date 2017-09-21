import numpy as np

def hr_averaging(time_array, mv_array, averaging_time):

    averaging_time_sec = averaging_time * 60
    avg_index = (np.abs(time_array - averaging_time_sec)).argmin()

    mv_array_sliced = mv_array[:avg_index]

    average_hr_val = (len(mv_array_sliced))/averaging_time

    return average_hr_val

def tachy(average_hr_val):
    if average_hr_val > 100:
        print("Tachycardia was found!")
        return False
    else:
        return True

def brachy(average_hr_val):

    if average_hr_val < 60:
        print("Brachycardia was found!")
        return False

    else:
        return True
