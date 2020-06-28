# Ch1Ex017.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 17
# Title: Heat Capacity

def main():
	m = float(input("Mass: "))
	delT = float(input("Delta Temp: "))
	q = m * delT * 4.186
	cost = (q / (3.6e6)) * (8.9 / 100)

	print("Energy Reqd: %.3f J" % q)
	print("Total Cost:  $%.2f" % (cost))

if __name__ == "__main__": main()