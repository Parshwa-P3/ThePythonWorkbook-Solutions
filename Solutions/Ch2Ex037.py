# Ch2Ex037.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 37
# Title: Name that Shape

def main():
	numSides = int(input("Number of sides: "))

	if numSides == 3: print("Triangle")
	elif numSides == 4: print("Square")
	elif numSides == 5: print("Pentagon")
	elif numSides == 6: print("Hexagon")
	elif numSides == 7: print("Heptagon")
	elif numSides == 8: print("Octagon")
	elif numSides == 9: print("Nonagon")
	elif numSides == 10: print("Decagon")
	else: print("ERR!")

if __name__ == "__main__": main()