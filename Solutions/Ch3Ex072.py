# Ch3Ex072.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 72
# Title: Is the String a Palindrome?

def main():
	string = input("Enter String: ").lower()

	l = len(string)
	isPalindrome = True

	for i in range((l // 2)):
		if string[i] != string[-i - 1]:
			isPalindrome = False
			break

	print("String is ", end="")
	if not isPalindrome: print("not ", end="")
	print("a Palindrome")

if __name__ == "__main__": main()