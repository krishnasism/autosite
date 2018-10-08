def ocr(xy,h,w):
    import cv2
    import pytesseract
    from PIL import Image
    
    
    img = cv2.imread("images/test2.png")
    x=int(xy[0])
    y=int(xy[1])
    print(str(x)+","+str(y))
    crop_img = img[y:y+w, x:x+h]
    
    #cv2.imshow("cropped", crop_img)
    cv2.imwrite("images/cropped.png",crop_img)
    text = pytesseract.image_to_string(Image.open("images/cropped.png"))

    #cv2.waitKey(0)
    
    return text
