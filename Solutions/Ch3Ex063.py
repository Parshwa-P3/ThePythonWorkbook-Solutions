# Ch3Ex063.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 63
# Title: Temperature Conversion Table

def main():
	print("   °C |   °F")
	for i in range(11):
		C = i * 10
		F = int((C * (9 / 5)) + 32)
		print("% 5d |% 5d" % (C, F))

if __name__ == "__main__": main()