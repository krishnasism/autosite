
def genWeb(imA, imB, dimA, dimB, color,f):
    
    a=int(dimA*60)
    b=int(dimB*60)
    
    imA-=200 #account for placement of reference
    
    pa=int((a/imA*100))
    pb=int((b/imB*100))
    
    #from win32api import GetSystemMetrics
    
    #syswidth= GetSystemMetrics(0)
    #sysheight= GetSystemMetrics(1)
    
    #pa=int((a/imA*100)*sysheight/imA)
    #pb=int((b/imB*100)*syswidth/imB)
   
    
    
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
    
    genCode="<div "+style+"> <p style=\"font-family:Courier New; color:white; font-size:20px;\">This is a demonstration.</p> </div>\n"
    
    
    f.write(genCode)
    
    
