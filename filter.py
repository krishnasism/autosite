from PIL import Image,ImageEnhance
#import cv2
img=Image.open("images/test.png")
d=img.info['dpi'][0]

#img=cv2.imread("p.jpg")
img.show
cn=ImageEnhance.Contrast(img)
img=cn.enhance(2.8)
bn=ImageEnhance.Brightness(img)
img=bn.enhance(1.0)
sn=ImageEnhance.Sharpness(img)
img=sn.enhance(2.5)


img.save("images/output.png", dpi=(d,d))