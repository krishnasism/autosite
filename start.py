def takePic():
    print("I was pressed")






import thorpy

application = thorpy.Application(size=(300, 300), caption="Real Time Website Generator")

takepicbutt = thorpy.make_button("Take Picture",func=takePic())
croppicbutt = thorpy.make_button("Crop Picture")
genwebbutt = thorpy.make_button("Generate Website")

#a button for leaving the application:
quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_menu_func)

#a background which contains quit_button and useless_button
background = thorpy.Background.make(color=(200, 200, 255),
                                    elements=[takepicbutt,croppicbutt,genwebbutt, quit_button])

thorpy.store(background)

menu = thorpy.Menu(background)
menu.play() 

application.quit()

