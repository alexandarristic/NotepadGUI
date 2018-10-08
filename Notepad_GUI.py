#Make a simple "Notepad-like" GUI to read and edit text files within a window
#Alexandar Ristic, October 2018

from Tkinter import *
from tkFileDialog import *

root = Tk()
root.title("File reader")
write = Text(root,height=20,width=40,wrap=WORD)
scroll = Scrollbar(root)
menubar = Menu(root)
filemenu= Menu(menubar,tearoff=0)

def openFile():
    name = askopenfilename(title="Select a file")
    with open(name) as inFile:
        for line in inFile:
            write.insert(END,line + "\n")

def saveFile():
    savename = asksaveasfile(mode='w')
    if savename != None:
        data = write.get('1.0',END)
        savename.write(data)
        savename.close()


filemenu.add_command(label='Open',command=openFile)
filemenu.add_command(label='Save',command=saveFile)
filemenu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label='File',menu=filemenu)

scroll.pack(side=RIGHT,fill=Y)
write.pack(side=LEFT,fill=Y)
scroll.config(command=write.yview)
write.config(yscrollcommand = scroll.set)

root.config(menu=menubar)
root.mainloop()
