# Ch4Ex102.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 102
# Title: Reduce Measures

def reduceMeasures(n, unit):
	tsp2Tbsp = 3		# 1 tbsp =  3 tsp
	tsp2Cup  = 3 * 16	# 1 cup  = 16 tbsp

	if unit == "tsp": tsp = n
	elif unit == "tbsp": tsp = n * tsp2Tbsp
	elif unit == "cup": tsp = n * tsp2Cup 

	cup = tsp // tsp2Cup
	tsp -= cup * tsp2Cup
	tbsp = tsp // tsp2Tbsp
	tsp -= tbsp * tsp2Tbsp

	res = ""

	if cup > 0:
		res += str(cup) + " cup"
		if cup > 1: res += "s"
	if tbsp > 0:
		if res != "": res += ", "
		res += str(tbsp) + " tbsp"
		if tbsp > 1: res += "s"
	if tsp > 0:
		if res != "": res += ", "
		res += str(tsp) + " tsp"
		if tsp > 1: res += "s"
	if res == "": res = "0 tsps"

	return res

def main():
	print("59 tsp  =>", reduceMeasures(59, "tsp"))
	print("59 tbsp =>", reduceMeasures(59, "tbsp"))
	print("1 tsp   =>", reduceMeasures(1, "tsp"))
	print("1 tbsp  =>", reduceMeasures(1, "tbsp"))
	print("1 cup   =>", reduceMeasures(1, "cup"))
	print("4 cup   =>", reduceMeasures(4, "cup"))
	print("3 tsp   =>", reduceMeasures(3, "tsp"))
	print("6 tsp   =>", reduceMeasures(6, "tsp"))
	print("95 tsp  =>", reduceMeasures(95, "tsp"))
	print("96 tsp  =>", reduceMeasures(96, "tsp"))
	print("97 tsp  =>", reduceMeasures(97, "tsp"))
	print("98 tsp  =>", reduceMeasures(98, "tsp"))
	print("99 tsp  =>", reduceMeasures(99, "tsp"))

if __name__ == "__main__": main()