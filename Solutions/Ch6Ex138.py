# Ch6Ex138.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 138
# Title: Create a Bingo Card

from random import randint

def displayBingoCard(card):
	print("  B   I   N   G   O")
	print("--------------------")
	for i in range(5):
		print("% 3d% 4d% 4d% 4d% 4d" % (card['B'][i], card['I'][i], card['N'][i], card['G'][i], card['O'][i]))

def createBingoCard():
	card = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
	keys = list(card.keys())
	for i in range(5):
		low = i * 15 + 1
		up = i * 15 + 15
		for j in range(5):
			n = randint(low, up)
			while n in card[keys[i]]: n = randint(low, up)
			card[keys[i]].append(n)
		card[keys[i]].sort()
	return card

def main(): displayBingoCard(createBingoCard())

if __name__ == "__main__": main()