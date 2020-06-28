# Ch1Ex012.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 12
# Title: Distance between two points on Earth

import math as M

def main():
	t1 = M.radians(float(input("t1: ")))
	g1 = M.radians(float(input("g1: ")))
	t2 = M.radians(float(input("t2: ")))
	g2 = M.radians(float(input("g2: ")))

	d = 6371.01 * M.acos((M.sin(t1) * M.sin(t2)) + (M.cos(t1) * M.cos(t2) * M.cos(g1 - g2)))

	print("Distance: %.3f km" % d)

if __name__ == "__main__": main()