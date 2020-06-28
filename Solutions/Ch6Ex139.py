# Ch6Ex139.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 139
# Title: Checking for a Winning Card

from Ch6Ex138 import createBingoCard, displayBingoCard

def isWinningCard(card):
	# Vertical
	for k in card.keys():
		if sum(card[k]) == 0: return True
	
	# Horizontal
	for i in range(5):
		if sum([col[i] for col in card.values()]) == 0:
			return True
	
	# Forward Diagonal
	tot = 0
	i = 0
	for col in card.values():
		for j in range(5):
			if i == j: tot += col[j]
		i += 1
	if tot == 0: return True
	
	# Backward Diagonal
	tot = 0
	i = 0
	for col in card.values():
		for j in range(5):
			if i + j == 4: tot += col[j]
		i += 1
	if tot == 0: return True

	return False

def main():
	print("\nVertical Winning:")
	card = createBingoCard()
	card['I'] = [0 for i in range(5)]
	displayBingoCard(card)
	print("Is winning card? ->", isWinningCard(card))

	print("\nHorizontal Winning:")
	card = createBingoCard()
	for k in card.keys(): card[k][2] = 0
	displayBingoCard(card)
	print("Is winning card? ->", isWinningCard(card))

	print("\nForward Diagonal Winning:")
	card = createBingoCard()
	i = 0
	for col in card.values():
		for j in range(5):
			if i == j: col[j] = 0
		i += 1
	displayBingoCard(card)
	print("Is winning card? ->", isWinningCard(card))

	print("\nBackward Diagonal Winning:")
	card = createBingoCard()
	i = 0
	for col in card.values():
		for j in range(5):
			if i + j == 4: col[j] = 0
		i += 1
	displayBingoCard(card)
	print("Is winning card? ->", isWinningCard(card))

if __name__ == "__main__": main()