# Ch1Ex028.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 28
# Title: Wind Chill

def main():
	Ta = float(input("Air Temp (∘C): "))
	V = float(input("Wind Speed (km/h): "))

	WCI = 13.12 + (0.6215 * Ta) - (11.37 * (V ** 0.16)) + (0.3965 * Ta * (V ** 0.16))

	print("WCI: %d" % WCI)

if __name__ == "__main__": main()