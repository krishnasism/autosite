
from capture import takePicture
from crop import main as cropMain
from controller import startGenerate

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Toplevel()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
    
    
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family {Yu Gothic} -size 20 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("590x448+336+154")
        top.title("Realtime Website Generator")
        top.configure(background="#05d9e8")
        top.resizable(False, False)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.22, rely=0.067, height=43, width=355)
        self.Label1.configure(background="#05d9e8")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Realtime Website Generator''')
        self.Label1.configure(width=355)

        self.Button1 = tk.Button(top,command=takePicture)
        self.Button1.place(relx=0.271, rely=0.223, height=104, width=117)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#18b2d8")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(cursor="pencil")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self._img1 = tk.PhotoImage(file="capx.png")
        self.Button1.configure(image=self._img1)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Capture''')
        self.Button1.configure(width=117)

        self.Button2 = tk.Button(top,command=cropMain)
        self.Button2.place(relx=0.525, rely=0.223, height=104, width=117)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#18b2d8")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(cursor="plus")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self._img2 = tk.PhotoImage(file="crop.png")
        self.Button2.configure(image=self._img2)
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Crop''')
        self.Button2.configure(width=117)

        self.Button3 = tk.Button(top,command=startGenerate)
        self.Button3.place(relx=0.271, rely=0.469, height=154, width=267)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#18b2d8")
        self.Button3.configure(borderwidth="0")
        self.Button3.configure(cursor="spraycan")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self._img3 = tk.PhotoImage(file="gen.png")
        self.Button3.configure(image=self._img3)
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Generate!''')
        self.Button3.configure(width=267)


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





