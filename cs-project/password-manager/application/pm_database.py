import sqlite3
from sqlite3 import Cursor
from werkzeug.security import check_password_hash, generate_password_hash


def connect_database():
    cursor = None
    try:
        connector = sqlite3.connect("password_manager.db")
        cursor = connector.cursor()
        assert_database(cursor)
    except Exception as e:
        print("connect database error")
        print(e)
    return cursor


def create_user_table(cursor: Cursor) -> bool:
    try:
        cursor.execute(
            "create table if not exists user(username varchar(60), email varchar(100), password varchar(100));")
        return True
    except Exception as e:
        print("create user table error")
        print(e)

    return True


def create_password_table(cursor: Cursor) -> bool:
    try:
        cursor.execute(
            "CREATE TABLE if not exists password(email varchar(60), website_username varchar(100), website_url varchar(100), website_password varchar(100));")
        return True
    except Exception as e:
        print("create password table error")
        print(e)

    return True


def assert_database(cursor: Cursor) -> bool:
    try:
        if not create_user_table(cursor):
            return False
        if not create_password_table(cursor):
            return False
        return True
    except Exception as e:
        print("assert database failed")
        print(e)
    return False


def insert_user(cursor: Cursor, username: str, email: str, password: str) -> bool:
    hashed_password = generate_password_hash(password)
    try:
        if not assert_email(cursor, username):
            cursor.execute(
                "INSERT INTO user VALUES(?, ?, ?);", (username, email, hashed_password))
            cursor.connection.commit()
            return True
        else:
            return False
    except Exception as e:
        print("insert user error")
        print(e)
    return False


def insert_password_entry(cursor: Cursor, email: str, website_username: str, website_url: str,
                          website_password: str) -> bool:
    try:
        cursor.execute(
            "INSERT INTO password VALUES(?, ?, ?, ?);",
            (email, website_username, website_url, website_password))
        cursor.connection.commit()
        return True
    except Exception as e:
        print("insert password entry error")
        print(e)
    return False


def update_user(cursor: Cursor, username: str, email: str, password: str) -> bool:
    try:
        cursor.execute(
            'UPDATE user SET username = ?,password = ? WHERE email = ?;', (username, password, email))
        if cursor.rowcount > 0:
            cursor.connection.commit()
            return True
    except Exception as e:
        print("update user error")
        print(e)
    return False


def update_password_entry(cursor: Cursor, email: str, website_username: str, website_url: str,
                          website_password: str) -> bool:
    try:
        cursor.execute(
            'UPDATE passsword SET website_username = ?,website_url = ?, website_password = ? WHERE email = ?;',
            (website_username, website_url, website_password, email))
        if cursor.rowcount > 0:
            cursor.connection.commit()
            return True
    except Exception as e:
        print("update password entry error")
        print(e)
    return False


def authenticate_email(cursor: Cursor, email: str, password: str) -> bool:
    # hashed_password = generate_password_hash(password)
    try:
        result = cursor.execute(
            'SELECT password FROM user WHERE email = ?;', (email,)).fetchall()
        if check_password_hash(result[0][0], password):
            return True
    except Exception as e:
        print("authentication error")
        print(e)
    return False


def assert_email(cursor: Cursor, email: str) -> bool:
    try:
        result = cursor.execute(
            'SELECT COUNT(email) FROM user WHERE email = ?;', (email,)).fetchall()
        if result[0][0]:
            return True
    except Exception as e:
        print("assert email error")
        print(e)
    return False


def fetch_password_entry(cursor: Cursor, email: str) -> list or None:
    try:
        result = cursor.execute(
            'SELECT * FROM password WHERE email = ?;', (email,)).fetchall()
        return list(result)
    except Exception as e:
        print("fetch password error")
        print(e)
    return None


def fetch_user_entry(cursor: Cursor, email: str) -> list or None:
    try:
        result = cursor.execute(
            'SELECT * FROM user WHERE email = ?;', (email,)).fetchall()
        return list(result[0])[:-1]
    except Exception as e:
        print("fetch password error")
        print(e)
    return None
# cursor = connect_database()
# assert_database(cursor)
#
# #insert_user(cursor, "jack", "jack@gmail.", "hlo")
#
# # insert_password_entry(cursor, "kavin", "facebook", "facebook.com", "helloworld")
# fetch_password_entry(cursor, "jack")
#
# if authenticate_user(cursor, "jack", "hlo"):
#     print("authentication verified")
# else:
#     print("not verified")
#
# update_user(cursor, "jack", "jack@1", "heloooo")
