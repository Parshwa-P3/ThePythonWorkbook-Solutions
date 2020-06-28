# Ch5Ex111.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 111
# Title: Only the Words

def getWords(string):
	symbols = [',', '.', '?', '-', '\'', '!', ':', ';']
	words = string.split()
	for i in range(len(words)):
		if words[i][0] in symbols:
			words[i] = words[i][1:]
		if words[i][-1] in symbols:
			words[i] = words[i][:-1]
	return words

def main():
	string = input("Enter the String:\n")
	words = getWords(string)
	for w in words: print(w)

if __name__ == "__main__": main()