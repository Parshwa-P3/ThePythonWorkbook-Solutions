# Ch2Ex046.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 46
# Title: Season from Month and Day

def main():
	MM = input("Month: ")
	dd = int(input("Day: "))

	season = ""

	if MM[:3] in ["Jan", "Feb"]: season = "Winter"
	elif MM[:3] == "Mar":
		if dd < 20: season = "Winter"
		else: season = "Spring"
	elif MM[:3] in ["Apr", "May"]: season = "Spring"
	elif MM[:3] == "Jun":
		if dd < 21: season = "Spring"
		else: season = "Summer"
	elif MM[:3] in ["Jul", "Aug"]: season = "Summer"
	elif MM[:3] == "Sep":
		if dd < 22: season = "Summer"
		else: season = "Fall"
	elif MM[:3] in ["Oct", "Nov"]: season = "Fall"
	elif MM[:3] == "Dec":
		if dd < 21: season = "Fall"
		else: season = "Winter"

	print("Season: %s" % season)

if __name__ == "__main__": main()