# bme590hrm

## HW Assignment #2

Medical Software Design Evaluators: Palmeri, Kumar, Desai

Contributors: Hoballah, S. Shah, Saxena

Travis CI Build Status
---

![Travis Badge] (https://travis-ci.org/yashasaxena/bme590hrm.svg?branch=master)


License
---

MIT License Copyright (c) [2017] [J. Hoballah, Y. Saxena, S. Shah]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Running the Code:
---
Pull from master branch.
Set up Conda environment (bme590hrm).
To run file, python JSY_HRcalc_programfile.py XX YY ZZ(data file must be titled "ecg_data.csv").

Where XX is desired averaging time(m) (integers, decimals and fractions are acceptable), YY is tachycardia limit (bpm, integer or float acceptable), and ZZ is brachycardia limit (bpm, integer or float acceptable). XX parameter is required. YY and ZZ parameter are optional and default values are 100 and 60 respectively. If you wish to change the brachycardia_limit, you must input XX YY and ZZ. For changing the tachycardia_limit, you only need to input XX and YY.

3.a) This file should output all required information to the command line. Output will also be stored in a test file will named HR_Specs.txt and will be saved in the repository you are working in.

Note: There is a file ecg_data.csv in the master branch right now, please keep this in mind when running code.

Unit Test Files:

    test_import.py

    test_HR.py

    test_Vitals.py

    test_Diagnosis.py
