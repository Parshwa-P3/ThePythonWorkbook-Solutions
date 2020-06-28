# Ch2Ex049.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 49
# Title: Ritcher Scale

def main():
	mag = float(input("Magnitude: "))

	print("Descriptor: ", end="")

	if mag < 2.0: print("Micro")
	elif mag < 3.0: print("Very Minor")
	elif mag < 4.0: print("Minor")
	elif mag < 5.0: print("Light")
	elif mag < 6.0: print("Moderate")
	elif mag < 7.0: print("Strong")
	elif mag < 8.0: print("Major")
	elif mag < 10.0: print("Great")
	else: print("Meteoric")

if __name__ == "__main__": main()