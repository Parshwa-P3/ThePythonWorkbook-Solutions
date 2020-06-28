# Ch6Ex134.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 134
# Title: Unique Characters

def uniqueCharacters(string):
	return len(set([c for c in string]))

def main():
	string = input("Enter a string:\n")
	print(uniqueCharacters(string))

if __name__ == "__main__": main()