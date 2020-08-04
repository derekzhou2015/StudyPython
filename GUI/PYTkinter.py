#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'Kerwin'
from tkinter import Frame,Label,Button,Entry
import tkinter.messagebox as messagebox

class Appliction(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.master.title('Kerwin')
        self.master.geometry("400x300")
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        lable = Label(self, text='Hello,World.')
        self.nameInput = Entry(self)
        alterButton = Button(self,text='hit me',command=self.alterButton_Handle)
        quitButton = Button(self, text='quit', command=self.quit)
        lable.pack()
        self.nameInput.pack()
        alterButton.pack()
        quitButton.pack()

    def alterButton_Handle(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Appliction()
app.mainloop()
print(app)
print("----------------------------------")
