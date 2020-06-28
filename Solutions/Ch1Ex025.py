# Ch1Ex025.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 25
# Title: Units of Time (Again)

def main():
	seconds = int(input("Total Seconds: "))

	minutes = seconds // 60
	seconds = seconds % 60

	hours = minutes // 60
	minutes = minutes % 60

	days = hours // 24
	hours = hours % 24

	print("Result: %d:%02d:%02d:%02d" % (days, hours, minutes, seconds))

if __name__ == "__main__": main()