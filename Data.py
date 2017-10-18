import numpy as np


class Data:

    def __init__(self, filename='ecg_testdata.csv'):
        self.filename_array = np.genfromtxt(filename,
                                            delimiter=',', skip_header=1, missing_values='', filling_values=0.0)
        self.hr_data = np.genfromtxt(filename, delimiter=',',
                                     skip_header=1, missing_values='', filling_values=0.0)
        self.column_check_result = None
        self.value_type_result = None
        self.value_range_result = None
        self.f = np.array([0, 0])

    def column_check(self):
        """ Confirms that data is arranged in 2 columns
        :param: csv file with HR data
        :rtype: Error raised if data structure is incorrect
        """

        if self.filename_array.shape[1] != 2:
            print("Your file does not have 2 columns.")
            self.column_check_result = False
            raise TypeError
        else:
            self.column_check_result = True

    def value_range(self):
        """ Confirms that the signal is within an expected range (below 300mV)
        :param: csv file with HR data
        :rtype: Error raised if mV values exceed 300mV
        """

        # rows, columns = self.filename_array.shape
        for row in range(len(self.filename_array)):
            if self.filename_array[row, 1] >= 300:
                print("Your voltage values seem too high!")
                self.value_range_result = False
                raise ValueError
            else:
                self.value_range_result = True

    def extraction(self):
        """ Opens CSV file, runs unit tests to throw any needed errors, then creates an array with any gaps in
        data filled with averages of previous/next data
        :param: csv file with HR data
        :rtype: hr_data as the matrix for data analysis """

        try:
            self.column_check()
        except Exception as ex:
            print(ex)
            return

        # try:
        #     self.value_type()
        # except Exception as ex:
        #     print(ex)
        #     return

        try:
            self.value_range()
        except Exception as ex:
            print(ex)
            return

        f = self.hr_data
        for x in range(1, len(f[:, 0])):
            if f[x, 0] == 0.0:
                f[x, 0] = (f[x + 1, 0]+f[x - 1, 0]) / 2

        self.hr_data = f
