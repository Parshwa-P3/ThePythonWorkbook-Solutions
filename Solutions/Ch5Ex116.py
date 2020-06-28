# Ch5Ex116.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 116
# Title: Pig Latin Improved

from Ch5Ex115 import pigLatin

def pigLatinImproved(string):
	puncs = [',', '.', '?', '-', '\'', '!', ':', ';']
	words = string.split()
	res = []
	for w in words:
		punc = ""
		r = ""
		upper = w[0].isupper()
		if w[-1] in puncs: 
			punc = w[-1]
			w = w[:-1]
		r += str(pigLatin(w.lower()))
		if upper: r = r.capitalize()
		if punc != "": r += punc
		res.append(r)
	
	return " ".join(res)

def main():
	string = input("Enter the String:\n")
	res = pigLatinImproved(string)
	print(res)

if __name__ == "__main__": main()