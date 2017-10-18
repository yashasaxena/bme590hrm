# import subclass files
import Data
import Processing
import Vitals
import Diagnosis


class Patient:
    def __init__(self, avg_time=.25, filename='ecg_data.csv', tachy_limit=100,
                 brachy_limit=60, return_file='HR_Specs.txt'):
        """
        Instantiates patient class

        :param avg_time:
        :param filename:
        :param tachy_limit:
        :param brachy_limit:
        :param return_file:

        """

        self.data = Data.Data(filename)
        self.data.extraction()
        self.pd_processing = Processing.Processing()  # self.data.HR_array
        self.pd_processing.ecg_peakdetect(self.data.hr_data)
        self.vitals = Vitals.Vitals(avg_time, self.pd_processing.t)
        self.diagnosis = Diagnosis.Diagnosis(self.vitals.avg_hr_val, tachy_limit, brachy_limit)
        self.f = filename
        self.r = return_file
        try:
            self.vitals = Vitals.Vitals(avg_time, self.pd_processing.t)
        except (ValueError, ZeroDivisionError):
            print("The program has encountered an error. Please view the error log in your console.")
        try:
            self.diagnosis = Diagnosis.Diagnosis(self.vitals.avg_hr_val, tachy_limit, brachy_limit)
        except ValueError:
            print("You inputted a brachycardia or tachycardia limit below zero. Are you sure you want to do that?")

    def create_patient_file(self):
        """Generates a text file with relevant heart patient information

        :rtype: text file
        """
        hr_txt = open(self.r, "w")
        hr_txt.write("Patient Name: Heart Patient Dude\n")
        hr_txt.write("Patient file: " + self.f + "\n")
        hr_txt.write("Estimated instant heart rate: {:.3f}\n".format(self.vitals.inst_hr_val))
        hr_txt.write("Estimated average heart rate: {:.3f}\n".format(self.vitals.avg_hr_val))
        hr_txt.write("Sign of tachycardia: " + str(self.diagnosis.tachy_result) + "\n")
        hr_txt.write("Sign of brachycardia: " + str(self.diagnosis.brachy_result) + "\n")
        hr_txt.write("Please note that values were extracted from a fixed sample of data.\n")
        hr_txt.write("Consult your physician for further information and clarification.\n")

        hr_txt.close()

        # read from the file to command line
        # f = open(self.r)
        # for line in iter(f):
        #     print(line)
        # f.close()


def main(avg_time=.25, filename='ecg_data.csv', tachy_limit=100, brachy_limit=60, return_file='HR_Specs.txt'):
    current_patient = Patient(avg_time, filename, tachy_limit, brachy_limit, return_file)
    current_patient.create_patient_file()


if __name__ == "__main__":
    main()
