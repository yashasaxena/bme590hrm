# bme590hrm

## HW Assignment #2

Medical Software Design Evaluators: Palmeri, Kumar, Desai

Contributors: Hoballah, S. Shah, Saxena

Travis CI Build Status
---

[![Build Status](https://travis-ci.org/yashasaxena/bme590hrm.svg?branch=master)](https://travis-ci.org/yashasaxena/bme590hrm)
License
---

MIT License Copyright (c) [2017] [J. Hoballah, Y. Saxena, S. Shah]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Running the Code:
---
Pull from ClassComposition branch.
Set up Conda environment (bme590hrm).

To run our program: In your Python script, import ECG_Patient as ecp_p (or however you wish to define it).

Instantiate an object of the Patient class.

For example:

    import ECG_Patient as ecg_p

    John_Smith = ecg_p.Patient(5/60, 'test_data5.csv', tachy_limit=110, brachy_limit=75, return_file='John_Smith.txt')

    John_Smith.create_patient_file()

This will create a file named John_Smith.txt in your current directory with the results of our HR monitor.