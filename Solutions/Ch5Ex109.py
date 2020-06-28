# Ch5Ex109.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 109
# Title: List of Proper Divisors

def properDivisors(n):
	divs = [1]
	maxD = n // 2
	d = 2
	while d < maxD:
		if n % d == 0: 
			divs.append(d)
			maxD = n // d
			divs.append(maxD)
		d += 1
	return sorted(divs)

def main():
	n = int(input("Enter the Number: "))
	divs = properDivisors(n)
	print("Proper divisors of %d:" % n)
	for n in divs: print(n, end=" ")

if __name__ == "__main__": main()