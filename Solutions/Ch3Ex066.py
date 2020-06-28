# Ch3Ex066.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 66
# Title: Compute the Grade Point Average

def main():
	totalPoints = count = 0

	while True:
		grade = input("Grade: ")
		if grade == "": break

		if grade in ["A+", "A"]: points = 4.0
		elif grade == "A-": points = 3.7
		elif grade == "B+": points = 3.3
		elif grade == "B": points = 3.0
		elif grade == "B-": points = 2.7
		elif grade == "C+": points = 2.3
		elif grade == "C": points = 2.0
		elif grade == "C-": points = 1.7
		elif grade == "D+": points = 1.3
		elif grade == "D": points = 1.0
		elif grade == "F": points = 0
		else: continue
		
		totalPoints += points
		count += 1

	average = totalPoints / count if count > 0 else 0.0
	print("GPA: %.2f" % average)

if __name__ == "__main__": main()