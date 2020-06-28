# Ch1Ex008.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 8
# Title: Widgets and Gizmos

def main():
	widgetWt = 75
	gizmoWt = 112
	numWidgets = int(input("No. of Widgets: "))
	numGizmos = int(input("No. of Gizmos: "))

	totalWt = (widgetWt * numWidgets) + (gizmoWt * numGizmos)

	print("Total Weight: %d g" % totalWt)

if __name__ == "__main__": main()