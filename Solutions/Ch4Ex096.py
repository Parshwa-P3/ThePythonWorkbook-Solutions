# Ch4Ex096.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 96
# Title: Check a Password

import re

def isGoodPassword(s):
	if len(s) >= 8 	and re.search(r'[A-Z]+', s) \
					and re.search(r'[a-z]+', s) \
				  	and re.search(r'[0-9]+', s):
		return True
	
	return False

def main():
	s = input("Enter Password: ")

	if isGoodPassword(s):
		print("%s is good password" % s)
	else:
		print("%s is not good password" % s)

if __name__ == "__main__": main()