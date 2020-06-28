# Ch3Ex061.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 61
# Title: Average

def main():
	count = 0
	nums = []

	while True:
		ip = int(input("Enter Number: "))
		if ip == 0:
			break
		else:
			count += 1
			nums.append(ip)

	total = 0
	for i in range(count): total += nums[i]
	average = total / count

	print("Average: %.3f" % average)

if __name__ == "__main__": main()