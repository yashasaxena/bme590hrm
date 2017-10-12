# where we import our combined function file
import HRimport as hr


def main(filename = 'ecg_data.csv', averaging_time = 10, tachy_limit= 100, brachy_limit= 60, retu):
    p_data = Data(filename)

    if p_data.columncheck(filename) == 1:
        pass
    if p_data.typecheck(filename) == 1:
        pass
    if p_data.practicality(filename) == 1:
        pass
    #hr_data = hr.dataextraction(filename)
    p_data.extraction(filename)

    hr_data = p_data.HR_data
    time_array = Processing(hr_data).t


    #inst_hrval = hr.instHR(time_array)

    #average_hr_val = hr.hr_averaging(averaging_time, time_array)

    #tachy_present = hr.tachy(average_hr_val, tachy_limit)
    #brachy_present = hr.brachy(average_hr_val, brachy_limit)

    hr_txt = open("HR_Specs.txt", "w")
    hr_txt.write("Patient Name: Heart Patient Dude\n")
    hr_txt.write("Estimated instant heart rate: {:.3f}\n".format(inst_hrval))
    hr_txt.write("Estimated average heart rate: {:.3f}\n".format(average_hr_val))
    hr_txt.write("Sign of tachycardia: " + str(tachy_present) + "\n")
    hr_txt.write("Sign of brachycardia: " + str(brachy_present) + "\n")
    hr_txt.write("Please note that values were extracted from a fixed sample of data.\n")
    hr_txt.write("Consult your physician for further information and clarification.\n")

    hr_txt.close()

    # read from the file to command line
    f = open('HR_Specs.txt')
    for line in iter(f):
        print(line)
    f.close()


    # if len(sys.argv) < 2:
    #     print("Please input an averaging time.")
    # if len(sys.argv) == 2:
    #     averaging_time = sys.argv[1]
    #     run_hr_func(averaging_time)
    # if len(sys.argv) == 3:
    #     averaging_time = sys.argv[1]
    #     tachy_limit = sys.argv[2]
    #     tachy_limit = complex(tachy_limit)
    #     tachy_limit = tachy_limit.real
    #     run_hr_func(averaging_time, tachy_limit)
    # if len(sys.argv) == 4:
    #     averaging_time = sys.argv[1]
    #     tachy_limit = sys.argv[2]
    #     tachy_limit = complex(tachy_limit)
    #     tachy_limit = tachy_limit.real
    #     brachy_limit = sys.argv[3]
    #     brachy_limit = complex(brachy_limit)
    #     brachy_limit = brachy_limit.real
    #     run_hr_func(averaging_time, tachy_limit, brachy_limit)
    # if len(sys.argv) > 4:
    #     print("Please view the README.md file for proper usage, you have too many arguments.")



if __name__ == "__main__":
    main()

