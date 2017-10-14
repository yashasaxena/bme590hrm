# where we import our combined function file
import HR_classfile as hr


def main(filename = 'ecg_data.csv', avg_time = 10, tachy_limit= 100, brachy_limit= 60, return_file ='HR_Specs.txt'):
    p_data = hr.Data(filename)

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

    vital_results = hr.Vitals(avg_time,time_array)
    instant_hr = vital_results.inst_hr_val

    average_hr = vital_results.avg_hr_val

    diag_results = hr.Diagnosis()
    diag_results..tachy(average_hr,tachy_limit)
    diag_results.brachy(average_hr,brachy_limit)
    tachy_present = diag_results.tachy_result
    brachy_present = diag_results.brachy_result

    hr_txt = open(return_file, "w")
    hr_txt.write("Patient Name: Heart Patient Dude\n")
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

