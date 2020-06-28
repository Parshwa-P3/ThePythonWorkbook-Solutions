# Ch1Ex033.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 33
# Title: Day old bread

def main():
	cost = 3.49
	discRate = 60

	numBread = int(input("No. of old bread: "))
	regularPrice = cost * numBread
	discount = (regularPrice * discRate) / 100
	totalPrice = regularPrice - discount

	print("Regular:  $% 8.2f" % regularPrice)
	print("Discount: $% 8.2f" % discount)
	print("- - - - - - - - - - -")
	print("Total:    $% 8.2f" % totalPrice)

if __name__ == "__main__": main()