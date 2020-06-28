# Ch5Ex117.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 117
# Title: Line of Best Fit

from Ch5Ex112 import calcAvg

def inputCoordsList():
	coords = []
	c = []
	print("Enter x and y coords: [blank to stop]")
	x = input()
	while x != "":
		c.append(float(x))
		y = input()
		while y == "":
			print("y can't be blank. Enter y again")
			y = input()
		c.append(float(y))
		coords.append(c)
		c = []
		x = input()
	return coords

def lineOfBestFit(coords):
	n = len(coords)
	avg = [
		calcAvg([c[0] for c in coords]),
		calcAvg([c[1] for c in coords])
	]
	sumxy = sum([(c[0] * c[1]) for c in coords])
	sumx  = sum([c[0] for c in coords])
	sumy  = sum([c[1] for c in coords])
	sumx2 = sum([(c[0] ** 2) for c in coords])
	m = (sumxy - ((sumx * sumy) / n)) / (sumx2 - ((sumx ** 2) / n))
	b = avg[1] - (m * avg[0])
	res = ("y = %.2fx " % m)
	res += "- " if b < 0 else "+ "
	res += ("%.2f" % abs(b))
	print(res)

def main():
	coords = inputCoordsList()
	lineOfBestFit(coords)

if __name__ == "__main__": main()