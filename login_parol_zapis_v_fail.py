import string
import keyboard
import sys
import random


Symbols='.,:;!_*-+()/#¤%&'
usernames={}
status=''
choose=''




def menu():
    status=input("Are you registered user (y/n)? Press q to quite.")
    if status=="y":
        oldUser()
    elif status=="n":
        newUser()
    elif status=="q":
        sys.exit()

def self():
    choose=input("Choose 1-self registration, 2-automatic registration")

    if choose=='1':
        new_name_password(usernames)

    elif choose=='2':
        create_login=input("Repeat your new username ")
        if create_login=='':
            print("Do not leave field blank")
        elif not create_login.isalpha():
            print("Only alphabetical letters allowed.")
        else:
            print(f"Your username is: {create_login}")
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0+str1+str2+str3
        print(str4)
        ls = list(str4)
        print(ls)
        random.shuffle(ls)
        print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([random.choice(ls) for x in range(12)])
        # Пароль готов
        print(f"Your password is: {psword}")
        usernames[create_login]=psword
        saveFile = open('text.txt', 'w')
        saveFile.write(create_login+":"+psword+"\n")
        saveFile.close()
        print("\nUser created.\n")



def new_name_password(usernames):
    create_login=input("Repeat you username ")
    if create_login=='':
        print("Do not leave field blank")
    elif create_login.isalpha():
        print(f"Your username is: {create_login}")
    else:
        print("\nThe username already exist or check tieped name, only alphabetical letters allowed.\n")
    create_passw=str(input("Create your password\nHas contain at least 1 small letter, 1  big letter, number and symbol--> "))
    if create_passw=='':
        print("Do not leave field blank")
    if len(create_passw)==4 and create_passw.isalnum():
        print("length is 4")
    elif create_passw.isalnum():
        res= [ele for ele in Symbols if(ele in create_passw)]
        print("The password-string contains symbols: " + str(bool(res)))

        if bool(res)==True:
            print(f"Your password is {create_passw}")
        elif bool(res)==False:
            print("you entered an invalid password")
            #sys.exit()
            self()
    else:

        usernames[create_login]=create_passw
        saveFile = open('text.txt', 'w')
        saveFile.write(create_login+":"+create_passw+"\n")
        saveFile.close()
        print("\nUser created.\n")
            #self()







def newUser():
    create_login=input("Write you username ")
    if create_login in usernames:
        print("\nThe username already exist\n")
    else:
       self()

def oldUser():
    login=input("Enter login name: ")
    passwd=input("Enter password: ")
    f=open('text.txt','r')
    if login in f and usernames[login] in f:
    #if login in usernames and usernames[login]==passwd:
        print("\nLogin successful!\n")
    else:
        print("\nThe user does not exist or wrong password\n")


while status!="q":
    menu()
