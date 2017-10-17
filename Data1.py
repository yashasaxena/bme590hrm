import numpy as np
import csv


class Data:
    def __init__(self, filename):
        self.HR_data = np.array([0, 0])
        self.extraction(filename)
        self.readfile = []

    def read(self, filename):
        self.readfile = np.genfromtxt(filename, delimiter=',', skip_header=1)

    def extraction(self, filename):
        """ Opens CSV file, converts all numbers to float type,
        then creates an array to append rows
        :param filename: csv file with HR data
        :rtype: HR_data as the matrix for data analysis """

        try:
            self.column_check(filename)
        except Exception as ex:
            print(ex)
            return

        try:
            self.type_check()
        except Exception as ex:
            print(ex)
            return

        try:
            self.practicality_check()
        except Exception as ex:
            print(ex)
            return

        with open(filename) as HR:
            csv_hr = csv.reader(HR)
            next(csv_hr)
            for row in csv_hr:
                if len(row) != 2:
                    time = float(row[0])
                    signal = float(row[1])
                    self.HR_data = np.vstack([self.HR_data, [time, signal]])

        HR.close()
        self.HR_data = np.delete(self.HR_data, 0, axis=0)

        return self.HR_data

    def column_check(self, filename):
        """ Confirms that data is arranged in 2 columns
        :param filename: csv file with HR data
        :rtype: Error raised if data structure is incorrect
        """
        with open(filename) as HR:
            csv_hr = csv.reader(HR)
            for row in csv_hr:
                if len(row) != 2:
                    raise TypeError('Data is not organized in 2 columns, '
                                    'please check and try again.')
        a = 1
        return a

    def type_check(self):
        """ Confirms there are no strings in the data
        :param csv file with HR data
        :rtype: Error raised if data type is incorrect
        """
        datafile = self.readfile
        for x in range(0, len(datafile)):
            if type(datafile[x, 1] == str):
                raise TypeError('Data is not of correct type, please check and try again')

        c = 1
        return c

    def practicality_check(self):
        """ Confirms that the signal is within an
        expected range (below 300mV)
        :param: csv file with HR data
        :rtype: Error raised if mV values exceed 10mV
        """
        datafile = self.readfile
        for x in range(0, len(datafile)):
            if datafile[x, 1] >= 300:  # check mV range for typical ECG Data
                raise TypeError('Data seems irregular, please check and try again')
        d = 1
        return d