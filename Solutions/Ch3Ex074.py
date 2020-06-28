# Ch3Ex074.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 74
# Title: Multiplication Table

MAX = 15

def main():
	c = ''

	for i in range(MAX + 1):
		for j in range(MAX + 1):
			if i == 0 and j == 0:
				c = " "
			else:
				if i == 0:
					i = 1
				elif j == 0:
					j = 1
				c = str(i * j)
			print("% 5s" % c, end="")
		print()

if __name__ == "__main__": main()