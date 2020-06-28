# Ch2Ex050.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 50
# Title: Roots of a Quadratic Equation

def main():
	import math as m

	a = float(input("a = "))
	b = float(input("b = "))
	c = float(input("c = "))

	d = (b ** 2) - (4 * a * c)

	if a == 0 or d < 0: numRoots = 0
	elif d == 0: numRoots = 1
	elif d > 0: numRoots = 2

	if numRoots == 0:
		print("No Real Roots")
	elif numRoots == 1:
		root = (-1 * b) / (2 * a)
		print("1 Real Root\nRoot => %.3f" % root)
	elif numRoots == 2:
		root1 = ((-1 * b) + m.sqrt(d)) / (2 * a)
		root2 = ((-1 * b) - m.sqrt(d)) / (2 * a)
		print("2 Real Roots\nRoots => %.3f, %.3f" % (root1, root2))

if __name__ == "__main__": main()