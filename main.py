from database.db_conection import Student
from frontend.Home import root

"""
Running the frontend and the connection to database

"""
student = Student()



if __name__ == "__main__":
    db = Student.student_db_connection()
    root.mainloop()
