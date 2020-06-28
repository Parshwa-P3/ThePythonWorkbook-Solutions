# Ch1Ex006.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 6
# Title: Tax and Tip

def main():
	cost = float(input("Cost of Meal: "))
	tax = 0.18 * cost
	tip = 0.18 * cost
	total = round(cost + tax + tip, 2)

	print()
	print("Cost:  $% 7.2f" % cost)
	print("Tax:   $% 7.2f" % tax)
	print("Tip:   $% 7.2f" % tip)
	print("-------------------")
	print("TOTAL: $% 7.2f" % total)

if __name__ == "__main__": main()