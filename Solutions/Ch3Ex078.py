# Ch3Ex078.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 78
# Title: Decimal to Binary

def main():
	decNum = int(input("Decimal Number: "))
	binNum = []

	while decNum > 0:
		binNum.append(str(decNum % 2))
		decNum = decNum // 2

	binNum = "".join(binNum[::-1])

	print("Binary Number: %s" % binNum)

if __name__ == "__main__": main()