from tkinter import *
from peewee import *
from database.db_conection import Student
from tkinter.messagebox import *
from tkinter import ttk
import re


def notification(fn):
    def wrapper(*args):
        try:
            print(f"""
              Precessing: {fn}
              """)
            fn(*args)
            print("Process finished successfully.")

        except Exception as e:
            print(e)

    return wrapper


class Screen():

    """
    Updating main screen once adding a new student.

    """

    def update_screen(self, data):
        try:
            self.data = data
            self.students_details = self.data.get_children()
            for i in self.students_details:
                self.data.delete(i)

            self.info = Student.select()
            for x in self.info:
                self.data.insert('', "end", text=x, values=(
                    x.Name, x.LastName, x.Age))
        except Exception as e:
            print(e)


class Controller(Screen):

    """
    Adding a new student.

    """
    @notification
    def create(self, Name, LastName, Age, tree, nameEntry, lastNameEntry, ageEntry):
        try:
            self.nameEntry = nameEntry
            self.lastNameEntry = lastNameEntry
            self.ageEntry = ageEntry
            self.Name = Name
            self.LastName = LastName
            self.Age = Age
            self.patron = "[a-zA-Z]*$"
            if (re.match(self.patron, self.Name)):
                if (len(self.Name) != 0 and len(self.LastName) != 0 and self.Age >= 0):
                    try:
                        self.student = Student(
                            Name=Name,
                            LastName=LastName,
                            Age=Age
                        )

                        self.student.save()
                        self.nameEntry.delete(0, "end")
                        self.lastNameEntry.delete(0, "end")
                        self.ageEntry.delete(0, "end")
                        self.update_screen(tree)
                    except:
                        print("Could not save Data.")
                else:
                    showerror(title="Error",
                              message="All inputs must be completed.")
            else:
                showerror(title="Error", message="Name must be letters only.")
        except Exception as e:
            print(e)

    """
    Updating student.
    
    """
    @notification
    def update(self, id, Name, LastName, Age, tree, update_window):
        try:
            self.id = id
            self.Name = Name
            self.LastName = LastName
            self.Age = Age
            self.tree = tree
            self.update_window = update_window
            self.selected_student = tree.selection()
            self.student = tree.item(self.selected_student)
            self.student_id = self.student["text"]

            if (self.id != 0 and self.Name != "" and self.LastName != "" and self.Age >= 0):
                self.updated_student = Student.update(Name=self.Name, LastName=self.LastName, Age=self.Age).where(
                    self.id == self.student_id).execute()
                self.update_screen(tree)
                self.update_window.destroy()
                showinfo(title="Success", message="Student updated.")
            else:
                showerror(title="Error",
                          message="All inputs must be completed.")
        except Exception as e:
            print(e)

    """
    Deleting a student.
    
    """
    @notification
    def delete(self, tree):
        try:
            self.tree = tree
            self.selected_student = tree.selection()
            self.student = tree.item(self.selected_student)
            self.student_id = self.student["text"]

            if (self.student_id != ""):
                self.deleted_student = Student.get(
                    Student.id == self.student_id)
                self.deleted_student.delete_instance()

                self.update_screen(tree)
            else:
                showerror(title="Error", message="Must be student selected.")

        except Exception as e:
            print(e)

        """
        Pop up for a DECORATOR IN CONSOLE.
        
        """


