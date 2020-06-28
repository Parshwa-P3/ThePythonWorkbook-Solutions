# Ch4Ex091.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 91
# Title: Operator Precedence

def precedence(s):
	if len(s) == 1:
		if s in ['+', '-']: return 1
		elif s in ['*', '/']: return 2
		elif s in ['^']: return 3
		else: return -1
	else:
		return -1

def main():
	s = input("String: ")
	r =  precedence(s)

	if r == -1: print("Invalid input")
	else: print("Precedence %d" % r)

if __name__ == "__main__": main()