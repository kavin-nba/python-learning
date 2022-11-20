import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="kavin232005")
db = conn.cursor()
lst = db.fetchall()


def assert_database():
    database_name = input("enter name of database:")
    if (database_name,) in lst:
        print("database exists")
    else:
        db.execute("create database {}".format(database_name))
        print("database created")


assert_database()
