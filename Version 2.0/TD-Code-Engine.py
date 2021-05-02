from tkinter import *
import tkinter.ttk as sutk
from tkinter import messagebox
from tkinter import filedialog

import os
import sys
import threading
import subprocess
import random
import time
from shutil import copyfile, move

main = Tk()
main.title('TD-Code Engine')
main.configure(bg='black')
main.wm_iconbitmap('icon.ico')
main.geometry('1000x600')
main.resizable(False, False)

def shließen():
    if messagebox.askokcancel("Close", "Are you sure to Close the Engine?"):
        main.destroy()

#==========================================================================================

#start
UseConsoleMode = Button(text='Console Mode', fg='black')
UseIDEmode = Button(text='Editor Mode', fg='black')
UseFileRunnerMode = Button(text='Engine Mode', fg='black')

#console
Consolelog = Text(fg='green', bg='black', width=125, height=30)
Consolelog.insert(END, 'TD-Engine Built in Console - COPYRIGHT: TheDoctor 2021\n"help" for help\n \n')
Consolelog.config(state="disabled")
PL_grf = Label(bg='black')
commandentry = Entry(PL_grf, width=40, fg='red', bg='gray')
Enterbutton = sutk.Button(PL_grf, text='Send ->')

#Engine
Actionlog = Text(fg='green', bg='black', width=125, height=30)
Actionlog.insert(END, 'TD-Code Engine - COPYRIGHT: TheDoctor 2021\n')
Actionlog.config(state="disabled")
Enginelabel01 = Label(bg='black')
Choosefilebutton = sutk.Button(Enginelabel01, text='Choose file to run')
Runenginebutton = sutk.Button(Enginelabel01, text='Run Selectet File')
Clearengineconsole = sutk.Button(Enginelabel01, text='Clear Engine Console')

#==========================================================================================

def commandengine(data):
    data = data.rstrip('\n')
    command = data.split(' ')
    command = command[0]
    global checkforcomment
    checkforcomment = command[0]
    if not checkforcomment == '#':
        data = data.lstrip(f'{command} ')
        global ausgabe
        ausgabe = ''
        if command == 'help':
            ausgabe = 'Help - List:\n-say <text>\n-sleep <time in seconds>\n-write <textfile.txt> <text>\n-read <textfile>\n-help\n-copy <file/path> <second/file/path>\n-smyle\n-rand <minimum number> <maximum number>\n-'

        elif command == 'say':
            ausgabe = data
        
        elif command == 'sleep':
            data = int(data)
            time.sleep(data)

        elif command == 'write':
            nachricht = data.split(' ')
            file_to_open = nachricht[0]
            nachricht.remove(nachricht[0])
            nachricht = ' '.join(nachricht)
            print(nachricht)
            with open(file_to_open, 'w', encoding='utf-8') as file:
                file.write(nachricht)
                file.close()

        elif command == 'read':
            with open(data, 'r', encoding='utf-8') as file:
                ausgabe = file.read()

        elif command == 'smyle':
            ausgabe = '                   __ooooooooo__\n              oOOOOOOOOOOOOOOOOOOOOOo\n          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo\n       oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo\n     oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo\n   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo\n  oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo\n oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo\n oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo\noOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo\noOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo\noOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo\n *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*\n *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*\n  *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*\n   *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*\n     *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*\n       *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*   \n          *OOOOOOOOo           oOOOOOOOO*   \n              *OOOOOOOOOOOOOOOOOOOOO*    \n                   ""ooooooooo""\n'

        elif command == 'rand':
            nachricht = data.split(' ')
            number1 = int(nachricht[0])
            number2 = int(nachricht[1])
            ausgabe = str(random.randint(number1, number2))
        
        elif command == 'copy':
            print(data)
            data = data.split(' ')
            print(data)
            copyfile(data[0], data[1])
        
        elif command == 'move':
            print(data)
            data = data.split(' ')
            print(data)
            move(data[0], data[1])

        elif command == '':
            pass

        else:
            ausgabe = 'Command not Found!'

    command = ''
    return ausgabe

#==========================================================================================

