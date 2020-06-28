# Ch2Ex054.py
# Author: Parshwa Patil
# ThePythonWorkbook Solutions
# Exercise No. 54
# Title: Wavelengths of Lisible Light

def main():
	wavelen = int(input("Wavelength: "))

	if wavelen < 380: print("Outside Visible Spectrum")
	elif wavelen < 450: print("Color: Violet")
	elif wavelen < 495: print("Color: Blue")
	elif wavelen < 570: print("Color: Green")
	elif wavelen < 590: print("Color: Yellow")
	elif wavelen < 620: print("Color: Orange")
	elif wavelen < 750: print("Color: Red")
	else: print("Outside Visible Spectrum")

if __name__ == "__main__": main()