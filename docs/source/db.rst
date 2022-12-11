DataBase
========

DB Conection:
------------

CONECTION WITH PEEWEE:

.. code-block:: 


"""
Connection to database and creation of table

"""

db = SqliteDatabase('Students.db')


class Student(Model):
    Name = CharField()
    LastName = CharField()
    Age = IntegerField()

    class Meta():
        database = db

    def student_db_connection():
        try:
            db.create_tables([Student])
            if not db.is_closed():
                db.close()
        except Exception as e:
            print(e)
