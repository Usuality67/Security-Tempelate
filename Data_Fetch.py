import sqlite3
def Catch_Usernames():
    stat1 = """SELECT Username FROM INFORMATION;"""
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(stat1)
        Data = cursor.fetchall()
        return Data
def Catch_Mail():
    stat1 = """SELECT Emails FROM INFORMATION
            ORDER BY Username ASC;"""
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(stat1)
        Data = cursor.fetchall()
        return Data
def Catch_Passwords():
    stat1 = """SELECT Passwords FROM INFORMATION
               ORDER BY Username ASC;"""
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(stat1)
        Data = cursor.fetchall()
        return Data
def Catch_Pins():
    stat1 = """SELECT Pins FROM INFORMATION;"""
    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(stat1)
        Data = cursor.fetchall()
        return Data
print(Catch_Passwords())
print(Catch_Usernames())