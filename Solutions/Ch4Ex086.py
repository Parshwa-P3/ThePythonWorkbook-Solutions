# Ch4Ex086.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 86
# Title: The Twelve Days of Christmas

from Ch4Ex085 import numToOrd

def genVerse(n):
	print("On the", numToOrd(n), "day of Christmas")
	print("my true love sent to me:")

	if n >= 12: print("Twelve drummers drumming,")
	if n >= 11: print("Eleven pipers piping,")
	if n >= 10: print("Ten lords a leaping,")
	if n >= 9: print("Nine ladies dancing,")
	if n >= 8: print("Eight maids a milking,")
	if n >= 7: print("Seven swans a swimming,")
	if n >= 6: print("Six geese a laying,")
	if n >= 5: print("Five golden rings,")
	if n >= 4: print("Four calling birds,")
	if n >= 3: print("Three French hens,")
	if n >= 2: print("Two turtle doves,")
	if n == 1: print("A", end=" ")
	else: print("And A", end=" ")
	print("partridge in a pear tree.")
	print()

def main():
	for v in range(1, 13): genVerse(v)
	
if __name__ == "__main__": main()