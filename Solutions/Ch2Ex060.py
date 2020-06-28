# Ch2Ex060.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 60
# Title: Roulette Payouts

import random

def main():
	spaces = [0, '00', 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36, 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
	red = ( 2, 20)
	black = (20, 38)
	spin = random.choice(spaces)

	print("Spin resulted in %s..." % str(spin))
	print("Pay %s" % str(spin))

	if spin in spaces[red[0]: red[1]]:
		print("Pay Red")
	elif spin in spaces[black[0]: black[1]]:
		print("Pay Black")

	if spin not in [0, '00']:
		if spin % 2 == 0: print("Pay Even")
		else: print("Pay Odd")
		
		if spin <= 18: print("Pay 1 to 18")
		else: print("Pay 19 to 36")

if __name__ == "__main__": main()