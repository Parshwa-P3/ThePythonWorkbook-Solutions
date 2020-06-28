# Ch2Ex053.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 53
# Title: Assessing Employees

def main():
	rating = float(input("Rating: "))

	if rating == 0.0:
		print("Unacceptable Performance")
		print("Raise = $%d" % (rating * 2400))
	elif rating == 0.4:
		print("Acceptable Performance")
		print("Raise = $%d" % (rating * 2400))
	elif rating == 0.6:
		print("Meritorious Performance")
		print("Raise = $%d" % (rating * 2400))
	else:
		print("ERR!")

if __name__ == "__main__":
	main()