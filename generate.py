def genWeb(xy,imA, imB, dimA, dimB, color,f):
    import readtext
    from PIL import Image
    import code_strings as cs
    im=Image.open(cs.filename)
    dpi=im.info['dpi'][0]

    
    a=int(dimA*dpi)
    b=int(dimB*dpi)
    text= readtext.ocr(xy,b,a)
    print(text)
    imA-=200 #account for placement of reference
    
    pa=int((a/imA*100))
    pb=int((b/imB*100))
    
    #from win32api import GetSystemMetrics
    
    #syswidth= GetSystemMetrics(0)
    #sysheight= GetSystemMetrics(1)
    
    #pa=int((a/imA*100)*sysheight/imA)
    #pb=int((b/imB*100)*syswidth/imB)
   
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
    
    
