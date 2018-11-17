from capture import takePicture
from crop import main as cropMain
import thorpy
import pygame
from controller import startGenerate

pygame.display.init()

application = thorpy.Application(size=(300, 300), caption="Real Time Website Generator")

takepicbutt = thorpy.make_button("Take Picture",func=takePicture)
croppicbutt = thorpy.make_button("Crop Picture",func=cropMain)

genwebbutt = thorpy.make_button("Generate Website",func=startGenerate)

quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_menu_func)

background = thorpy.Background.make(color=(200, 200, 255),
                                    elements=[takepicbutt,croppicbutt,genwebbutt, quit_button])

thorpy.store(background)

menu = thorpy.Menu(background)
menu.play() 

application.quit()

