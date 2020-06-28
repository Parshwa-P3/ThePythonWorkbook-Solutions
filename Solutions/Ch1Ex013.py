# Ch1Ex013.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 13
# Title: Making Change

def main():
	pen = nic = dim = qrt = loo = too = 0

	cents = int(input("Cents: "))

	if cents >= 200:
		too = cents // 200
		cents = cents % 200
	if cents >= 100:
		loo = cents // 100
		cents = cents % 100
	if cents >= 25:
		qrt = cents // 25
		cents = cents % 25
	if cents >= 10:
		dim = cents // 10
		cents = cents % 10
	if cents >= 5:
		nic = cents // 5
		cents = cents % 5
	if cents >= 1:
		pen = cents

	print()
	print("Pennies:  % 5d" % pen)
	print("Nickels:  % 5d" % nic)
	print("Dimes:    % 5d" % dim)
	print("Quarters: % 5d" % qrt)
	print("Loonies:  % 5d" % loo)
	print("Toonies:  % 5d" % too)

if __name__ == "__main__": main()