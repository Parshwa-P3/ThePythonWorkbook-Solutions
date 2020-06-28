# Ch1Ex030.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 30
# Title: Units of Pressure

def main():
	kPa = float(input("In kPa: "))

	PPSI = kPa / 6.895
	mmhg = kPa * 7.501
	atm = kPa / 101

	print("%.4f kPa = %.4f PPSI = %.4f mmhg = %.4f atm" % (kPa, PPSI, mmhg, atm))

if __name__ == "__main__": main()