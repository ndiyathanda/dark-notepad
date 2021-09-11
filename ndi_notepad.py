import re
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText

root = Tk()
root['background']='black'
root.title('Notepad')

notepad = ScrolledText(root, width = 100, height = 50, bg='black', fg='white')
fileName = ' '

def new():
    global fileName
    if len(notepad.get('1.0', END + '-1c')) > 0:
        if messagebox.askyesno("Notepad", "Do you want to save changes?"):
            save()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")


def open():
    fd = filedialog.askopenfile(parent=root, mode='r')
    t = fd.read()  # t is the text read through filedialog
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)


def save():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if fd != None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message="Not able to save file!")


def saveas():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = notepad.get(0.0, END)  # t stands for the text gotten from notepad
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message="Not able to save file!")


def exit():
        root.destroy()

def clear():
    notepad.event_generate("<<Clear>>")

def find():
    notepad.tag_remove("Found", '1.0', END)
    find = simpledialog.askstring("Find", "Find: ")
    if find:
        idx = '1.0'
    while 1:
        idx = notepad.search(find, idx, nocase=1, stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' % (idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground='white', background='red')
    notepad.bind("<1>", click)

def click(event):
    notepad.tag_config('Found', background='white', foreground='blue')

def selectall():
    notepad.event_generate("<<SelectAll>>")

notepadMenu = Menu(root)
root.configure(menu=notepadMenu)

fileMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='File', menu = fileMenu)

fileMenu.add_command(label='New', command = new)
fileMenu.add_command(label='Open...', command = open)
fileMenu.add_command(label='Save', command = save)
fileMenu.add_command(label='Save As...', command = saveas)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command = exit)

editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Edit', menu = editMenu)

editMenu.add_command(label='Find...', command = find)
editMenu.add_command(label='Select All', command = selectall)

notepad.pack()
root.mainloop()


