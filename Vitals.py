from fractions import Fraction
import math


class Vitals:

    MIN_TO_SEC = 60

    def __init__(self, averaging_time, peak_time_array, time_array):
        """
        Initialize Vitals class. Stores average and instantaneous HR values,
        calculated using the inputted time_array
        and user-specified averaging time.

        :param averaging_time: user inputted averaging time
        :param peak_time_array: holds time values at an identified peak
        :param time_array: original time array that was passed in
        """
        self.avg_hr_val = None
        self.inst_hr_array = []
        self.averaging_time = averaging_time
        self.peak_time_array = peak_time_array
        self.time_array = time_array
        self.hr_averaging()

    def hr_averaging(self):

        """
        .. function:: hr_averaging(self)

        Calculate the average HR based upon ECG data. Stores attributes with
        instant and average HR values.

        """

        # convert fraction averaging time input to float
        try:
            test_fraction = Fraction(self.averaging_time)
            self.averaging_time = float(Fraction(test_fraction))
        except ValueError:
            print("That is not a valid fraction, float, or int")
            raise ValueError
        except ZeroDivisionError:
            print("You cannot divide by zero")
            raise ZeroDivisionError
        # check for non-zero averaging time
        if self.averaging_time <= 0:
            print("Your averaging time input must be greater than zero.")
            raise ValueError

        # attempt to convert averaging time to float if it isn't a fraction
        try:
            self.averaging_time = float(self.averaging_time)
        except TypeError:
            print("Your averaging time input is not a a valid number,"
                  " please input a number.")

        averaging_time_sec = self.averaging_time * self.MIN_TO_SEC

        # find the total acquisition time
        max_acq_time = self.peak_time_array[-1]

        # check if averaging time is longer than the ECG acquisition time
        if averaging_time_sec > max_acq_time:
            print("Your averaging time is longer than the ECG acquisition time"
                  ", try a new value")
            averaging_time_sec = max_acq_time
            raise ValueError
        # find the smallest distance between the averaging_time
        final_ind = 0
        final_min = abs(self.peak_time_array[0] - averaging_time_sec)

        # for i in range(1, len(self.time_array)):
        #     if i == 1:
        #         dt_first_beat = self.time_array[i-1]
        #         self.inst_hr_array.insert(i-1, self.MIN_TO_SEC
        #                                   * (1/dt_first_beat))
        #
        #     dt_first_beat = self.time_array[i] - self.time_array[i-1]
        #     self.inst_hr_array.insert(i-1, self.MIN_TO_SEC * 1/dt_first_beat)
        #
        #     # self.inst_hr_array.insert(i, self.MIN_TO_SEC * 1 / dt_first_beat)
        #     self.inst_hr_array[i-1] = int(round(self.inst_hr_array[i-1]))

        # calculate instantaneous hr array
        for i in range(0, len(self.peak_time_array) - 1):

            dt_first_beat = self.peak_time_array[i + 1] \
                            - self.peak_time_array[i]
            self.inst_hr_array.insert(i, self.MIN_TO_SEC * 1 / dt_first_beat)
            self.inst_hr_array[i] = int(round(self.inst_hr_array[i]))

        # calculate average hr array
        for i in range(0, len(self.peak_time_array)):

            min_val = abs(self.peak_time_array[i] - averaging_time_sec)
            if min_val < final_min:
                final_min = min_val
                final_ind = i

        time_array_sliced = self.peak_time_array[:final_ind+1]
        self.avg_hr_val = \
            int(round((len(time_array_sliced))/self.averaging_time))
