# Ch5Ex118.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 118
# Title: Shuffling a Deck of Cards

from random import randrange

def createDeck():
	suits = ['s', 'h', 'd', 'c']
	cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	deck = []
	
	for s in suits:
		for c in cards:
			deck.append(str(c + s))
	
	return deck

def shuffleDeck(deck):
	for i in range(len(deck) - 1):
		n = randrange(i + 1, len(deck))
		temp = deck[i]
		deck[i] = deck[n]
		deck[n] = temp
	
	return deck

def main():
	deck = createDeck()
	deck = shuffleDeck(deck)
	print("Deck After Shuffling:")
	print(deck)

if __name__ == "__main__": main()