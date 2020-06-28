# Ch6Ex133.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 133
# Title: Write out Numbers in English

def numberToEnglish(num):
	if num == 0:
		print("%d => zero" % num)
		return

	ones = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}

	tens = {'0': '', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

	numHunds = num // 100
	numTens = (num % 100) // 10
	numOnes = (num % 10) if numTens >= 2 else (num % 20)

	print("%d => " % (num), end="")
	if numHunds > 0: print("%s hundred and " % (ones[str(numHunds)]), end="")
	if numTens >= 2: print("%s " % (tens[str(numTens)]), end="")
	print("%s" % (ones[str(numOnes)]))

def main():
	num = int(input("Enter a Number [upto 999]: "))
	numberToEnglish(num)

if __name__ == "__main__": main()