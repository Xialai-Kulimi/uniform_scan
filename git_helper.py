from tkinter import Tk, messagebox
from tkouter import *
import random


class HelloWorld(TkOutWidget):
    layout = """
<html>
    <head>
        <title> Random Selector </title>
    </head>
    <body>
        <left>
            <entry width="30" textvariable="{self.item.var}" />
            <button width="8" text="Select" command="{self.sel}" />
            <button width="8" text="Add" command="{self.add}" />
        </left>
        <top type="labelframe" name="itemframe" text="Items">
            <listbox name="listbox" />
        </top>
    </body>
</html>
"""
    item = StringField(default='Item Name')
    def hello(self):
        messagebox.showinfo('welcome to tkouter', 'hello world')

    def __init__(self, master):
        super().__init__(master)
        self._items = []

    def sel(self):
        if self._items:
            self.item = random.choice(self._items)

    def add(self):
        self._items.append(self.item)
        self.listbox.insert('end', self.item)

if __name__ == '__main__':
    root = Tk()
    hl = HelloWorld(root)
    hl.pack()
    root.mainloop()