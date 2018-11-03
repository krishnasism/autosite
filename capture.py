
def takePicture():  
    import cv2
    
    #cap = cv2.VideoCapture("0") #default webcam
    cap = cv2.VideoCapture("http://192.168.0.100:8080/videofeed")  #IP Camera
    while(True):
        ret,frame = cap.read() 
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite("images/capture.png",frame) #change this when camera added
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
