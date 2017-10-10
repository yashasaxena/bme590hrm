import numpy as np
from scipy import signal
import csv
from fractions import Fraction
import sys

min_to_sec = 60
num_arg = 3
HR_data = np.array([0, 0])  # initialize a matrix to store data

class data:
    def __init__(self):
        self.imported_data = []  # intended attribute??? for yasha's processing subclass
        self.HR_data = []  # output used in peak detect. not sure if i need both of these lines?


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

    def columncheck(self, filename):
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

    def typecheck(self, filename):

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

self.HR_data = HR_data # need help on this too?? don't think this is needed?