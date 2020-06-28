# Ch2Ex058.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 58
# Title: Next Day

def main():
	YY, mm, dd = [int(i) for i in input("Current Date (YYYY-mm-dd): ").split('-')]

	nd = nm = nY = 0

	leap = True
	if YY % 400 == 0: leap = True
	elif YY % 100 == 0: leap = False
	elif YY % 4 == 0: leap = True
	else: leap = False

	nd, nm, nY = dd, mm, YY

	if dd == 31:
		nd = 1
		if mm in [1, 3, 5, 7, 8, 10]:
			nm = mm + 1
		elif mm == 12:
			nm = 1
			nY = YY + 1
	elif dd == 30:
		if mm in [4, 6, 9, 11]:
			nd = 1
			nm = mm + 1
		else:
			nd = dd + 1
	elif dd == 29:
		if leap and mm == 2:
			nd = 1
			nm = 3
		else:
			nd = dd + 1
	elif dd == 28:
		if not leap and mm == 2:
			nd = 1
			nm = 3
		else:
			nd = dd + 1
	else:
		nd = dd + 1


	print("Next Date: %d-%02d-%02d" % (nY, nm, nd))

if __name__ == "__main__": main()