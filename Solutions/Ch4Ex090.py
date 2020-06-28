# Ch4Ex090.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 90
# Title: Does a String represent an integer

import re

def isInteger(s):
	s = s.strip()
	r = r'^[\+\-]?[0-9]+$'

	if len(s) >= 1:
		if re.match(r, s): return True
		else: return False
	else: return False

def main():
	s = input("String: ")
	if isInteger(s): print("%s is integer" % s)
	else: print("%s is not integer" % s)

if __name__ == "__main__": main()