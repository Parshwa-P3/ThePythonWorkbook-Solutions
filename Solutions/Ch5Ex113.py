# Ch5Ex113.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 113
# Title: Formatting a List

from Ch5Ex107 import inputWordList

def formatWordList(words):
	if len(words) == 1:
		return str(words[0])
	elif len(words) == 2:
		return str(words[0]) + " and " + str(words[1])
	elif len(words) >= 3:
		res = ""
		for w in words[:-2]:
			res += str(w) + ", "
		res += formatWordList(words[-2:])
		return res
	else:
		return ""

def main():
	words = inputWordList()
	res = formatWordList(words)
	print(res)

if __name__ == "__main__": main()