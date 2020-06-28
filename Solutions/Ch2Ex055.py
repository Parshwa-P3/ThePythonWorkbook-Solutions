# Ch2Ex055.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 55
# Title: Frequency to Name

def main():
	freq = float(input("Frequency: "))

	print("Category: ", end="")

	if freq < 3e9: print("Radio Waves")
	elif freq < 3e12: print("Microwaves")
	elif freq < 4.3e14: print("Infrared Light")
	elif freq < 7.5e14: print("Visible Light")
	elif freq < 3e17: print("Ultraviolet")
	elif freq < 3e19: print("X-Rays")
	else: print("Gamma Rays")

if __name__ == "__main__": main()