from PIL import Image,ImageEnhance

img=Image.open("images/11.png")
d=img.info['dpi'][0]

img.show
cn=ImageEnhance.Contrast(img)
img=cn.enhance(3.0)
bn=ImageEnhance.Brightness(img)
img=bn.enhance(3.0)


img.save("images/output.png", dpi=(d,d))