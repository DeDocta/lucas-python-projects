###########################
# Programmed by TheDoctor #
###########################

#============-<Imports>-=========================================================================================================================

from tkinter import *
import pytube

#============-<Hauptfenster>-====================================================================================================================

main = Tk()
main.title("TheDoctor´s Youtube Downloader")
main.geometry("1000x600")
main.iconbitmap("assets/icon.ico")

#============-<Listen/Variablen etc...>-=========================================================================================================



#============-<Funktionen/Klassen etc...>-=======================================================================================================

def startdownload():
    url = Linkeingabe.get("1.0", END)
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download('downloads')

#============-<main code>-=======================================================================================================================

platzhalter = Label(main, fg="white", bg="white", height=10, text="Youtube Video URL eingeben")
platzhalter.pack()

platzhalter2 = Label(main, fg="white", bg="white", height=2)

Background = Label(main, width=10000000, height=1000000000, bg='red')
Background.pack()

Linkeingabe = Text(Background, fg='blue', height=1)
Linkeingabe.pack()

platzhalter2.pack()

Downloadbutton = Button(main, text="Download", bg='white', fg='red', command=startdownload)
Downloadbutton.pack()

#============-<Informationen>-===================================================================================================================



#================================================================================================================================================

main.mainloop()