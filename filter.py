from PIL import Image,ImageEnhance
#import cv2
#import numpy

img=Image.open("images/11.png")
d=img.info['dpi'][0]

#img=cv2.imread("p.jpg")
img.show
cn=ImageEnhance.Contrast(img)
img=cn.enhance(3.0)
bn=ImageEnhance.Brightness(img)
img=bn.enhance(3.0)

#pil_image = img.convert('RGB') 
#open_cv_image = numpy.array(pil_image) 

#open_cv_image = open_cv_image[:, :, ::-1].copy() 
#cv2.imwrite("images/output.png",open_cv_image)


img.save("images/output.png", dpi=(d,d))