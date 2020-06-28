# Ch3Ex065.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 65
# Title: Compute the Perimeter of a Polygon

import math as m

def main():
	peri = 0.0
	x = x1 = float(input("X Coord: "))
	y = y1 = float(input("Y Coord: "))

	while True:
		x2 = input("X Coord (blank -> Exit): ")
		if x2 == "": break
		else: x2 = float(x2)
		y2 = float(input("Y Coord: "))

		peri += m.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

		x1, y1 = x2, y2

	peri += m.sqrt(((x1 - x) ** 2) + ((y1 - y) ** 2))

	print("Peri = %.2f" % peri)

if __name__ == "__main__": main()