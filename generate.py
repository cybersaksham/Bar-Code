from tkinter import *
from variables import *


def showBar(filename, gen_win):
    from PIL import ImageTk, Image
    img_init = Image.open(filename)
    img_init = img_init.resize((350, 170), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_init)
    qr_img = Label(gen_win, image=img, bg=BACKGROUND)
    qr_img.photo = img
    qr_img.grid(row=3, column=0, columnspan=3, padx=12, pady=5)


def generateBar(gen_win):
    from tkinter.filedialog import asksaveasfilename
    import tkinter.messagebox as tmsg
    filename = asksaveasfilename(title="Save Barcode", initialfile="bar.png",
                                 filetypes=(
                                     ("PNG Images", "*.png"),
                                     ("JPG Images", "*.jpg"),
                                     ("ALL Files", "*.*")
                                 ),
                                 defaultextension=".png")
    if filename != "":
        try:
            import code128
            bar = code128.image(url_str.get())
            bar.save(filename)
            showBar(filename, gen_win)
        except:
            tmsg.showerror(title="Error", message="In-appropriate File")


def start(gen_win):
    global url_str

    # Window Design
    url_label = Label(gen_win, text="Enter URL", bg=BACKGROUND)
    url_str = StringVar()
    url_entry = Entry(gen_win, textvariable=url_str, width=50)
    submit_btn = Button(gen_win, text="Generate", command=lambda: generateBar(gen_win))
    url_label.grid(row=0, column=0, padx=11, pady=5)
    url_entry.grid(row=0, column=1, columnspan=3)
    submit_btn.grid(row=1, column=1, pady=5, columnspan=3)
