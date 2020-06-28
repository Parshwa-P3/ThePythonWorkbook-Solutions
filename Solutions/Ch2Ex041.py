# Ch2Ex041.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 41
# Title: Note to Frequency

def main():
	frqs = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88]

	name = input("Name of Note: ")
	note = name[0]
	octv = int(name[1])

	print("Frequency: ", end="")

	if note == 'C': fr = frqs[0]
	elif note == 'D': fr = frqs[1]
	elif note == 'E': fr = frqs[2]
	elif note == 'F': fr = frqs[3]
	elif note == 'G': fr = frqs[4]
	elif note == 'A': fr = frqs[5]
	elif note == 'B': fr = frqs[6]
	else: fr = 0

	fr = fr / (2 ** (4 - octv))

	print(fr)

if __name__ == "__main__": main()