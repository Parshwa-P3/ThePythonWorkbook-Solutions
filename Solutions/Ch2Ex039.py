# Ch2Ex039.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 39
# Title: Sound Levels

def main():
	db = int(input("Decibel Level: "))

	if db > 130:
		print("Louder than a Jackhammer")
	elif db == 130:
		print("As loud as a Jackhammer")
	elif db > 106:
		print("Louder than a Gas Lawnmower but Quieter than a Jackhammer")
	elif db == 106:
		print("As loud as a Gas Lawnmower")
	elif db > 70:
		print("Louder than an Alarm Clock but Quieter than a Gas Lawnmower")
	elif db == 70:
		print("As loud as an Alarm Clock")
	elif db > 40:
		print("Louder than a Quiet Room but Quieter than an Alarm Clock")
	elif db == 40:
		print("As quiet as a Quiet Room")
	else:
		print("Quieter than a Quiet Room")

if __name__ == "__main__": main()