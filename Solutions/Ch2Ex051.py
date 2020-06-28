# Ch2Ex051.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 51
# Title: Letter Grade to Grade Points

def main():
	grade = input("Grade: ")

	print("Points: ", end="")

	if grade in ["A+", "A"]: print("4.0")
	elif grade == "A-": print("3.7")
	elif grade == "B+": print("3.3")
	elif grade == "B": print("3.0")
	elif grade == "B-": print("2.7")
	elif grade == "C+": print("2.3")
	elif grade == "C": print("2.0")
	elif grade == "C-": print("1.7")
	elif grade == "D+": print("1.3")
	elif grade == "D": print("1.0")
	elif grade == "F": print("0")
	else: print("ERR!")

if __name__ == "__main__": main()