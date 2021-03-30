###########################
# Programmed by TheDoctor #
###########################

from tkinter import *
from tkinter import filedialog
from tkinter import font
import os


main = Tk()
main.title("TheDoctor´s Texteditor Programm")
main.geometry("1000x700")
main.iconbitmap("assets/icon.ico")

################################################################################################################

def save():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="C:/Desktop/", title="Speichern als ...")
    if filename:
        with open(filename, 'w') as fn:
            fn.write(text.get("1.0", END))

def td_open():
    filename = filedialog.askopenfilename(initialdir="C:/Desktop/", title="Speichern Als ...")
    if filename:
        with open(filename, 'r') as fn:
            stuff = fn.read()
            text.insert(END, stuff)

def td_clear():
    def fclear():
        text.delete("1.0", END)
        rly.destroy()
    rly = Tk()
    rly.title("Leeren")
    rly.iconbitmap("assets/icon.ico")
    rly.resizable(False, False)
    frage = Label(rly, text="Willst du wirklich das Textfeld leeren?", fg='red')
    frage.pack()
    ja = Button(rly, text="Ja", command=fclear, fg='red')
    ja.pack()
    nein = Button(rly, text="Nein", fg='green', command=rly.destroy)
    nein.pack()


def credit():
    credit = Tk()
    credit.iconbitmap("assets/icon.ico")
    credit.title("Credits")
    credit1 = Label(credit, text="Texteditor Pogrammiert und desingt von TheDoctor!\nDanke für das benutzen dieses Programmes!", fg='red', bg='black')
    credit1.pack()
    ok_button = Button(credit, text="Ok", fg='green', bg='black', command=credit.destroy)
    ok_button.pack()

def light():
    text.config(fg="black", bg="white", insertbackground="black", selectforeground="gray", selectbackground="white")

def dark():
    text.config(fg="white", bg="gray", insertbackground="blue", selectforeground="black", selectbackground="blue")

def hack():
    text.config(fg="red", bg="black", insertbackground="green", selectforeground="green", selectbackground="black")

def td_close():
    def fclose():
        main.destroy()
        close.destroy()
    close = Tk()
    close.title("Schließen")
    close.iconbitmap("assets/icon.ico")
    close.resizable(False, False)
    frage = Label(close, text="Wilst du das Pogramm Verlassen?\nUngespeicherte Daten können verloren gehen!", fg='red')
    frage.pack()
    ja = Button(close, text="Ja", command=fclose, fg='red')
    ja.pack()
    nein = Button(close, text="Nein", fg='green', command=close.destroy)
    nein.pack()



menu = Menu(main)
main.config(menu=menu)
filemenu = Menu(menu)
configmenu = Menu(menu)
thememenu = Menu(configmenu)

menu.add_cascade(label="Datei", menu=filemenu)
menu.add_cascade(labe="Einstellungen", menu=configmenu)

filemenu.add_command(label="Speichern", command=save)
filemenu.add_command(label="Datei Öffnen", command=td_open)
filemenu.add_command(label="Textfeld Leeren", command=td_clear)
filemenu.add_separator()
filemenu.add_command(label="Schließen", command=td_close)

configmenu.add_cascade(label="Aussehen", menu=thememenu)
configmenu.add_separator()
configmenu.add_command(label="Credits", command=credit)

thememenu.add_command(label="Dunkel", command= dark)
thememenu.add_command(label="Hell", command=light)
thememenu.add_command(label="Hacker", command=hack)


sb1 = Scrollbar()
text = Text(yscrollcommand=sb1.set, width=120, height=500, insertbackground="black")
text.size()
text.pack()

################################################################################################################

main.resizable(False, False)
main.mainloop()