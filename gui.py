from tkinter import *


class GUI(Tk):
    def __init__(self, title="Window", icon=None, width=200, height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.iconbitmap(icon)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()

    def stop(self):
        self.destroy()


class NewWindow(Toplevel):
    def __init__(self, master, title="Window", icon=None, width=200, height=200, bg="white",
                 resizableX=0, resizableY=0):
        super().__init__(master)
        self.title(title)
        self.iconbitmap(icon)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)
