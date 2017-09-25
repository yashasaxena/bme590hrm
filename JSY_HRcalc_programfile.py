# where we import our combined function file
import HR_allfuncs as hr
import sys
filename = "ecg_data.csv"
def run_hr_func(averaging_time, tachy_limit = 100, brachy_limit=60):
    if(hr.columncheck(filename) == 1):
        pass
    if(hr.datatypecheck(filename) == 1):
        pass
    if(hr.datapracticality(filename)==1):
        pass
    hr_data = hr.dataextraction(filename)

    time_array = hr.HR_peakdetect(hr_data)

    inst_hrval = hr.instHR(time_array)

    average_hr_val = hr.hr_averaging(averaging_time)

    tachy_present = hr.tachy(average_hr_val, tachy_limit)
    brachy_present = hr.brachy(average_hr_val, brachy_limit)

    hr_txt = open("HR_Specs.txt", "w")
    hr_txt.write("Patient Name: Heart Patient Dude\n")
    hr_txt.write("Estimated instant heart rate: {:.3f}\n".format(inst_hrval))
    hr_txt.write("Estimated average heart rate: {:.3f}\n".format(average_hr_val))
    hr_txt.write("Sign of tachycardia: " + tachy_present + "\n")
    hr_txt.write("Sign of brachycardia: " + brachy_present + "\n")
    hr_txt.write("Please note that values were extracted from a fixed sample of data.\n")
    hr_txt.write("Consult your physician for further information and clarification.\n")

    hr_txt.close()

    # read from the file to command line
    f = open('HR_Specs.txt')
    for line in iter(f):
        print
    line
    f.close()

# use Sonali's functions to validate data before extraction
# use Sonali's function to extract data
# use peak detection function to collect peak times, store in a time array
# import time array into instant heart rate function, store in a float variable
# import time array into average heart rate function, store in a float variable
# import average heart rate value into tachy-,brachycardia function, store in a boolean variable

#basic syntax on opening, and writing to a file


def main(argv):
    if len(sys.argv) == 2:
        averaging_time = sys.argv[1]
        run_hr_func(averaging_time)
    if len(sys.argv) == 3:
        averaging_time = sys.argv[1]
        tachy_limit = sys.argv[2]
        run_hr_func(averaging_time,tachy_limit)
    if len(sys.argv) == 4:
        averaging_time = sys.argv[1]
        tachy_limit = sys.argv[2]
        brachy_limit = sys.argv[3]
        run_hr_func(averaging_time,tachy_limit,brachy_limit)


if __name__ == "__main__":
    main(argv)

