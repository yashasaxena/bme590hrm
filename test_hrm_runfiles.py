import glob
import JSY_HR_programv2 as JSY_HR
import pytest

 file_counter = 0

def test_fileimport():
    """ Tests if all files are imported into directory
    """
    for x in glob.glob('/test_data/*.csv'):
        JSY_HR.main(x,10,80,100, 'Patient' + str(file_counter) + '_hrResults.txt')
        file_counter = file_counter + 1

    assert file_counter == 32



