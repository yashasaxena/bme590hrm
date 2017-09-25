# where we import our combined function file
import HR_allfuncs as HR
filename = "ecg_data.csv"
def run_hr_func(averaging_time, tachy_limit = 100, brachy_limit=60):
    if(HR.columncheck(filename) == 1):
        pass
    if(HR.datatypecheck(filename) == 1):
        pass
    if(HR.datapracticality(filename)==1):
        pass
    HR_data = HR.dataextraction(filename)

    time_array = HR.HR_peakdetect(HR_data)

    inst_hrval = HR.instHR(time_array)

    average_hr_val = HR.hr_averaging(averaging_time)

    tachy_present = HR.tachy(average_hr_val, tachy_limit)
    brachy_present = HR.brachy(average_hr_val, brachy_limit)








# use Sonali's functions to validate data before extraction
# use Sonali's function to extract data
# use peak detection function to collect peak times, store in a time array
# import time array into instant heart rate function, store in a float variable
# import time array into average heart rate function, store in a float variable
# import average heart rate value into tachy-,brachycardia function, store in a boolean variable

#basic syntax on opening, and writing to a file

def main():
    hr_txt = open("HR_Specs.txt","w")
    hr_txt.write("Patient Name: Heart Patient Dude")
    hr_txt.write("Estimated instant heart rate: {}" + "{:.3f}".format(#inst hr variable))
    hr_txt.write("Estimated average heart rate: {}" + "{:.3f}".format(#avg hr variable))
    hr_txt.write("Sign of tachycardia: {}" + #tachycardia variable)
    hr_txt.write("Sign of brachycardia: {}" + #brachycardia variable)
    hr_txt.write("Please note that values were extracted from a fixed sample of data.")
    hr_txt.write("Consult your physician for further information and clarification.")

    hr_txt.close()

    #read from the file to command line
    f = open('HR_Spects.txt')
    for line in iter(f):
        print line
    f.close()


if __name__ == "__main__":
    main()

