# Ch2Ex056.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 56
# Title: Cell Phone Bill

def main():
	mins = int(input("Call Minutes: "))
	msgs = int(input("Messages: "))

	baseChrg = 15
	callCentreChrg = 0.44

	extraMins = extraMinChrg = extraMsgs = extraMsgChrg = 0

	if mins > 50:
		extraMins = mins - 50
		extraMinChrg = extraMins * 0.25

	if msgs > 50:
		extraMsgs = msgs - 50
		extraMsgChrg = extraMsgs * 0.15

	totalChrg = baseChrg + callCentreChrg + extraMinChrg + extraMsgChrg
	tax = (5 * totalChrg) / 100

	grandTotal = totalChrg + tax

	print("Base Charge:             $% 8.2f" % baseChrg)
	if mins > 50:
		print("Extra Minutes Charge:    $% 8.2f" % extraMinChrg)
	if msgs > 50:
		print("Extra Messages Charge:   $% 8.2f" % extraMsgChrg)
	print("911 Call Center Charge:  $% 8.2f" % callCentreChrg)
	print("- - - - - - - - - - - - - - - - - - - -")
	print("Total Base Charge:       $% 8.2f" % totalChrg)
	print("Tax Charge (@5%):        $% 8.2f" % tax)
	print("---------------------------------------")
	print("Grand Total Charge:      $% 8.2f" % grandTotal)

if __name__ == "__main__": main()