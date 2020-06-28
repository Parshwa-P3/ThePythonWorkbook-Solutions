# Ch2Ex045.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 45
# Title: What color is that square

def main():
	pos = input("Position: ")

	col = pos[0]
	row = int(pos[1])
	clr = 1 # 1 -> White / -1 -> Black

	if col in ['a', 'c', 'e', 'g']: clr = -1
	elif col in ['b', 'd', 'f', 'h']: clr = 1

	if row % 2 == 0: clr *= -1

	print("Square %s is color " % pos, end="")

	if clr == 1: print("White")
	elif clr == -1: print("Black")

if __name__ == "__main__": main()