import random
import time
from tkinter import *

pferd_animation1 = ['@1', '=', '=', '=', '=', '=', '=', '=', '=', '=']
pferd_animation2 = ['@2', '=', '=', '=', '=', '=', '=', '=', '=', '=']
def rennstrecke_replacement():
    while pferd_animation1[9] or pferd_animation2[9] != '@1' or '@2':
        zufall_1 = random.randint(0, 1)
        while zufall_1 != 0:
            zufall_1 = zufall_1 - 1
            lauf1()

        zufall_2 = random.randint(0, 1)
        while zufall_2 != 0:
            zufall_2 = zufall_2 - 1
            lauf2()

def lauf1():
    global pferd_animation1
    if pferd_animation1[9] != '@1':
        pferd_animation1.pop()
        pferd_animation1.insert(0, '=')
        rennstrecke1.config(text=pferd_animation1)
def lauf2():
    global pferd_animation2
    if pferd_animation2[9] != '@2':
        pferd_animation2.pop()
        pferd_animation2.insert(0, '=')
        rennstrecke2.config(text=pferd_animation2)

def label_replacement1():
    global punkte1
    name_1 = name_entry1.get()
    if name_1 == '':
        show_points_1.config(text=str(punkte1))
        punkte_label1.config(text='Niemands Punkte:')
    else:
        show_points_1.config(text=str(punkte1))
        punkte_label1.config(text=str(name_1) + 's' + ' Punkte:')
def label_replacement2():
    global punkte2
    name_2 = name_entry2.get()
    if name_2 == '':
        show_points_2.config(text=str(punkte2))
        punkte_label2.config(text='Niemands Punkte:')

    else:
        show_points_2.config(text=str(punkte2))
        punkte_label2.config(text=str(name_2) + 's' + ' Punkte:')

punkte1 = 0
punkte2 = 0
# Fenstererstellung
window = Tk()
window.title('Pferdewetten')
window.geometry('400x70')
# Buttons Für Pferde
button_bet1 = Button(window, text='Erstes Pferd')

#Startknopf
start_button = Button(window, text='Start', command=rennstrecke_replacement)
# Labels, Buttons
rennstrecke1 = Label(window, text=pferd_animation1)
rennstrecke2 = Label(window, text=pferd_animation2)

ziellinie1 = Label(window, text='Y')
ziellinie2 = Label(window, text='Y')

# Punkte von 1 und 2
punkte_label1 = Label(window, text='Name vom 1. Spieler' + ':')
punkte_label2 = Label(window, text='Name vom 2. Spieler' + ':')

# Darstellung Points
show_points_1 = Label(window, text='')
show_points_2 = Label(window, text='')

# Eingabe Namen
name_entry1 = Entry(window, bd=2, width=7)
name_entry2 = Entry(window, bd=2, width=7)

# Enter Buttons
enter1 = Button(window, text='Enter', command=label_replacement1)
enter2 = Button(window, text='Enter', command=label_replacement2)


start_button.grid(row=1, column=0)
rennstrecke1.grid(row=1, column=1)
rennstrecke2.grid(row=2, column=1)
ziellinie1.grid(row=1, column=2)
ziellinie2.grid(row=2, column=2)
punkte_label1.grid(row=1, column=3)
punkte_label2.grid(row=2, column=3)
show_points_1.grid(row=1, column=4)
show_points_2.grid(row=2, column=4)
name_entry1.grid(row=1, column=5)
name_entry2.grid(row=2, column=5)
enter1.grid(row=1, column=6)
enter2.grid(row=2, column=6)

mainloop()
def wette_button():
    x = True
