# Ch6Ex129.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 129
# Title: Two Dice Simulation

from random import randint

def rollTwoDice():
	return randint(1, 6) + randint(1, 6)

def twoDiceSim(iters):
	counts = dict([(str(k), 0) for k in range(2, 13)])
	percents = {}
	for i in range(iters):
		roll = str(rollTwoDice())
		counts[roll] += 1
	
	for k in counts.keys():
		percents[k] = (counts[k] / iters) * 100

	expected = {'2': (1 / 0.36), '3': (2 / 0.36), '4': (3 / 0.36), '5': (4 / 0.36), '6': (5 / 0.36), '7': (6 / 0.36), '8': (5 / 0.36), '9': (4 / 0.36), '10': (3 / 0.36), '11': (2 / 0.36), '12': (1 / 0.36)}
	
	print("Total     Rolls   Sim. %   Exp. %")
	for k in counts.keys():
		print("% 5d  % 8d   % 6.2f   % 6.2f" % (int(k), counts[k], percents[k], expected[k]))

def main(): twoDiceSim(int(input("Iterations: ")))

if __name__ == "__main__": main()