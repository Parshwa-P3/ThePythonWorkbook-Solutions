# Ch5Ex127.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 127
# Title: The Sieve of Eratosthenes

def sieveOfErato(limit):
	nums = list(range(limit + 1))
	nums[1] = 0
	p = nums[2]
	while p < limit:
		for i in range(2 * p, limit + 1, p): nums[i] = 0
		p = p + 1
		while p < limit and nums[p] == 0: p += 1

	primes = []
	for n in nums:
		if n != 0: primes.append(n)

	print("Primes between 2 and %d:" % limit)
	for p in primes: print(p, end=", ")

def main():
	limit = int(input("Enter the limit: "))
	sieveOfErato(limit)

if __name__ == "__main__": main()