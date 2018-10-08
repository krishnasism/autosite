#python controller.py --image images/test2.png --width 0.955
import object_size as gen
import argparse
import code_strings as code
import os

exists = os.path.isfile("index.html")
if exists:
    os.remove("index.html")

f=open("index.html","a+")

f.write(code.start)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-w", "--width", type=float, required=True,
	help="width of the left-most object in the image (in inches)")
args = vars(ap.parse_args())

gen.generate(args["image"],args["width"],f)

f.write(code.end)