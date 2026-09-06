import sqlite3
import DB_tester

def enter_details(Usernh,Password,Email,Pins):

    statement = """INSERT INTO INFORMATION (Username,Passwords,Emails,Pins)
                    VALUES(?,?,?,?);"""


    with sqlite3.connect("Usernames_Passwords.db") as conn:
        cursor = conn.cursor()
        cursor.execute(statement,(Usernh,Password,Email,Pins))
        conn.commit()
        return


def check_details_mail(mail):
    statement = """INSERT INTO INFORMATION(Emails)
                  VALUES (?);"""
    try:

        with sqlite3.connect("Usernames_Passwords.db") as conn:
            cursor = conn.cursor()
            cursor.execute(statement, (mail,))
            conn.commit()
            DB_tester.email_delete(mail)
            return 0

    except:
        return 2

def check_details_User(Userh):
    statement = """INSERT INTO INFORMATION(Username)
                  VALUES (?);"""

    try:
        with sqlite3.connect("Usernames_Passwords.db") as conn:
            cursor = conn.cursor()
            cursor.execute(statement, (Userh,))
            conn.commit()
            DB_tester.User_delete(Userh)
            return 0
    except:
        return 1
    #kk_56_lk_90





















