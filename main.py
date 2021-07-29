from tkinter import *
from threading import Thread
from gui import *
from variables import *
import generate
import scan


def scanThread():
    scan_win = NewWindow(root, title="Scanner", icon=ICON,
                         width=250, height=175, bg=BACKGROUND, resizableX=1, resizableY=1)
    scan.start(scan_win)


def scanBar():
    t1 = Thread(target=scanThread)
    t1.daemon = 1
    t1.start()


def genThread():
    gen_win = NewWindow(root, title="Generator", icon=ICON,
                        width=385, height=290, bg=BACKGROUND)
    generate.start(gen_win)


def generateBar():
    t1 = Thread(target=genThread)
    t1.daemon = 1
    t1.start()


if __name__ == '__main__':
    # Making Window
    root = GUI("Bar Code", icon=ICON, width=250, height=100, bg=BACKGROUND)

    # Window Design
    scan_btn = Button(root, text="Scan", width=20, command=scanBar)
    gen_btn = Button(root, text="Generate", width=20, command=generateBar)
    scan_btn.pack(pady=10)
    gen_btn.pack(pady=10)

    # Starting Window
    root.start()
