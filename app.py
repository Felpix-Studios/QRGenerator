import PIL.Image,PIL.ImageTk

import qrcode
import sys,os
from tkinter import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def refresh(self):
  self.update()
def generate():
  conv=urlEntry.get()
  print(conv)
  img=qrcode.make(conv)
  img.save("qr.png","PNG")

  pres=PIL.ImageTk.PhotoImage(PIL.Image.open("qr.png"))

  panel.configure(image=pres)
  refresh()




root=Tk()
root.title("QR Generator")
root.geometry('800x600')
header=Label(root,text="Enter a URL")
urlEntry=Entry(root,width=36)
button=Button(root,text="Generate QR Code", command=generate)
panel=Label(root,image=None)
header.pack()
urlEntry.pack()
button.pack()
panel.pack()
root.mainloop()