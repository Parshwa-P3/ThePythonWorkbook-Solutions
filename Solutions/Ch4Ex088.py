# Ch4Ex088.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 88
# Title: Is it a Valid Triangle

def isValidTri(s1, s2, s3):
	return not (s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2)

def main():
	print(isValidTri(1, 2, 3))
	print(isValidTri(3, 3, 5))

if __name__ == "__main__": main()