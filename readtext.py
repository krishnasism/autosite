def ocr(xy,h,w):
    import cv2
    import pytesseract
    from PIL import Image
    import code_strings as cs
    import os
        
    img = cv2.imread(cs.filename)
    x=int(xy[0])
    y=int(xy[1])
    print(str(x)+","+str(y))
    crop_img = img[y:y+w, x:x+h]
    
    
    cv2.imwrite("images/cropped.png",crop_img)
    

    if os.path.exists("images/cropped.png") and os.path.getsize("images/cropped.png") > 0:
        text = pytesseract.image_to_string(Image.open("images/cropped.png"))
    else:
        text=""

    
    return text


def checkFile():
    import os

    if os.path.exists("images/cropped.png") and os.path.getsize("images/cropped.png") > 0:
        return True
    else:
        return False