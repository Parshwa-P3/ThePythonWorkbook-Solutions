# Ch3Ex062.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 62
# Title: Discount Table

def main():
	originalPrices = [4.95, 9.95, 14.95, 24.95]
	newPrices = []

	print("Old Price - Discount  - New Price")
	for price in originalPrices:
		discount = 0.6 * price
		newPrices = price - discount
		print(" $% 7.2f   $% 7.2f     $% 7.2f" % (price, discount, newPrices))

if __name__ == "__main__": main()