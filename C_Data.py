import numpy as np


class Data:

    def __init__(self, filename='ecg_testdata.csv'):
        self.filename_array = np.genfromtxt(filename, delimiter=',', skip_header=1)
        self.HR_data = np.array([0, 0])
        self.column_check_result = None
        self.value_type_result = None
        self.value_range_result = None

    def column_check(self):
        if self.filename_array.shape[1] != 2:
            print("Your file does not have 2 columns.")
            self.column_check_result = False
            raise TypeError
        else:
            self.column_check_result = True

    def value_type(self):
        #for row in range(self.filename_array.shape[1]):
           # if self.filename_array[row, 1] == np.nan
            if np.isnan(self.filename_array).any():
                print("The values in your array are not all numbers.")
                self.value_type_result = False
                raise TypeError
            else:
                self.value_type_result = True

    def value_range(self):
        # rows, columns = self.filename_array.shape
        for row in range(len(self.filename_array)):
            if self.filename_array[row, 1] >= 300:
                print("Your voltage values seem too high!")
                self.value_range_result = False
                raise ValueError
            else:
                self.value_range_result = True

    def test_data_is_good(self):
        good_test_data = Data('GoodData_UnitTest.csv')
        good_test_data.column_check()
        good_test_data.value_type()
        good_test_data.value_range()
        assert good_test_data.column_check_result is True
        assert good_test_data.value_type_result is True
        assert good_test_data.value_range_result is True