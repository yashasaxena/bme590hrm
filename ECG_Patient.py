import numpy as np
from scipy import signal

# import subclass files
import Data
import Processing
import Vitals
import Diagnosis

class Patient:
    def __init__(self, avg_time, filename = 'ecg_data.csv', tachy_limit=100,
                 brachy_limit=60, return_file = 'HR_Specs.txt'):
        """
        Instantiates patient class

        :param avg_time:
        :param filename:
        :param tachy_limit:
        :param brachy_limit:
        :param return_file:

        """

        self.data = Data(filename)
        self.pd_processing = Processing(self.data.HR_array)
        try:
            self.vitals = Vitals.Vitals(avg_time, self.pd_processing.t)
        except (ValueError,ZeroDivisionError):
            print("The program has encountered an error. Please view the error log in your console.")
        try:
            self.diagnosis = Diagnosis.Diagnosis(self.vitals.avg_HR, tachy_limit, brachy_limit)
        except ValueError:
            print("You inputted a brachycardia or tachycardia limit below zero. Are you sure you want to do that?")

    def create_patient_file(self):
        '''Generates a text file with relevant heart patient information

        :rtype: text file
        '''
        hr_txt = open(return_file, "w")
        hr_txt.write("Patient Name: Heart Patient Dude\n")
        hr_txt.write("Patient file: " + file_name + "\n")
        hr_txt.write("Estimated instant heart rate: {:.3f}\n".format(instant_hr))
        hr_txt.write("Estimated average heart rate: {:.3f}\n".format(average_hr))
        hr_txt.write("Sign of tachycardia: " + str(tachy_present) + "\n")
        hr_txt.write("Sign of brachycardia: " + str(brachy_present) + "\n")
        hr_txt.write("Please note that values were extracted from a fixed sample of data.\n")
        hr_txt.write("Consult your physician for further information and clarification.\n")

        hr_txt.close()

        # read from the file to command line
        f = open(return_file)
        for line in iter(f):
            print(line)
        f.close()

def main(avg_time, filename='ecg_data.csv', tachy_limit=100,
    brachy_limit=60, return_file='HR_Specs.txt'):
    Patient.create_patient_file(self)

