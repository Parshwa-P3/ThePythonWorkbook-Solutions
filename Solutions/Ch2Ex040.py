# Ch2Ex040.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 40
# Title: Name that Triangle

def main():
	sides = list(map(int, input("Enter sides: ").strip().split()))

	if sides[0] == sides[1] == sides[2]:
		print("Equilateral Triangle")
	elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
		print("Isosceles Triangle")
	else:
		print("Scalene Triangle")

if __name__ == "__main__": main()