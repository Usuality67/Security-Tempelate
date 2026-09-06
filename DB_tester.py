import sqlite3

# statement = ("CREATE TABLE INFORMATION ("
#              "Username varchar(255) PRIMARY KEY,"
#              "Passwords varchar(255) NOT NULL,"
#              "Emails varchar(255) NOT NULL,"
#              "Pins CHAR(4) NOT NULL,"
#              "UNIQUE (Emails)"
#              ");"
#
#
#)

def email_delete(Email):
    statement = """DELETE FROM INFORMATION WHERE Emails = ?;"""
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(statement,(Email,))
        conn.commit()

def User_delete(Usernh):
    statement = """DELETE FROM INFORMATION WHERE Username = ?;"""
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(statement,(Usernh,))
        conn.commit()
def __D__elete_all():
    statement1 = "DELETE FROM INFORMATION;"
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(statement1)
        conn.commit()

def Edit():
    statement = """ALTER TABLE INFORMATION
                DROP COLUMN created_time;"""
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()


def Show_Table():

    statement1 = "SELECT * FROM INFORMATION;"
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(statement1)
        Data = cursor.fetchall()
        return Data
print(Show_Table())
Edit()
print(Show_Table())