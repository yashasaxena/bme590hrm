
import csv
import numpy as np

HR_data = np.array([0, 0])  # initialize a matrix to store data

#Open CSV
#filename = 'ecg_data.csv'

def dataextraction(filename):

    """ """
    """..function: dataextraction():
     opens CSV file, converts all numbers to float type, then creates an array to append rows """

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

    """"""
    """..function columncheck():
     makes sure the data is arranged in 2 columns"""

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
    """"""
    """..function: datatypecheck():
     makes sure there are no strings in the data"""
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
    """"""
    """..function: datapracticality():
     checks that the signal is within an expected range (below 10mV"""
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
