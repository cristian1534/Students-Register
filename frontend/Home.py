from tkinter import *
from tkinter import ttk
from controllers.controllers import Screen
from controllers.controllers import Controller
from controllers.controllers import Window

"""
Main Screen

"""

screen = Screen()
controller = Controller()
window = Window()

root = Tk()
root.geometry("420x380")
root.title("Students Control")

title = Label(root, text="CRUD -Students-", bg="green",
              fg="white", height=1, width=60)
title.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

name = Label(root, text="Name:")
name.grid(row=1, column=0, sticky=W)
lastName = Label(root, text="Last Name:")
lastName.grid(row=2, column=0, sticky=W)
age = Label(root, text="Age:")
age.grid(row=3, column=0, sticky=W)

nameValue, lastNameValue, ageValue = StringVar(), StringVar(), IntVar()
entryLarge = 20

nameEntry = Entry(root, textvariable=nameValue, width=entryLarge)
nameEntry.grid(row=1, column=1)
lastNameEntry = Entry(root, textvariable=lastNameValue, width=entryLarge)
lastNameEntry.grid(row=2, column=1)
ageEntry = Entry(root, textvariable=ageValue, width=entryLarge)
ageEntry.grid(row=3, column=1)

# --------------
# TREEVIEW
# ---------------


tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3")
tree.column("#0", width=70, minwidth=50, anchor=W)
tree.column("col1", width=100, minwidth=50)
tree.column("col2", width=100, minwidth=50)
tree.column("col3", width=100, minwidth=50)
tree.heading("#0", text="Id")
tree.heading("col1", text="Name")
tree.heading("col2", text="Last Name")
tree.heading("col3", text="Age")
tree.grid(row=10, column=0, columnspan=4)

screen.update_screen(tree)

btn_insert = Button(root, text="Add Student", bg="green", fg="white", command=lambda: controller.create(
    nameValue.get(), lastNameValue.get(), ageValue.get(), tree, nameEntry, lastNameEntry, ageEntry))
btn_insert.grid(row=13, column=0)

btn_delete = Button(root, text="Delete Student", bg="red",
                    fg="white", command=lambda: controller.delete(tree))
btn_delete.grid(row=13, column=1)

btn_update = Button(root, text="Update Student", bg="brown", fg="white",
                    command=lambda: window.update_screen_details(root, tree))
btn_update.grid(row=13, column=2)

btn_search = Button(root, text="Search Student", bg="orange",
                    fg="white", command=lambda: window.search_screen(root))
btn_search.grid(row=15, column=1)
