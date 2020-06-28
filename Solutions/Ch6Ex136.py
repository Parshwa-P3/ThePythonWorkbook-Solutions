# Ch6Ex136.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 136
# Title: Anagrams Again

from re import match

def countLettersExt(string):
	letters = {}
	for c in string.lower():
		if match(r'[a-z0-9]', c):
			if c in letters.keys(): letters[c] += 1
			else: letters[c] = 1
	return letters

def isAnagramExtended(string1, string2):
	s1Letters = countLettersExt(string1.replace(' ', ''))
	s2Letters = countLettersExt(string2.replace(' ', ''))
	return s1Letters == s2Letters

def main():
	string1 = input("Enter first string: ")
	string2 = input("Enter second string: ")
	print(string1, '-', string2, '=>', isAnagramExtended(string1, string2))

if __name__ == "__main__": main()