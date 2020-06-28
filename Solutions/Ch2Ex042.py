# Ch2Ex042.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 42
# Title: Frequency to Note

def main():
	freq = float(input("Frequency: "))

	if freq > 261.63 - 1 and freq < 261.63 + 1:
		note = "C4"
	elif freq > 293.66 - 1 and freq < 293.66 + 1:
		note = "D4"
	elif freq > 329.63 - 1 and freq < 329.63 + 1:
		note = "E4"
	elif freq > 349.23 - 1 and freq < 349.23 + 1:
		note = "F4"
	elif freq > 392 - 1 and freq < 392 + 1:
		note = "G4"
	elif freq > 440 - 1 and freq < 440 + 1:
		note = "A4"
	elif freq > 493.88 - 1 and freq < 493.88 + 1:
		note = "B4"
	else:
		note = None

	if note: print("Note: " + note)
	else: print("ERR!")

if __name__ == "__main__": main()