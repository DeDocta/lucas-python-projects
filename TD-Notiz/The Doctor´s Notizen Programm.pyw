from tkinter import *
from tkinter import filedialog

main = Tk()
main.title("TheDoctor´s Notizen Programm")
main.geometry("450x530")
main.iconbitmap('assets/icon.ico')

###############################################################################################

def safe():
    dateiname = open("Notizen.txt", "w")
    dateiname.write(textfeld.get("1.0", END))
    dateiname.close

def delete():
    textfeld.delete("1.0", END)

scrollbar = Scrollbar(main)
scrollbar.pack(side=RIGHT, fill=Y)

textfeld = Text(font=("Helvetica"), bg="black", fg="green", selectbackground="blue", selectforeground="red", cursor="dotbox", insertbackground='red')
textfeld.pack(pady=5)

textfeld.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textfeld.yview)

scroll = Scrollbar(textfeld)

clearbutton = Button(text="Notizfeld Leeren", command=delete, fg="red")
clearbutton.pack()

createbutton = Button(text="Speichern im Ordner (Notizen.txt)", command=safe, fg="green")
createbutton.pack()

warning = Label(fg="red", text="!WARNUNG!\nNotizen.txt wird beim Speichern überschrieben!")
warning.pack()

###############################################################################################
main.resizable(False, False)
main.mainloop()