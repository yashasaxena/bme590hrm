import csv
import numpy as np
import matplotlib.pyplot as plt
import HR_allfuncs as hr

def extraction(filename):
    """ Opens CSV file, converts all numbers to float type,
    then creates an array to append rows
    :param filename: csv file with HR data
    :rtype: HR_data as the matrix for data analysis """
    HR_data = np.array([0, 0])
    with open(filename) as HR:
        csv_hr = csv.reader(HR)
        next(csv_hr)
        for row in csv_hr:
            time = float(row[0])
            signal = float(row[1])
            HR_data = np.vstack([HR_data, [time, signal]])

    HR.close()
    HR_data = np.delete(HR_data, 0, axis=0)

    return HR_data

def ecg_peakdetect(data_array):
    """ Peak detection function returning a
    time array of times when peak was detected
    :param data_array: a 2-d array with time
    and voltage values
    :rtype: array"""
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
    #inverted_data = np.multiply(-1, pre_processing)
    # heart rates to test, lower spectrum to higher spectrum
    #rates = np.array(range(40, 200)) / 60
    t_step = data_array[1, 0] - data_array[0, 0]
    # sampling frequency that provides number of steps in 1 second
    fs = int(1 / t_step)

    max_peak = np.max(pre_processing)

    threshold = max_peak - 0.5*max_peak
    peakind = []
    time_array = []
    time_array_clean = []

    for c in range(0, len(pre_processing)):
        if pre_processing[c] >= threshold:
            peakind.append(c)
            time_array.append(data_array[c,0])

    time_differences = np.diff(time_array)

    for d in range(0, len(time_differences)):
        if time_differences[d] > 0.3:
            time_array_clean.append(time_array[d])


    time_array_clean.append(time_array[-1])
    return time_array_clean

# for x in glob.glob('/test_data/Tests1-27/*.csv'):
#     HR_data = extraction(x)
#     indices = ecg_peakdetect(HR_data)
#     plt.interactive(False)
#     plt.plot(HR_data, markevery=indices)
#     plt.show()


HR_data = extraction('./test_data/Tests1_27/test_data5.csv')
indices = ecg_peakdetect(HR_data)
x = hr.Vitals()
x.hr_averaging(5/60, indices)
avg_time = x.avg_hr_val

print(indices)
print(avg_time)

plt.plot(HR_data[:,0], HR_data[:,1])

#plt.plot(HR_data[indices, 0], HR_data[indices, 1], 'r')

plt.show()

