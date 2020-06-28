# Ch1Ex024.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 24
# Title: Units of Time

def main():
	days = int(input("Days: "))
	hours = int(input("Hours: "))
	mins = int(input("Minutes: "))
	secs = int(input("Seconds: "))

	hours = hours + (days * 24)
	mins = mins + (hours * 60)
	secs = secs + (mins * 60)

	print("Total Seconds: %d" % secs)

if __name__ == "__main__": main()