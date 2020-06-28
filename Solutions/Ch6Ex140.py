# Ch6Ex140.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 140
# Title: Play Bingo

from Ch6Ex138 import createBingoCard, displayBingoCard
from Ch6Ex139 import isWinningCard
from random import shuffle

def calcAvg(nums):
	return float(sum(nums)) / len(nums)

def crossOut(card, num):
	for col in card.values():
		for i in range(len(col)):
			if col[i] == num: col[i] = 0

def playBingo(card):
	calls = [i for i in range(1, 76)]
	shuffle(calls)

	numCalls = 0
	while not isWinningCard(card):
		c = calls.pop()
		numCalls += 1
		crossOut(card, c)
	return numCalls

def simBingo(numSims):
	numCallsList = []
	for i in range(numSims):
		numCallsList.append(playBingo(createBingoCard()))
	print("Average calls: %.2f" % calcAvg(numCallsList))
	print("Maximum calls: %d" % max(numCallsList))

def main(): simBingo(int(input("Number of Simulations: ")))

if __name__ == "__main__": main()