def IDE_MODE():
    IDE_main = Tk()
    IDE_main.title('TD-Code Engine - IDE')
    IDE_main.configure(bg='black')
    IDE_main.geometry('1000x600')
    IDE_main.resizable(False, False)
    IDE_main.wm_iconbitmap('icon.ico')
    #=========================================================================================

    ideconsolelabel = Label(bg='black')
    ideengineconsole = Text(ideconsolelabel, bg='black', fg='yellow', width=125)
    ideengineconsole.insert(END, 'TD-Engine IDE Built in Console - COPYRIGHT: TheDoctor 2021\n"help" for help\n \n')
    ideengineconsole.config(state='disabled')
    closeideconsole = sutk.Button(ideconsolelabel, text='Close the Console')
    closeideconsole.pack()
    ideengineconsole.pack()
    runstatement = False

    #=========================================================================================
    def closerunconsole():
        ideengineconsole.config(state='normal')
        ideengineconsole.delete('1.0', END)
        ideengineconsole.insert(END, 'TD-Engine IDE Built in Console - COPYRIGHT: TheDoctor 2021\n"help" for help\n \n')
        text.config(height=40)
        ideengineconsole.config(state='disabled')

    closeideconsole.config(command=closerunconsole)

    def shließen():
        if messagebox.askokcancel("Close", "Are you sure to Close the Engine??"):
            IDE_main.destroy()
    
    scr = Scrollbar()
    text = Text(fg='white', bg='black', width=120, height=35)
    scr.config(command=text.yview)
    text.config(yscrollcommand=scr.set)
    scr.pack(side="right", fill="y", expand=False)
    def td_runcode():
        text.config(height=20)
        if runstatement == False:
            ideconsolelabel.pack()
            runstatement == True
        else:
            pass
        code = text.get('1.0', END)
        with open('scriptrunner/idemode.tdco', 'w') as A:
            A.write(code)
            A.close()
        with open('scriptrunner/idemode.tdco', 'r') as B:
            for zeile in B:
                line = zeile.rstrip()
                line = line.rstrip('\n')
                ausgabe = commandengine(line)
                ideengineconsole.config(state='normal')
                ausgabe = ausgabe + '\n'
                ideengineconsole.insert(END, ausgabe)
                ideengineconsole.config(state='disabled')

    def td_open():
        filename = filedialog.askopenfilename(initialdir="C:/Desktop/", title="Open File ...")
        if filename:
            with open(filename, 'r') as fn:
                stuff = fn.read()
                text.delete('1.0', END)
                text.insert(END, stuff)
        
    def td_save():
        filename = filedialog.asksaveasfilename(initialdir="C:/Desktop/", title="Save as ...", initialfile="unnamed.tdco")
        if filename:
            with open(filename, 'w') as fn:
                fn.write(text.get("1.0", END))
    Optionmenu = Menu(fg='blue')
    IDE_main.config(menu=Optionmenu)
    Optionmenu.add_command(label='Save Code', command=td_save)
    Optionmenu.add_command(label='Load Code', command=td_open)
    Optionmenu.add_command(label='Run Code', command=td_runcode)
    text.pack()
    IDE_main.protocol("WM_DELETE_WINDOW", shließen)
    IDE_main.mainloop()

def td_main():
    def ConsoleMode():
        main.title('TD-Code Engine - CONSOLE')
        def übertrage():
            command = commandentry.get()
            übertragung = commandengine(command)
            Consolelog.config(state="normal") 
            Consolelog.insert(END, f'\n{übertragung}\n')
            Consolelog.config(state="disabled")
            commandentry.delete(0, END)
        UseIDEmode.destroy()
        UseFileRunnerMode.destroy()
        UseConsoleMode.destroy()
        Consolelog.grid(row=0, column=0)
        PL_grf.grid(row=1, column=0)
        commandentry.grid(row=0, column=0)
        Enterbutton.configure(command=übertrage)
        Enterbutton.grid(row=1, column=0)

    def IDEMode():
        UseIDEmode.destroy()
        UseFileRunnerMode.destroy()
        UseConsoleMode.destroy()
        main.destroy()
        IDE_MODE()
    
    def Enginemode():
        main.title(f'TD-Code Engine - ENGINE')
        UseIDEmode.destroy()
        UseFileRunnerMode.destroy()
        UseConsoleMode.destroy()
        def td_clear_cmd():
            Actionlog.config(state="normal") 
            Actionlog.delete('1.0', END)
            Actionlog.insert(END, 'TD-Code Engine - COPYRIGHT: TheDoctor 2021\n')
            Actionlog.config(state="disabled")

        def td_runengine(file):
            print(file)
            with open(file, 'r') as datei:
                for zeile in datei:
                    übertragung = commandengine(zeile)
                    if übertragung:
                        Actionlog.config(state="normal") 
                        Actionlog.insert(END, f'\n{übertragung}\n')
                        Actionlog.config(state="disabled")


        def td_open():
            filename = filedialog.askopenfilename(initialdir="C:/Desktop/", title="Open File ...")
            if filename:
                global filetorun
                filetorun = filename
                main.title(f'TD-Code Engine - ENGINE - {filetorun}')
        Choosefilebutton.configure(command=td_open)
        Runenginebutton.configure(command=lambda:[td_runengine(filetorun)])
        Actionlog.grid(row=0, column=0)
        Enginelabel01.grid(row=2, column=0)
        Choosefilebutton.grid(row=1, column=0)
        Runenginebutton.grid(row=2, column=0)
        Clearengineconsole.configure(command=td_clear_cmd)
        Clearengineconsole.grid(row=3, column=0)


    
    UseConsoleMode.config(command=ConsoleMode)
    UseIDEmode.config(command=IDEMode)
    UseFileRunnerMode.config(command=Enginemode)

    UseConsoleMode.grid(row=0, column=0)
    UseIDEmode.grid(row=1, column=0)
    UseFileRunnerMode.grid(row=2, column=0)

td_main()

main.protocol("WM_DELETE_WINDOW", shließen)
main.mainloop()
