
import csv
import numpy as np

HR_data = [0, 0]  # initialize a matrix to store data

#Open CSV
filename = 'ecg_data.csv'


# DATA VALIDATION
def columncheck(filename): #checks number of columns
    with open(filename) as HR:
        csv_HR = csv.reader(HR)
    for row in csv_HR:
        if len(row)!= 2:
            raise TypeError('Data is not organized in 2 columns, please check and try again.')

def headercheck(filename):  # checks presence of headers
    with open(filename) as HR:
         csv_HR = csv.reader(HR)
    header_row = csv_HR.next() #verify that this accesses the very first row
    if (type(header_row[0]) != str) or (type(header_row[1]) != str):
               raise TypeError('Data headers are not present, please check and try again.')

def datatypecheck(filename):  # checks float/int
    with open(filename) as HR:
         csv_HR = csv.reader(HR)
    next(csv_HR)
    for row in csv_HR:
        for x in range(0,2):
            if (type(row[x])= str):
                raise TypeError('Data is not of correct type, please check and try again')

def datapracticality(filename):  # checks that the signal range will make sense
    with open(filename) as HR:
        csv_HR = csv.reader(HR)
    next(csv_HR)
    for row in csv_HR:
            if row[2]>=100: #check mV range for typical ECG Data
                raise TypeError('Data seems irregular, please check and try again')

#converting to numpy array
def dataextraction(filename):
    with open(filename) as HR:
        csv_HR = csv.reader(HR)
    next(csv_HR)
    for row in csv_HR:
        time = float(row[0])
        signal = float(row[1])
        HR_data=np.vstack([HR_data, [time, signal]])


HR.close()
