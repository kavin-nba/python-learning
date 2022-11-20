import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
# create the salesman table
#cursor.execute("CREATE TABLE user_info(name_app varchar(60), username varchar(60), password varchar(60));")
check = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name='user_info';").fetchall()
print(check)
s_name = input('Name of the app:')
s_username = input('Username:')
s_passwd = input('Password:')
cursor.execute("""
INSERT INTO user_info(name_app, username, password)
VALUES (?,?,?)
""", (s_name, s_username, s_passwd))
conn.commit()
print('Data entered successfully.')
conn.close()
if (conn):
    conn.close()
    print("\nThe SQLite connection is closed.")