class Window(Controller):
    def update_screen_details(self, root, tree):
        """
        Pop up for a new window when Update Student button is clicked.

        """
        try:
            self.root = root
            self.tree = tree

            self.update_window = Toplevel(self.root)
            self.update_window.title("Update Student")
            self.update_window.geometry("420x150")

            title = Label(self.update_window, text="Update",
                          bg="green", fg="white", height=1, width=60)
            title.grid(row=0, column=0, columnspan=4,
                       padx=1, pady=1, sticky=W+E)

            self.id = Label(self.update_window, text="Student ID to Update")
            self.id.grid(row=1, column=0, sticky=W)
            self.name = Label(self.update_window, text="Name:")
            self.name.grid(row=2, column=0, sticky=W)
            self.lastName = Label(self.update_window, text="Last Name:")
            self.lastName.grid(row=3, column=0, sticky=W)
            self.age = Label(self.update_window, text="Age:")
            self.age.grid(row=4, column=0, sticky=W)

            self.idValue, self.nameValue, self.lastNameValue, self.ageValue = IntVar(
            ), StringVar(), StringVar(), IntVar()
            self.entryLarge = 20

            self.idEntry = Entry(
                self.update_window, textvariable=self.idValue, width=self.entryLarge)
            self.idEntry.grid(row=1, column=1)
            self.nameEntry = Entry(
                self.update_window, textvariable=self.nameValue, width=self.entryLarge)
            self.nameEntry.grid(row=2, column=1)
            self.lastNameEntry = Entry(
                self.update_window, textvariable=self.lastNameValue, width=self.entryLarge)
            self.lastNameEntry.grid(row=3, column=1)
            self.age = Entry(self.update_window,
                             textvariable=self.ageValue, width=self.entryLarge)
            self.age.grid(row=4, column=1)

            btn_update = Button(self.update_window, text="Update Student", bg="brown", fg="white", command=lambda: self.update(
                self.idValue.get(), self.nameValue.get(), self.lastNameValue.get(), self.ageValue.get(), self.tree, self.update_window))
            btn_update.grid(row=13, column=1)

        except Exception as e:
            print(e)

    def search_screen(self, root):
        """
        Pop up for a new window when Search Student button is clicked.

        """
        try:
            self.root = root
            self.nameValue, self.lastNameValue, self.ageValue = StringVar(), StringVar(), IntVar()
            self.idValue = IntVar()

            self.entryLarge = 20
            self.search_window = Toplevel(self.root)
            self.search_window.title("Search Movie")
            self.search_window.geometry("420x150")

            title = Label(self.search_window, text="Search",
                          bg="green", fg="white", height=1, width=60)
            title.grid(row=0, column=0, columnspan=4,
                       padx=1, pady=1, sticky=W+E)

            self.id = Label(self.search_window, text="Search Student by ID: ")
            self.id.grid(row=1, column=0, sticky=W)

            self.name = Label(self.search_window, text="Name:")
            self.name.grid(row=2, column=0, sticky=W)
            self.lastName = Label(self.search_window, text="Last Name:")
            self.lastName.grid(row=3, column=0, sticky=W)
            self.age = Label(self.search_window, text="Age:")
            self.age.grid(row=4, column=0, sticky=W)

            self.idEntry = Entry(
                self.search_window, textvariable=self.idValue, width=self.entryLarge)
            self.idEntry.grid(row=1, column=1, sticky=W)
            self.nameEntry = Entry(
                self.search_window, textvariable=self.nameValue, width=self.entryLarge)
            self.nameEntry.grid(row=2, column=1, sticky=W)
            self.lastNameEntry = Entry(
                self.search_window, textvariable=self.lastNameValue, width=self.entryLarge)
            self.lastNameEntry.grid(row=3, column=1, sticky=W)
            self.age = Entry(self.search_window,
                             textvariable=self.ageValue, width=self.entryLarge)
            self.age.grid(row=4, column=1, sticky=W)

            self.btn_search = Button(self.search_window, text="Search Student", bg="orange",
                                     fg="white", command=lambda: self.update_search_screen(self.idValue.get()))
            self.btn_search.grid(row=13, column=1, sticky=W)

        except Exception as e:
            print(e)

    def update_search_screen(self, id):
        """
        Returning data in screen when Student was found by ID.

        """
        try:
            self.id = id
            self.found_student = Student.select().where(Student.id == self.id)
            if (self.found_student):
                for i in self.found_student:
                    self.nameValue.set(i.Name)
                    self.lastNameValue.set(i.LastName)
                    self.ageValue.set(i.Age)
                showinfo(title="Success", message=("Student found."))
            else:
                showerror(title="Error", message="No Student found.")

        except Exception as e:
            print(e)
