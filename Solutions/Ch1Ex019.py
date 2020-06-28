# Ch1Ex019.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 19
# Title: Free Fall

import math as m

def main():
	h = float(input("Height (m): "))
	vel = m.sqrt(2 * 9.8 * h)
	print("Velocity: %.2f m/s" % (vel))

if __name__ == "__main__": main()