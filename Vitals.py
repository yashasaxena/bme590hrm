from fractions import Fraction


class Vitals:

    MIN_TO_SEC = 60

    def __init__(self, averaging_time, time_array):
        """
        Initialize Vitals class. Stores average and instantaneous HR values, calculated using the inputted time_array
        and user-specified averaging time.

        :param averaging_time: user inputted averaging time
        :param time_array: time_array that consists of identified peaks
        """
        self.avg_hr_val = None
        self.inst_hr_val = None
        self.averaging_time = averaging_time
        self.time_array = time_array
        self.hr_averaging()


    def hr_averaging(self):

        """
        .. function:: hr_averaging(self)

        Calculate the average HR based upon ECG data. Stores attributes with instant and average HR values.

        """

        # check if the averaging time was inputted as a fraction and convert to float
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
            print("Your averaging time input is not a a valid number, please input a number.")

        averaging_time_sec = self.averaging_time * self.MIN_TO_SEC

        # find the total acquisition time
        max_acq_time = max(self.time_array)

        # check if averaging time is longer than the ECG acquisition time
        if averaging_time_sec > max_acq_time:
            print("Your averaging time is longer than the ECG acquisition time, try a new value")
            raise ValueError
        # find the smallest distance between the averaging_time
        final_ind = 0
        final_min = abs(self.time_array[0] - averaging_time_sec)

        for i in range(0, len(self.time_array)):

            min_val = abs(self.time_array[i] - averaging_time_sec)
            if min_val < final_min:
                final_min = min_val
                final_ind = i

        time_array_sliced = self.time_array[:final_ind+1]
        self.avg_hr_val = int(round((len(time_array_sliced))/self.averaging_time))
        dt_first_beat = self.time_array[2] - self.time_array[1]
        self.inst_hr_val = self.MIN_TO_SEC * 1 / dt_first_beat
