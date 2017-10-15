import glob
import JSY_HR_programv2 as JSY_HR

 file_counter = 1

 for x in glob.glob('*.csv'):
     JSY_HR.main(x,10,80,100, 'Patient' + str(file_counter) + '_hrResults.txt')
     file_counter = file_counter + 1


