# Ch4Ex089.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 89
# Title: Capitalize it

import re

def capitalize(s):
	s = s.replace(' i ', ' I ')
	s = s[0].upper() + s[1:]

	p = 0
	while p < len(s):
		if s[p] in ['.', '!', '?']:
			p += 1
			while p < len(s) and s[p] == ' ':
				p += 1
			if p < len(s):
				s = s[0:p] + s[p].upper() + s[p+1:len(s)]		
		p += 1
	return s

def main():
	s = input("Enter a string: ")
	print(capitalize(s))

if __name__ == "__main__": main()