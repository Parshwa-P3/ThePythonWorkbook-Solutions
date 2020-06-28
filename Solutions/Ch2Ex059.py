# Ch2Ex059.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 59
# Title: Is a License Plate Valid?

import re

licenseNum = input("License Plate No.: ")

valid = False
style = ""

if len(licenseNum) == 6 and re.fullmatch(r"^[A-Z]{3}[0-9]{3}$", licenseNum):
	valid = True
	style = "Old"
elif len(licenseNum) == 7 and re.fullmatch(r"^[0-9]{4}[A-Z]{3}$", licenseNum):
	valid = True
	style = "New"

print("This num is ", end="")

if valid: print("Valid in %s Style" % style)
else: print("Invalid")