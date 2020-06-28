# Ch3Ex064.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 64
# Title: No more Pennies

def main():
	ips = []
	while True:
		ip = input("Input: ")
		if ip == "": break
		else: ips.append(float(ip))

	tot = sum(ips, 0)
	rem = (tot * 100) % 5
	if rem < 2.5: cTot = tot - (rem / 100)
	else: cTot = tot + ((5 - rem) / 100)

	print()
	print("Actual Total: %.2f" % tot)
	print("Cash Payable: %.2f" % cTot)

if __name__ == "__main__": main()