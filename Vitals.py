from fractions import Fraction
import numpy as np


class Vitals:

    MIN_TO_SEC = 60

    def __init__(self, peak_time_array, time_array, averaging_time=.25, ):
        """
        Initialize Vitals class. Stores average and instantaneous HR values,
        calculated using the inputted time_array
        and user-specified averaging time.

        :param averaging_time: user inputted averaging time
        :param peak_time_array: holds time values at an identified peak
        :param time_array: original time array that was passed in
        """
        self.avg_hr_array = []
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
        except ValueError:
            print("Your averaging time input is not a a valid number,"
                  " please input a number.")

        averaging_time_sec = self.averaging_time * self.MIN_TO_SEC

        # find the total acquisition time
        max_acq_time = max(self.peak_time_array)

        # check if averaging time is longer than the ECG acquisition time
        if averaging_time_sec > max_acq_time:
            print("Your averaging time is longer than the ECG acquisition time"
                  ", try a new value")
            raise ValueError

        # calculate instantaneous hr array
        for i in range(0, len(self.peak_time_array) - 1):

            dt_first_beat = self.peak_time_array[i + 1] \
                            - self.peak_time_array[i]
            self.inst_hr_array.insert(i, self.MIN_TO_SEC * 1 / dt_first_beat)
            self.inst_hr_array[i] = int(round(self.inst_hr_array[i]))

        # initialize variables for interpolated inst_hr_array
        temp_inst_hr_array = []
        lower_bound = self.peak_time_array[0]
        upper_bound = self.peak_time_array[1]
        counter = 0

        # interpolate instantaneous hr values for all peak times
        for time in self.time_array:
            # append first inst_hr for times before first peak
            if time < self.peak_time_array[0]:
                temp_inst_hr_array.append(self.inst_hr_array[0])

            # append the inst_hr value from the inter-peak time interval
            elif lower_bound <= time <= upper_bound:
                temp_inst_hr_array.append(self.inst_hr_array[counter])

            # append next inst_hr value after passing the inter-peak interval
            elif time > upper_bound:
                lower_bound = upper_bound
                counter = counter + 1
                upper_bound = temp_inst_hr_array[counter]
                temp_inst_hr_array.append(self.inst_hr_array[counter])
            # append last inter-peak inst_hr value for times after final peak
            elif time > max(self.peak_time_array):
                temp_inst_hr_array.append(self.inst_hr_array[
                                              max(self.peak_time_array)])
        # set inst_hr_array to the interpolated inst_hr_array
        self.inst_hr_array = temp_inst_hr_array

        # find the smallest distance between the averaging_time
        final_ind = 0
        final_min = abs(self.time_array[0] - averaging_time_sec)
        # final_min = abs(self.time_array[0] - averaging_time_sec)

        for i in range(0, len(self.time_array)):

            min_val = abs(self.time_array[i] - averaging_time_sec)
            if min_val < final_min:
                final_min = min_val
                final_ind = i
        # for i in range(0, len(self.peak_time_array)):
        #
        #     min_val = abs(self.peak_time_array[i] - averaging_time_sec)
        #     if min_val < final_min:
        #         final_min = min_val
        #         final_ind = i

        # use a moving average to calculate avg_hr from inst_hr

        self.avg_hr_array = np.convolve(self.inst_hr_array,
                                        np.ones(final_ind) / final_ind, 'same')
        self.avg_hr_array = np.around(self.avg_hr_array)
        self.avg_hr_array = self.avg_hr_array.astype(int)

        # # calculate average hr array
        # time_array_sliced = self.peak_time_array[:final_ind+1]
        # self.avg_hr_val = \
        #     int(round((len(time_array_sliced))/self.averaging_time))
