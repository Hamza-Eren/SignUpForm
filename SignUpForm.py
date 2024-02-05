# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:26:16 2024

@author: HamzaEren
"""

from tkinter import Tk, Label, LabelFrame, StringVar, Radiobutton, Entry, ttk, Button

def signUp():
    person = {
        "cinsiyet" : var.get(),
        "name" : name.get(),
        "age" : int(combo.get())
    }
    print(person)

app = Tk()
app.title("Sign Up")
app.geometry("300x290")
app.resizable(0, 0)

title_lbl = Label(app, text="Sign Up Form")
title_lbl.place(x=0, y=20, width=300, height=30)

gender_frame = LabelFrame(app, text="Gender")
gender_frame.place(x=20, y=60, width=260, height=50)
var = StringVar()
m = Radiobutton(gender_frame, text="Male", variable=var, value="Male")
m.place(x=0, y=0, width=120, height=20)
f = Radiobutton(gender_frame, text="Female", variable=var, value="Female")
f.place(x=120, y=0, width=120, height=20)

name_frame = LabelFrame(app, text="Name")
name_frame.place(x=20, y=120, width=260, height=40)
name = Entry(name_frame, background="SystemButtonFace", borderwidth=0, font=("Segoe UI", 10))
name.place(x=5, y=0, width=250, height=20)

age_frame = LabelFrame(app, text="Age")
age_frame.place(x=20, y=170, width=260, height=50)
combo = ttk.Combobox(age_frame, state="readonly", values=[x for x in range(18, 65)])
combo.place(x=10, y=5, width=235, height=20)

btn = Button(app, text="Sign Up", command=signUp)
btn.place(x=30, y=240, width=240, height=30)

app.mainloop()
