# Ch2Ex048.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 48
# Title: Chinese Zodiac

def main():
	year = int(input("Year: "))

	anims = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']

	print("Animal: %s" % anims[year % 12])

if __name__ == "__main__": main()