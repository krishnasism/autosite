def startGenerate(): 
    import object_size as gen
    import code_strings as code
    import os
    import capture as cap
    import code_strings as cs
    from filter import postProcess
    import webbrowser

    exists = os.path.isfile("index.html")
    if exists:
        os.remove("index.html")
    
    #cap.takePicture() #enable this 
    
    
    f=open("index.html","a+")
    
    f.write(code.start)
    
    image=cs.filename
    refS=0.955
    postProcess()
    gen.generate(image,refS,f)
    
    f.write(code.end)
    webbrowser.open('file://' + os.path.realpath("index.html"))
