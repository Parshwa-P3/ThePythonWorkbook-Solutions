# Ch5Ex123.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 123
# Title: Infix to Postfix

from Ch5Ex122 import mathTokenizer
from Ch4Ex090 import isInteger
from Ch4Ex091 import precedence

def infixToPostfix(tokenList):
	ops = []
	postfix = []

	for token in tokenList:
		if isInteger(token): postfix.append(token)
		if token in ['+', '-', '*', '/', '^']:
			while len(ops) > 0 and ops[len(ops) - 1] != '(' \
				and precedence(token) < precedence(ops[len(ops) - 1]):
				postfix.append(ops.pop())
			ops.append(token)
		if token == '(': ops.append(token)
		if token == ')':
			while ops[len(ops) - 1] != '(': postfix.append(ops.pop())
			ops.pop()

	while len(ops) > 0: postfix.append(ops.pop())

	return postfix

def main():
	expr = input("Enter expression: ")
	tokenList = mathTokenizer(expr)
	print(infixToPostfix(tokenList))

if __name__ == "__main__": main()