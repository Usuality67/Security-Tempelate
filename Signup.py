import Encrypt
import Info_enter

def Mail_Checker(Email):
    if len(Email) > 320 or "@" not in Email or " " in Email or len(Email.split("@")) > 2:
        return -1
    return 0
def Username_Checker(Usernh):

    if " " in Usernh or len(Usernh) == 0:
        return -1
    return 0



def Signup():
    print("Hello welcome to the financial manager, enter your desired unique email and username below,without spaces: ")
    Email = input("Email: ")

    Code = Info_enter.check_details_mail(Email)
    Status = Mail_Checker(Email)
    while Code == 2 or Status == -1:
        print("Enter a unique and correct Email address!")
        Email = input("Email: ")
        Code = Info_enter.check_details_mail(Email)
        Status = Mail_Checker(Email)

    Username = input("Username: ")

    Status = Username_Checker(Username)
    Code = Info_enter.check_details_User(Username)
    while Status == -1 or Code == 1:
        print("Enter a correct and/or unique username!")
        Username = input("Username: ")
        Status = Username_Checker(Username)
        Code = Info_enter.check_details_User(Username)




    print("Enter your new password below",end="")
    print(", it should be at least 8 characters long, without any spaces.")
    Password = input("Password: ")

    while " " in Password:
        print("Password should be without spaces!")
        Password = input("Password: ")
    while len(Password) < 8 :
        print("Password should be 8 characters long!")
        Password = input("Password: ")
    Password = Encrypt.Encrypt(Password)

    pin = input("Enter your four digit pin: ")
    while len(pin) != 4:
        print("The pin should be 4 digits long!")
        pin = input("Pin: ")
    while not pin.isdigit():
        print("The pin should only contain digits!")
        pin = input("Pin: ")

    Info_enter.enter_details(Username,Password,Email,pin)

    print("Sign-up successful , welcome to the Smirk Bank 😏!")

Signup()
