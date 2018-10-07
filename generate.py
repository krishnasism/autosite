
def genWeb(dimA, dimB, color):
   
    
    
    
    filename="index.html"

    f=open(filename,"a+")
    a=str(int(dimA*60))
    b=str(int(dimB*60))
    
    display="block"
    if(int(dimB)<5):
        display="inline-block"
    
    
    style="""style=\"
    border: 0px solid black;
    padding: 2px;
    text-align: center;
    background-color:rgb"""+str(color)+"""
   ; height:"""+a+"""
    ; width:"""+b+"""
    ; margin-bottom:"""+str(10)+"""
    ; margin-left:"""+str(10)+"""
    ; display:"""+display+"""
    ;}\""""
    
    genCode="<div "+style+"> <p style=\"font-family:Courier New; color:white; font-size:20px;\">This is a demonstration.</p> </div>\n"
    
    
    f.write(genCode)
    
    
