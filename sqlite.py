#import the sqlite  library
import sqlite3

#connect to sqlite
connection=sqlite3.connect("student.db")

#create a cursor object to insert record, create table, retrieve data
cursor = connection.cursor()

#create the table
table_info = """
Create table STUDENT_INFO(NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

#Insert some  more records
cursor.execute('''Insert Into STUDENT_INFO values('Kiran','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT_INFO values('VishnuPriya','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT_INFO values('Ramu','Data Science','B',90)''')
cursor.execute('''Insert Into STUDENT_INFO values('Raju','DEVOPS','c',80)''')
cursor.execute('''Insert Into STUDENT_INFO values('sindhu','DEVOPS','B',60)''')


#Display all the records
print("The inserted records are:")

data = cursor.execute('''Select *From STUDENT_INFO''')
for row in data:
    print(row)


#Close the connection
connection.commit()
connection.close()