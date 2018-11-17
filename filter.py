def postProcess():
    from PIL import Image,ImageEnhance
    
    img=Image.open("images/output.png")
    
    img.show
    cn=ImageEnhance.Contrast(img)
    img=cn.enhance(3.0)
    bn=ImageEnhance.Brightness(img)
    img=bn.enhance(3.0)
    
    
    img.save("images/output.png")