# Ch4Ex085.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 85
# Title: Convert a Number to Ordinal form

def numToOrd(n):
	if n == 1: return 'first'
	elif n == 2: return 'second'
	elif n == 3: return 'third'
	elif n == 4: return 'fourth'
	elif n == 5: return 'fifth'
	elif n == 6: return 'sixth'
	elif n == 7: return 'seventh'
	elif n == 8: return 'eighth'
	elif n == 9: return 'ninth'
	elif n == 10: return 'tenth'
	elif n == 11: return 'eleventh'
	elif n == 12: return 'twelfth'
	else: return ''

def main():
	ST = 1
	EN = 12

	for i in range(ST, EN + 1):
		print("% 4d" % i, "% 12s" % numToOrd(i))

if __name__ == "__main__": main()