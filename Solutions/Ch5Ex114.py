# Ch5Ex114.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 114
# Title: Random Lottery Numbers

from random import randint

def randomLottery():
	rands = []
	while len(rands) < 6:
		num = randint(1, 49)
		if num not in rands: rands.append(num)
	return sorted(rands)

def main():
	rands = randomLottery()
	print("Lottery Numbers:")
	for n in rands: print(n, end=" ")

if __name__ == "__main__": main()