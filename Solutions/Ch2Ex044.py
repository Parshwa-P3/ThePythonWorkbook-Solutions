# Ch2Ex044.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 44
# Title: Date to Holiday Name

def main():
	date = input("Enter Date: ")

	if date == "January 1":
		print("New Year's Day")
	elif date == "July 1":
		print("Canada Day")
	elif date == "December 25":
		print("Christmas Day")
	else:
		print("ERR!")

if __name__ == "__main__": main()