# Ch3Ex069.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 69
# Title: Approximate Pi

def main():
	limit = 10
	pi = 3
	sign = 1

	for i in range(1, limit):
		print("%.16f" % pi)
		i *= 2
		pi += sign * (4 / (i * (i + 1) * (i + 2)))
		sign *= -1

if __name__ == "__main__": main()