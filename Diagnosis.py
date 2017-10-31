class Diagnosis:

    def __init__(self, hr_array, tachy_limit=100, brachy_limit=60):
        """
        Initializes Diagnosis class for brachycardia and tachycardia tests
        :param hr_array: hr_array that is compared w/ brachy and tachy limits
        :param tachy_limit: user inputted tachycardia limit (default is 100)
        :param brachy_limit: user inputted brachycardia limit (default is 60)
        """
        self.hr_array = hr_array
        self.tachy_limit = tachy_limit
        self.brachy_limit = brachy_limit
        self.tachy_result = []
        self.brachy_result = []
        self.tachy()
        self.brachy()

    def tachy(self):

        """
        .. function:: tachy(self)
        Determine if tachycardia occurred during ECG acquisition. Stores
        boolean array of tachycardia result.

        """

        # Ensure the brachycardia limit is above 0
        if self.tachy_limit <= 0:
            print("Your tachycardia limit must be greater than zero.")
            raise ValueError
        # Convert the brachycardia limit to type float
        try:
            self.tachy_limit = float(self.tachy_limit)
        except TypeError:
            print("Your tachycardia threshold input is not a number,"
                  " please input a number.")
        # Evaluate if tachycardia is present in inst_hr_array
        for i in range(0, len(self.hr_array)):
            if self.hr_array[i] > self.tachy_limit:
                self.tachy_result.insert(i, True)

            else:
                self.tachy_result.insert(i, False)

    def brachy(self):

        """
        .. function:: brachy(self)
        Determine if brachycardia occurred during ECG acquisition. Stores
        boolean array of brachycardia result.

        """
        # Ensure the brachycardia limit is above 0
        if self.brachy_limit <= 0:
            print("Your brachycardia limit must be greater than zero.")
            raise ValueError
        # Convert the brachycardia limit to type float
        try:
            self.brachy_limit = float(self.brachy_limit)
        except ValueError:
            print("Your brachycardia threshold input is not a number,"
                  " please input a number.")
        # Evaluate if brachycardia is present in inst_hr_array
        for i in range(0, len(self.hr_array)):
            if self.hr_array[i] < self.brachy_limit:
                self.brachy_result.insert(i, True)
            else:
                self.brachy_result.insert(i, False)
