# Ch4Ex082.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 82
# Title: Taxi Fare

def calcFare(dist):
	baseFare = 4.00
	addFare = 0.25
	addDist = 140
	totalFare = 0

	dist = dist * 1000	# km to m
	totalFare += baseFare

	while dist > addDist:
		totalFare += addFare
		dist -= addDist
	
	return totalFare

def main():
	dist = float(input("Distance (km): "))
	print("Fare: $% 6.2f" % calcFare(dist))

if __name__ == "__main__": main()