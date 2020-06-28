# Ch5Ex119.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 119
# Title: Dealing Hands of Cards

from Ch5Ex118 import shuffleDeck, createDeck

def dealCards(numHands, numCardsPerHand, deck):
	if numHands * numCardsPerHand > len(deck):
		print("Invalid no. of hands or cards!")
		return

	deal = [list() for i in range(numHands)]
	for c in range(numCardsPerHand):
		for h in range(numHands):
			deal[h].append(deck.pop(0))

	print("Cards Dealt:")
	for h in range(numHands):
		print("Hand %2d: " % (h + 1), end=" ")
		for c in range(numCardsPerHand):
			print("%s" % deal[h][c], end=" ")
		print()
	
	print("Remaining Deck:", end=" ")
	if len(deck) == 0: print("None")
	else:
		for d in deck: print("%s" % d, end=" ")

def main():
	h = int(input("Enter no. of hands: "))
	c = int(input("Enter no. of cards per hand: "))
	dealCards(h, c, shuffleDeck(createDeck()))

if __name__ == "__main__": main()