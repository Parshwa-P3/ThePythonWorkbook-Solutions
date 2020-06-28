# Ch2Ex043.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 43
# Title: Faces on Money

def main():
	den = int(input("Denomination: "))

	if den == 1: print("George Washington")
	elif den == 2: print("Thomas Gefferson")
	elif den == 5: print("Abraham Lincoln")
	elif den == 10: print("Alexander Hamilton")
	elif den == 20: print("Andrew Jackson")
	elif den == 50: print("Ulysses S. Grant")
	elif den == 100: print("Benjamin Franklin")
	else: print("ERR!")

if __name__ == "__main__": main()