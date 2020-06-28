# Ch2Ex052.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 52
# Title: Grade Points to Letter Grade

def main():
	points = float(input("Grade Points: "))

	print("Grade: ", end="")

	if points >= 4.0: print("A+")
	elif points > 3.85: print("A")
	elif points > 3.5: print("A-")
	elif points > 3.15: print("B+")
	elif points > 2.85: print("B")
	elif points > 2.5: print("B-")
	elif points > 2.15: print("C+")
	elif points > 1.85: print("C")
	elif points > 1.5: print("C-")
	elif points > 1.15: print("D+")
	elif points > 0.85: print("D")
	else: print("F")

if __name__ == "__main__": main()