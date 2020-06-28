# Ch6Ex128.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 128
# Title: Reverse Lookup

def reverseLookup(dic, val):
	keys = []
	for k, v in dic.items():
		if v == val: keys.append(k)
	return keys

def main():
	dic1 = {'a': 'apple', 'b': 'ball'}
	dic2 = {'a': 'small', 'b': 'small', 'A': 'big', 'B': 'big', '1': 'digit', '2': 'digit'}
	print(dic1, '\ncat =>', reverseLookup(dic1, 'cat'))
	print(dic1, '\nball =>', reverseLookup(dic1, 'ball'))
	print(dic2, '\nsmall =>', reverseLookup(dic2, 'small'))

if __name__ == "__main__": main()