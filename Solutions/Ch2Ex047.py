# Ch2Ex047.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 47
# Title: Birth date to Astrological Sign

def main():
	MM = input("Month: ")[:3]
	dd = int(input("Day: "))

	zodiacs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Saggitarius"]

	if MM == "Jan":
		if dd < 20: index = 0
		else: index = 1
	elif MM == "Feb":
		if dd < 19: index = 1
		else: index = 2
	elif MM == "Mar":
		if dd < 21: index = 2
		else: index = 3
	elif MM == "Apr":
		if dd < 20: index = 3
		else: index = 4
	elif MM == "May":
		if dd < 21: index = 4
		else: index = 5
	elif MM == "Jun":
		if dd < 21: index = 5
		else: index = 6
	elif MM == "Jul":
		if dd < 23: index = 6
		else: index = 7
	elif MM == "Aug":
		if dd < 23: index = 7
		else: index = 8
	elif MM == "Sep":
		if dd < 23: index = 8
		else: index = 9
	elif MM == "Oct":
		if dd < 23: index = 9
		else: index = 10
	elif MM == "Nov":
		if dd < 22: index = 10
		else: index = 11
	elif MM == "Dec":
		if dd < 22: index = 11
		else: index = 0

	print("Zodiac: %s" % zodiacs[index])

if __name__ == "__main__":
	main()