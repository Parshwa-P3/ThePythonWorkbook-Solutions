# Ch1Ex011.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 11
# Title: Fuel Efficiency

def main():
	mpg = float(input("MPG: "))
	lpk = 235.214583 / mpg
	print("LPK = %.3f L/100km" % (lpk))

if __name__ == "__main__": main()