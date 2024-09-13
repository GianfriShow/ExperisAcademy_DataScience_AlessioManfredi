# using SQL, create a student database in which the user can insert/update/delete students/votes/means or just view the database

import mysql.connector

def create_student_database():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root'
    )
    mycursor = mydb.cursor()
    sql = """create database student_db"""
    mycursor.execute(sql)

def create_student_table():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'student_db'
    )
    mycursor = mydb.cursor()
    sql = """create table if not exists students (id int auto_increment primary key, name varchar(255), surname varchar(255), maths float, physics float, chemistry float, average float default null)"""
    mycursor.execute(sql)

def insert_student(student_tuple):  # 'val' must be a tuple for ONE student with (name,surname,maths,physics,chemistry)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "student_db"
    )
    mycursor = mydb.cursor()
    sql = """insert into students (name,surname,maths,physics,chemistry) values (%s,%s,%s,%s,%s)"""
    mycursor.execute(sql,student_tuple)
    mydb.commit()
    sql = """update students set average = (maths+physics+chemistry)/3 where id = %s"""
    mycursor.execute(sql,(mycursor.lastrowid,))
    mydb.commit()

def update_student(student_tuple):  # 'student_tuple' must be a tuple for ONE student with (id,name,surname,maths,physics,chemistry)
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "student_db"
        )
    mycursor = mydb.cursor()
    sql = """update students set name = %s, surname = %s, maths = %s, physics = %s, chemistry = %s where id = %s"""
    modified_tuple = student_tuple[1:] + (student_tuple[0],)
    mycursor.execute(sql,modified_tuple)
    mydb.commit()
    sql = """update students set average = (maths+physics+chemistry)/3 where id = %s"""
    mycursor.execute(sql,(student_tuple[0],))
    mydb.commit()

def delete_student(id):  # 'id' must be the id of the ONE student we wish to eliminate from the database
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "student_db"
        )
    mycursor = mydb.cursor()
    sql = """delete from students where id = %s"""
    mycursor.execute(sql,(id,))
    mydb.commit()










### TO BE CLEANED AND CONTINUED ###





def view_students(ids = 0):  # 'ids' must be a list of the ids of the students we want to view (0 by default if we want to see them all)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "student_db"
    )
    mycursor = mydb.cursor()
    if ids == 0:
        sql = """select * from students"""
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    else:





# FINAL BIG FUNCTION
def student_management():  # add parameters (False by default) for the option we choose
    # check one and only one option was chosen (sum of parameters == 1)
    # create_table already checks for existence, so always run it
    # loop over list of students to insert/update/delete








# EXTRA: divide the system into administrator and normal user
# the administrator can do anything, the users can only view or insert new students

def create_user_table():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'student_db'
    )
    mycursor = mydb.cursor()
    sql = """create table users (id int auto_increment primary key, username varchar(255) not null unique, password varchar(255) not null, admin boolean default 0)"""
    mycursor.execute(sql)






def insert_user_for_admin(user_tuple):  # ONE user at a time with (username,password,admin)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "student_db"
    )
    mycursor = mydb.cursor()
    sql = """insert into users (username,password,admin) values (%s,%s,%s)"""
    mycursor.execute(sql,user_tuple)
    mydb.commit()

def insert_user_for_user(user_tuple):  # ONE user at a time with (username,password)
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "student_db"
    )
    mycursor = mydb.cursor()
    sql = """insert into users (username,password) values (%s,%s)"""
    mycursor.execute(sql,user_tuple)
    mydb.commit()
