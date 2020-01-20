from tkinter import *
from tkinter import messagebox
 
 
def clear():
    name_entry.delete(0, END)
    name_entry1.delete(0, END)
    name_entry2.delete(0, END)
    name_entry3.delete(0, END)
    name_entry4.delete(0, END)
    name_entry5.delete(0, END)

def add():
  pass  
 
root = Tk()
root.title("Мой фитнес 2020")
root.geometry("350x300+150+200")

 
name_label = Label(text="Приседания:")
name_label.grid(row=0, column=0, padx=10, pady=10, ipadx=10, sticky="w")
name_label = Label(text="Повороты:")
name_label.grid(row=1, column=0, padx=10, pady=10, ipadx=10,sticky="w")
name_label = Label(text="Колени вверх:")
name_label.grid(row=2, column=0, padx=10, pady=10, ipadx=10,sticky="w")
name_label = Label(text="Повороты шея:")
name_label.grid(row=3, column=0, padx=10, pady=10, ipadx=10,sticky="w")
name_label = Label(text="Планка:")
name_label.grid(row=4, column=0, padx=10, pady=10, ipadx=10,sticky="w")
name_label = Label(text="Руки в стороны:")
name_label.grid(row=5, column=0, padx=10, pady=10, ipadx=10,sticky="w")
 
 
name_entry = Entry()
name_entry1 = Entry()
name_entry2 = Entry()
name_entry3 = Entry()
name_entry4 = Entry()
name_entry5 = Entry()

name_entry.grid(row=0,column=1, padx=5, pady=5)
name_entry1.grid(row=1,column=1, padx=5, pady=5)
name_entry2.grid(row=2,column=1, padx=5, pady=5)
name_entry3.grid(row=3,column=1, padx=5, pady=5)
name_entry4.grid(row=4,column=1, padx=5, pady=5)
name_entry5.grid(row=5,column=1, padx=5, pady=5)

 
# вставка начальных данных
name_entry.insert(0, "Количество")
name_entry1.insert(0, "Количество")
name_entry2.insert(0, "Количество")
name_entry3.insert(0, "Количество")
name_entry4.insert(0, "Количество")
name_entry5.insert(0, "Количество")

 
clear_button = Button(text="Очистить", command=clear)
add_button = Button(text="Добавить", command=add)
 

clear_button.grid(row=7, column=1, padx=5, pady=5, sticky="e")
add_button.grid(row=7, column=0, padx=5, pady=5, sticky="e")
 
root.mainloop()