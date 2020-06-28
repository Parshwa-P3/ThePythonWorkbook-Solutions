# Ch5Ex115.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 115
# Title: Pig Latin

def pigLatin(word):
	word = word.lower()
	vowels = ['a', 'e', 'i', 'o', 'u']
	res = ""
	if word[0] in vowels:
		res = str(word) + "way"
	else:
		ct = 0
		c = word[ct]
		while c not in vowels and ct < len(word) - 1:
			ct += 1
			c = word[ct]
		res = str(word[ct:]) + str(word[:ct]) + "ay"

	return res

def main():
	string = input("Enter the String:\n")
	res = [pigLatin(w) for w in string.split()]
	print(" ".join(res))

if __name__ == "__main__": main()