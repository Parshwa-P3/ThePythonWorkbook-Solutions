# Ch2Ex038.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 38
# Title: Month name to Number of days

def main():
	MM = input("Enter name of month: ")

	if MM in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
		print("31 days")
	elif MM in ['April', 'June', 'September', 'November']:
		print("30 Days")
	elif MM is "February":
		print("28 or 29 Days")
	else:
		print("ERR!")

if __name__ == "__main__": main()