import Decrypt
import Data_Fetch

def Login_account():

    Username = input("Enter your username: ")

    Lister_Users = Data_Fetch.Catch_Usernames()

    Password = input("Enter your password: ")

    Lister_Passwords = Data_Fetch.Catch_Passwords()
    print(Lister_Passwords)
    for x in range(len(Lister_Users)):

        if Lister_Users[x][0] == Username and Decrypt.Decryption((Lister_Passwords[x][0])) == Password:
            return 0
    return 1

print(Login_account())



