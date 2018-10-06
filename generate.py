
def genWeb(dimA, dimB, color):
   
    
    
    
    filename="index.html"

    f=open(filename,"a+")
    a=str(int(dimA*60))
    b=str(int(dimB*60*2))
    
    display="block"
    if(int(dimB)<5):
        display="inline-block"
    
    
    style="""style=\"
    border: 1px solid black;
    background-color:rgb"""+str(color)+"""
   ; height:"""+a+"""
    ; width:"""+b+"""
    ; margin-bottom:"""+str(10)+"""
    ; margin-left:"""+str(10)+"""
    ; display:"""+display+"""
    ;}\""""
    
    genCode="<div "+style+"> <h1 style=\"font-family:Courier New\">Hello World</h1> </div>\n"
    
    
    f.write(genCode)
    
    