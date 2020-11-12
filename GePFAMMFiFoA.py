import sys
import os
import tkinter
import requests
import subprocess


print()

def importPIL():
	try:
		from PIL import Image
	except:
		subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
		sys.exit()

def getSize(filen):
	img = Image.open(filen)
	width, height = img.size

def walk():
	allPngs = [os.path.join(root,name)
				for (root, dirs, files) in os.walk("testfiles")
				for name in files
				if name.endswith(("png"))]
	return allPngs

def sort(list):
	animated = []
	import PIL
	for img in list:
		opened = PIL.Image.open(img)
		width, height = opened.size
		if width!=height:
			animated.append(img)
	return animated

def main():
	importPIL()
	print(sort(walk()))


main()
