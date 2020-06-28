# Ch6Ex135.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 135
# Title: Anagrams

def countLetters(word):
	letters = {}
	for c in word:
		if c in letters.keys(): letters[c] += 1
		else: letters[c] = 1
	return letters

def isAnagram(word1, word2):
	w1Letters = countLetters(word1)
	w2Letters = countLetters(word2)
	return w1Letters == w2Letters

def main():
	word1 = input("Enter first word: ")
	word2 = input("Enter second word: ")
	print(word1, '-', word2, '=>', isAnagram(word1, word2))

if __name__ == "__main__": main()