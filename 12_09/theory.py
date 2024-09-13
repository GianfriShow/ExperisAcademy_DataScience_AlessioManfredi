a,b = 10,'hello'

try:
    print(a/b)
    print("Code successfully executed")
except ZeroDivisionError as e:
    print(f'Error: {e}')
except TypeError as e:
    print(f'Error: {e}')
except:  # any other unaccounted error type if we don't specify it
    print('Unknown error')


# with open('test.txt','r') as my_file:  # if the file we try to open doesn't exist, we'll raise a FileNotFoundError
#     content = my_file.read()

def read_file(file_path):
    with open(file_path,'r') as my_file:
        content = my_file.read()
        return content  # in this case, return is inside the with statement, since as soon as we close it 'content' will go away

path = '12_09/test.txt'
print(read_file(path))

def append_file(file_path,text_to_append):
    with open(file_path,'a') as my_file:
        my_file.write(text_to_append)

addend = '\nHello again!'
append_file(path,addend)
print(read_file(path))


path = '12_09/test.csv'
with open(path,'w') as my_file:
    my_file.write('name,surname,age\nthomas,bellington,21\nrobert,janish,34')

def csv_to_rows(path,separator='\n'):
    return read_file(path).split(separator)

rows = csv_to_rows(path)
print(rows)

def csv_rows_to_lists(rows,variable_names=True):
    return [row.split(',') for row in rows[variable_names:len(rows)]]

print(csv_rows_to_lists(rows,variable_names=True))

new_name = 'alfred'
new_surname = 'green'
new_age = '46'
new_row = f'\n{new_name},{new_surname},{new_age}'

path = '12_09/test.csv'
append_file(path,new_row)
print(read_file(path))
print(csv_rows_to_lists(csv_to_rows(path)))



import pickle  # library for binary content

dictionary = {1:'Thomas',2:"Mark"}
dictionary_binary = pickle.dumps(dictionary)  # transform a dictionary to binary

with open('12_09/binary.bin','wb') as my_file:  # write a binary file
    my_file.write(dictionary_binary)

with open('12_09/binary.bin','rb') as my_file:  # read a binary file
    content = my_file.read()

print(content)  # unreadable because binary
readable_content = pickle.loads(content)  # make it readable
print(readable_content)



class Cat:

    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def __str__(self):  # dunder method (characterized by the '__ __')
        return f'Name: {self.name}, Type: {self.type}'  # every time the object is treated as a string, this will be returned


kitty = Cat('cutie','orange')
print(kitty)  # prints the object info and its location if no __str__ method, otherwise it runs the latter
    


# connect to databases

import mysql.connector

mydb = mysql.connector.connect(  # connect to the database
    host = 'localhost',
    user = 'root',
    password = 'root'
#   port = ....  # in case we change port from the default (3306)
)

print(mydb)

mycursor = mydb.cursor()  # interact with the database through the cursor

sql = 'create database python_exercise'  # prepare sql query
mycursor.execute(sql)  # execute query

sql = 'show databases'
mycursor.execute(sql)

for db in mycursor:  # the cursor is an iterable with the database names
    print(f'Database: {db}')
for tb in mycursor:
    print(f'Table: {tb}')


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'python_exercise'  # this time we specify the database we work in
)
mycursor = mydb.cursor()
sql = 'create table users(id int auto_increment primary key, name varchar(255), surname varchar(255))'
mycursor.execute(sql)

sql = 'insert into users(name,surname) values(%s,%s)'  # '%s' is used to prevent SQL injection and for dynamic values
val = [("Mark","Jones"),("Luke","Stone"),("John","Rovers")]
mycursor.executemany(sql, val)  # if we only have one tuple to add, we use execute() instead

mydb.commit()  # whenever we modify data inside tables/databases, we need to also confirm the query using commit()

print(mycursor.rowcount,"data points uploaded")
print(mycursor.lastrowid)  # show the id of the last row


sql = 'select * from users where id>1'
mycursor.execute(sql)

data = mycursor.fetchall()  # fetchall() retrieves all the output rows of the query, exhausting them from memory
for datum in data:
    print(datum)

sql = 'select * from users where id>1'
mycursor.execute(sql)

datum = mycursor.fetchone()  # if we hadn't rerun the query, we wouldn't have been able to fetch anything (would have returned None)
print(datum)  # fetchone() only returns the first row of the query output
for element in datum:  # therefore, we now extract all variables of the first row only
    print(element)

sql = 'delete from users where id = 1'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount)
