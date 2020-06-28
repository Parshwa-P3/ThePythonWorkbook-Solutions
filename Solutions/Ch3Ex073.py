# Ch3Ex073.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 73
# Title: Multiple word Palindromes

def main():
	string = input("Enter String: ").replace(" ", '').lower()

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