import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create Table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT Values("Jaswanth","AI","A")''')
cursor.execute('''Insert Into STUDENT Values("Jessi","Machine Learning","B")''')
cursor.execute('''Insert Into STUDENT Values("Mannem","GenAI","A")''')
cursor.execute('''Insert Into STUDENT Values("Jashu","AI/ML Ops","c")''')
cursor.execute('''Insert Into STUDENT Values("Jersy","Deep Learning","B")''')


print("Inserted Records are ....")

data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()