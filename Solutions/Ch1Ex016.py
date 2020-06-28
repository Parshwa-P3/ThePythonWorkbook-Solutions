# Ch1Ex016.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 16
# Title: Area and Volume

import math as m

def main():
	r = float(input("Radius (cm): "))
	area = m.pi * r * r
	vol = (m.pi * 4 / 3) * r * r * r

	print("Area:   %.3f cm²" % area)
	print("Volume: %.3f cm³" % vol)
	

if __name__ == "__main__": main()