import numpy as np
import scipy
from scipy import signal
import csv
import matplotlib.pyplot as plt

def dataextraction(filename):
    HR_data = np.array([0,0])
    
    with open(filename) as HR:
        csv_HR = csv.reader(HR)
#        data = list(csv_HR)
#        N = len(data)
        next(csv_HR)
        for row in csv_HR:
            time = float(row[0])
            signal = float(row[1])
            HR_data = np.vstack([HR_data, [time,signal]])

    HR.close()
    HR_data = np.delete(HR_data,(0),axis=0)


    return HR_data

def HR_peakdetect(data_array): 
    # peak detection function based on variable threshold method
     diff_filter = 0.125*np.array([2,1,-1,-2])
     # differentiation process window, baseline correction
     pre_processing = data_array[:,1]
     pre_processing = np.convolve(pre_processing,diff_filter,'same')
#     pre_processing = data_array[:, 1].astype(complex)
     # hilbert transform
#     pre_processing = scipy.signal.hilbert(data_array[:,1])
#     pre_processing = pre_processing.astype(float)
     data_array[:,1] = pre_processing
     
     t_step = data_array[0,0]-data_array[1,0]
     #first_peakind = signal.find_peaks_cwt(data_array[:,1],np.arange(1,750))
     peakind = signal.find_peaks_cwt(data_array[:,1],np.arange(1,500))
     
     #calculate a threshold based on standard deviation of detected peaks in 1 sec sampling
     max_peak = max(pre_processing)

     time_array = []
     for c in range(0,len(peakind)): 
         y = peakind[c]
         time_array.append(data_array[y,0])

     return time_array




# test script goes here
heart_rate_data = dataextraction('/Users/yashasaxena/PycharmProjects/bme590hrm/ecg_data.csv')
t_values = HR_peakdetect(heart_rate_data)


plt.plot(heart_rate_data)
plt.ylim(-0.1,0.1)
plt.show()
