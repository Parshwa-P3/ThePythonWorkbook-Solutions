# Ch5Ex124.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 124
# Title: Evaluate Postfix

from Ch5Ex123 import infixToPostfix
from Ch5Ex122 import mathTokenizer
from Ch4Ex090 import isInteger

def applyOper(left, right, oper):
	if oper == "+": return left + right
	if oper == "-": return left - right
	if oper == "*": return left * right
	if oper == "/": return left / right
	if oper == "^": return left ** right

def evalPostfix(postfix):
	vals = []

	for token in postfix:
		if isInteger(token): vals.append(int(token))
		else:
			right = vals.pop()
			left = vals.pop()
			vals.append(applyOper(left, right, token))
	
	return vals[0]

def main():
	expr = input("Enter expresion: ")
	postfix = infixToPostfix(mathTokenizer(expr))
	val = evalPostfix(postfix)
	print(val)

if __name__ == "__main__": main()