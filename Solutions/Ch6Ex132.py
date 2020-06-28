# Ch6Ex132.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 132
# Title: Postal Codes

def postalCodeParser(code):
	charToProvince = {'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick', 'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec', 'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba', 'S': 'Saskatchwan', 'T': 'Alberta', 'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'}

	if code[0] in ['D', 'F', 'I', 'O', 'Q', 'U', 'W', 'Z']:
		print("Invalid Postal Code!")
		return
	
	prov = charToProvince[code[0]]
	addrType = 'a rural' if code[1] == '0' else 'an urban'

	print("%s is for %s address in %s" % (code, addrType, prov))
 
def main():
	code = input("Enter Postal Code: ").upper()
	postalCodeParser(code)
 
if __name__ == "__main__": main()