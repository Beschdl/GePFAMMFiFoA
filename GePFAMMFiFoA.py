import sys
import os
import requests
import subprocess

folder_path="testfiles"

base_speed = 4

print()

def importPIL():
	try:
		from PIL import Image
	except:
		subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
		sys.exit()

def walk(df):
	allPngs = [os.path.join(root,name)
				for (root, dirs, files) in os.walk(str(df))
				for name in files
				if name.endswith(("png"))]
	return allPngs

def sort(list):
	animated = []
	frames = []
	import PIL
	from PIL import Image
	for img in list:
		opened = PIL.Image.open(img)
		width, height = opened.size
		if width!=height:
			animated.append(img)
			frames.append(height/width)
	return animated, frames

def createFile(name, speed, frames):
	out="{\n	\"animation\": {\n	\"frametime\": "+str(speed)+",\n	\"frames\": [\n"
	for x in range(frames-1):
		out+="	"+str(x)+",\n"
	out+="	"+str(frames-1)+"\n"
	out+="		]\n	}\n}"
	file = open(name.replace("png", "mcmeta"),"w")
	file.write(out)

def generate(fd):
		allNames, allFrames = sort(walk(fd))
		i = 0
		for f in allNames:
			createFile(f, base_speed, int(allFrames[i]))
			i+=1


def main():
	importPIL()
	generate(folder_path)
