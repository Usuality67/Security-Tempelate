The following repo represents a security system that can be used for e.g banking apps, and other applications. 

The Database used here is made through "sqllite3", and is named "Usernames_Password.db", not a really creative name but it works.

The Database has a table called INFORMATION, which stores the following columns: Usernames,Passwords (Encrypted), Emails,and Pins.

Usernames,Passwords,and Emails all have the data type "VARCHAR(255)", and pins is "CHAR(4)". 

You can find the statement commented in the "DB_tester" file.

The "Info_enter" file is called by the "Signup" function/file when the user first make contact with this program, it then takes the username as input, and verify if its: 
     1. Correctly formatted 
     2. Is unique
     
 The program check for uniqueness by calling the function "check_details_User(Userh)" which is in the info_enter file. Similarly it checks for the uniqueness of an email by using the "check_details_mail(mail)", also in the Info_enter file.
 
 It then verifies the format for password, and encrypts it using an enchanced CSEAR-13 encrption module which encrypts letters,numbers, and symbols. 
 
 It then verifies that pins is indeed four characters long . 
 
 Then push them onto the table INFORMATION.  
 
 Now, at the "Login" file, the user is asked to enter username , and password. The Usernames,and passwords are then extracted from the table arranged in the order with respect to the username, in form of a list-tuple i.e [(Username,)] etc. 
 
 Then the password from the table,which is encrypted, is decrypted through the Decryption function from the "Decrypt" file . After that usernames, and passwords are compared with the ones stored in the database, if they match the login is succesful,and 0 is passed if not then 1 is passed as failure code.
 
 This is the small description of the program,hope its useful.
 
 
 
 
 