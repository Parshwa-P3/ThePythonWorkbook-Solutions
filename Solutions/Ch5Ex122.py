# Ch5Ex122.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 122
# Title: Tokenizing a String

from re import match

def mathTokenizer(expr):
	expr = expr.replace(" ", '')
	tokenList = []
	token = ""
	tType = ''
	prev = ''
	
	for c in expr:
		if c in ['*', '/', '^', '(', ')']:
			if token != "":
				tokenList.append(token)
				token = ""
				tType = ''
			tokenList.append(c)
		elif c in ['+', '-']:
			if match(r'[0-9]', prev) or prev == ')':
				if token != "":
					tokenList.append(token)
					token = ""
					tType = ''
				tokenList.append(c)
			else:
				if token != "":
					tokenList.append(token)
					token = ""
					tType = ''
				token = c
				tType = 'N'
		elif match(r'[0-9]', c):
			if tType == 'N': token += c
			else: 
				token = c
				tType = 'N'
		prev = c
	if token != "": tokenList.append(token)
	
	return tokenList

def main():
	expr = input("Enter expression: ")
	print(mathTokenizer(expr))

if __name__ == "__main__": main()