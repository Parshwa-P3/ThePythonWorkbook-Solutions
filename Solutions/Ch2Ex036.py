# Ch2Ex036.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 36
# Title: Vowel or Consonant

def main():
	letter = input("Enter a Letter: ")

	if letter in ['a', 'e', 'i', 'o', 'u']:
		print("%c is a vowel" % letter)
	elif letter == 'y':
		print("Sometimes y is Vowel & sometimes consonant")
	elif letter in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']:
		print("%c is a consonant" % letter)
	else:
		print("%c is not a letter" % letter)

if __name__ == "__main__": main()