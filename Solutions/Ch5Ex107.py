# Ch5Ex107.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 107
# Title: Avoiding Duplicates

def inputWordList():
	words = []
	print("Enter Words: [blank to stop]")
	ip = input()
	while ip != "":
		words.append(ip)
		ip = input()
	return words

def removeDuplicates():
	words = inputWordList()
	newWords = []
	for w in words:
		if w not in newWords:
			newWords.append(w)
	for w in newWords: print(w)

def main(): removeDuplicates()

if __name__ == "__main__": main()