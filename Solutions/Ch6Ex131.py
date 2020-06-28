# Ch6Ex131.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 131
# Title: Morse Code

def textToMorseCode(text):
	morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

	code = []
	for c in text.upper():
		if c in morseCode.keys(): code.append(morseCode[c])
	
	return " ".join(code)

def main():
	text = input("Enter the text:\n")
	print(textToMorseCode(text))

if __name__ == "__main__": main()