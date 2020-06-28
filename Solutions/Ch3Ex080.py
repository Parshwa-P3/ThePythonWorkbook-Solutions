# Ch3Ex080.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 80
# Title: Coin Flip Simulation

from random import choice

NUM_FLIPS = 10
NUM_CONSEC = 3

def coinFlipSim(numConsec):
	outcomes = ["H", "T"]
	flipCount = 1
	consecCount = 1
	prevFlip = choice(outcomes)
	print(prevFlip, end=" ")

	while True:
		result = choice(outcomes)
		print(result, end=" ")

		flipCount += 1
		if result == prevFlip:
			consecCount += 1
		else:
			consecCount = 1
		
		prevFlip = result

		if consecCount == numConsec:
			break
	
	print("(%d flips)" % flipCount)
	return flipCount

def main():
	totalFlips = 0
	maxFlips = NUM_CONSEC

	for i in range(NUM_FLIPS):
		result = coinFlipSim(NUM_CONSEC)
		totalFlips += result
		if result > maxFlips: maxFlips = result

	average = totalFlips / NUM_FLIPS

	print("Average %.1f flips" % average)
	print("Maximum %d flips" % maxFlips)

if __name__ == "__main__": main()