def genWeb(xy,imA, imB, dimA, dimB, color,f,ppm):
    import readtext
    
    a=int(dimA*ppm)
    
    b=int(dimB*ppm)
    text= readtext.ocr(xy,b,a)
    
    print(text)
    print("DIMENSIONS OF DIV : "+str(a)+","+str(b))
    print(str(imA)+" inches X "+str(imB)+" inches")
    print("DIMENSIONS OF image : "+str(imA)+","+str(imB))

    imA-=200 #account for placement of reference
    
    pa=int((a/imA*100))
    pb=int((b/imB*100))
    
   
    if(len(text)==0):
        text="This is a demonstration."
    
    
    
    display="block"
    if(int(dimB)<5):
        display="inline-block"
    
    
    style="""style=\"
    border: 0px solid black;
    padding: 2px;
    text-align: center;
    background-color:rgb"""+str(color)+"""
   ; height:"""+str(pa)+"""%
    ; width:"""+str(pb)+"""%
    ; margin-bottom:"""+str(10)+"""
    ; margin-left:"""+str(10)+"""
    ; display:"""+display+"""
    ;}\""""
    
    genCode="<div "+style+"> <p style=\"font-family:Courier New; color:white; font-size:20px;\">"+text+"</p> </div>\n"
    
    
    f.write(genCode)
    
    
