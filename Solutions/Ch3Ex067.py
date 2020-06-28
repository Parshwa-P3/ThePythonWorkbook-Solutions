# Ch3Ex067.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 67
# Title: Admission Price

def main():
	groups = ["< 2", "3 to 12", "13 to 64", "> 65"]
	prices = [0, 14, 23, 18]
	counts = [0, 0, 0, 0]

	while True:
		age = input("Age: ")
		if age == "": break
		else: age = int(age)

		if age <= 2:
			counts[0] += 1
			continue
		elif age <= 12:
			counts[1] += 1
		elif age >= 65:
			counts[3] += 1
		else:
			counts[2] += 1

	totalCount = totalPrice = 0

	print("Age Group - Count - Adm. Price")
	for i in range(4):
		print("% 9s - % 4d  - $% 8.2f" % (groups[i], counts[i], counts[i] * prices[i]))
		totalCount += counts[i]
		totalPrice += counts[i] * prices[i]

	print("------------------------------")
	print("    TOTAL - % 4d  - $% 8.2f" % (totalCount, totalPrice))

if __name__ == "__main__": main()