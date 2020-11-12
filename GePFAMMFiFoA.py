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
	frames = []
	import PIL
	for img in list:
		opened = PIL.Image.open(img)
		width, height = opened.size
		if width!=height:
			animated.append(img)
			frames.append(height/width)
	return (animated, frames)

def createFile(name, speed, frames):
	out="{\n	\"animation\": {\n	\"frametime\": "+str(speed)+",\n	\"frames\": [\n"
	for x in range(frames-1):
		out+="	"+str(x)+",\n"
	out+="	"+str(frames-1)+"\n"
	out+="		]\n	}\n}"
	print(out)



def main():
	importPIL()
	print(sort(walk()))
	print("\n")
	createFile(1,1,12)

main()
