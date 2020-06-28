# Ch4Ex099.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 99
# Title: Arbitrary Base Conversions

from Ch4Ex098 import *

def decToN(num, n):
	res = ""
	q = num

	r = q % n
	res = decToHex(r) + res
	q = q // n

	while q > 0:
		r = q % n
		res = decToHex(r) + res
		q = q // n
	
	return res

def nToDec(num, n):
	dec = 0
	pwr = 0

	for i in range(len(num)):
		dec *= n
		dec += hexToDec(num[i])
	
	return dec

def mToN(m, num, n):
	dec = nToDec(num, m)
	new = decToN(dec, n)
	return new

def main():
	ogBase = int(input("Original Base: "))
	ogNum = input("Original Number: ")
	newBase = int(input("New Base: "))

	new = mToN(ogBase, ogNum, newBase)
	print("New Number: %s" % new)

if __name__ == "__main__": main()