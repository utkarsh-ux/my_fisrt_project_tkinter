#remember don't import everything from tkinter as it gives you 100+ error if don't use all.
#Import single

from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import mainloop
from tkinter import Tk
from tkinter import END
from tkinter import messagebox

root = Tk()
root.title("Мой фитнес 2020")
root.geometry("350x300+150+200")


def clear():
    name_entry.delete(0, END)
    name_entry1.delete(0, END)
    name_entry2.delete(0, END)
    name_entry3.delete(0, END)
    name_entry4.delete(0, END)
    name_entry5.delete(0, END)


def add():
    f = open('fitnes.txt', 'a')
    f.write(name_label1.winfo_name())
    f.write('---')
    sid = name_entry.get()
    f.write(sid)
    f.write('\n')
    ##########
    f.write(name_label2.winfo_name())
    f.write('---')
    turn = name_entry1.get()
    f.write(turn)
    f.write('\n')
    ###########
    f.write(name_label3.winfo_name())
    f.write('---')
    koleni = name_entry2.get()
    f.write(koleni)
    f.write('\n')
    ############
    f.write(name_label4.winfo_name())
    f.write('---')
    shea = name_entry3.get()
    f.write(shea)
    f.write('\n')
    ##########
    f.write(name_label5.winfo_name())
    f.write('---')
    planka = name_entry4.get()
    f.write(planka)
    f.write('\n')
    #######
    f.write(name_label6.winfo_name())
    f.write('---')
    hands = name_entry5.get()
    f.write(hands)
    f.write('\n')
    f.close()



name_label1 = Label(text="Приседания:")
name_label1.grid(row=0, column=0, padx=10, pady=10, ipadx=10, sticky="w")
name_label2 = Label(text="Повороты:")
name_label2.grid(row=1, column=0, padx=10, pady=10, ipadx=10, sticky="w")
name_label3 = Label(text="Колени вверх:")
name_label3.grid(row=2, column=0, padx=10, pady=10, ipadx=10, sticky="w")
name_label4 = Label(text="Повороты шея:")
name_label4.grid(row=3, column=0, padx=10, pady=10, ipadx=10, sticky="w")
name_label5 = Label(text="Планка:")
name_label5.grid(row=4, column=0, padx=10, pady=10, ipadx=10, sticky="w")
name_label6 = Label(text="Руки в стороны:")
name_label6.grid(row=5, column=0, padx=10, pady=10, ipadx=10, sticky="w")

name_entry = Entry()
name_entry1 = Entry()
name_entry2 = Entry()
name_entry3 = Entry()
name_entry4 = Entry()
name_entry5 = Entry()

name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry1.grid(row=1, column=1, padx=5, pady=5)
name_entry2.grid(row=2, column=1, padx=5, pady=5)
name_entry3.grid(row=3, column=1, padx=5, pady=5)
name_entry4.grid(row=4, column=1, padx=5, pady=5)
name_entry5.grid(row=5, column=1, padx=5, pady=5)

# вставка начальных данных
name_entry.insert(0, "Количество")
name_entry1.insert(0, "name_entry1")
name_entry2.insert(0, "Количество")
name_entry3.insert(0, "Количество")
name_entry4.insert(0, "Количество")
name_entry5.insert(0, "Количество")

clear_button = Button(text="Очистить", command=clear)
add_button = Button(text="Добавить", command=add)

clear_button.grid(row=7, column=1, padx=5, pady=5, sticky="e")
add_button.grid(row=7, column=0, padx=5, pady=5, sticky="e")

root.mainloop()
# © 2020
