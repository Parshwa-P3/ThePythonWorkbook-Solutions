# Ch4Ex087.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 87
# Title: Center a String in the Terminal

def centerString(s, w, c=" "):
	if w < len(s): return s
	sp = (w - len(s)) // 2
	return c * sp + s + c * (w - sp - len(s))

def main():
	W = 100
	string1 = input("Enter String1: ")
	string2 = input("Enter String2: ")
	string3 = input("Enter String3: ")
	print(centerString(string1, W))
	print(centerString(string2, W))
	print(centerString(string3, W))

if __name__ == "__main__": main()