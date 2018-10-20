import object_size as gen
import code_strings as code
import os
import capture as cap



exists = os.path.isfile("index.html")
if exists:
    os.remove("index.html")

cap.takePicture()
f=open("index.html","a+")

f.write(code.start)

image="images/capture.png"
refS=0.955

gen.generate(image,refS,f)

f.write(code.end)