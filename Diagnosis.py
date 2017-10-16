class Diagnosis:

    def __init__(self, average_hr_val, tachy_limit=100, brachy_limit=60):
        """
        Initializes Diagnosis class for brachycardia and tachycardia tests
        :param average_hr_val: average HR which is calculated in the Vitals class
        :param tachy_limit: user inputted tachycardia limit (default is 100)
        :param brachy_limit: user inputted brachycardia limit (default is 60)
        """
        self.average_hr_val = average_hr_val
        self.tachy_limit = tachy_limit
        self.brachy_limit = brachy_limit
        self.tachy_result = None
        self.brachy_result = None
        self.tachy()
        self.brachy()


    def tachy(self):

        """
        .. function:: tachy(self)

        Determine if tachycardia occurred during ECG acquisition.

        """

        # Ensure the brachycardia limit is above 0
        if self.tachy_limit <= 0:
            print("Your tachycardia limit must be greater than zero.")
            raise ValueError
        # Convert the brachycardia limit to type float
        try:
            self.tachy_limit = float(self.tachy_limit)
        except ValueError:
            print("Your tachycardia threshold input is not a number, please input a number.")
        # Evaluate whether tachycardia is present based upon the average HR value calculated previously
        if self.average_hr_val > self.tachy_limit:
            print("Tachycardia was found!")

            self.tachy_result = True
        else:
            self.tachy_result = False

    def brachy(self):

        """
        .. function:: brachy()

        Determine if brachycardia occurred during ECG acquisition.

        """
        # Ensure the brachycardia limit is above 0
        if self.brachy_limit <= 0:
            print("Your brachycardia limit must be greater than zero.")
            raise ValueError
        # Convert the brachycardia limit to type float
        try:
            self.brachy_limit = float(self.brachy_limit)
        except ValueError:
            print("Your brachycardia threshold input is not a number, please input a number.")
        # Evaluate whether brachycardia is present based upon the average HR value calculated previously
        if self.average_hr_val < self.brachy_limit:
            print("Brachycardia was found!")
            self.brachy_result = True

        else:
            self.brachy_result = False
