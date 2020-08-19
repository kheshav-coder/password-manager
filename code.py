import sys
import random
import time
import os
import hashlib
import getpass
from playsound import playsound
import mysql.connector
from colorama import Fore, Style

masterpass="22b30fe60a3dd31411aae8a25c35d6c5950cc099b56bf5688dc20cd5165a1933"
alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
special=['!','@','#','$','%','^','&','*','(',')','_','+','-','=','~','[',']','|','?','<','>','/']

def access(p):
    os.system('clear')
    p_=((hashlib.sha256(getpass.getpass(prompt='Please enter the master password>>>', stream=None) .encode())).hexdigest())
    if p==p_:
        return True
    else:
        return False

while True:
    try:
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="kheshav")
        cursor = mydb.cursor()
        cursor.execute("use passwords")
        break
    except:
        os.system('service mysql start')


access_val=5
while True:

    def cont():
        v=input("do you wish to continue(y/n)?:")
        if v=='y':
            time.sleep(1)
        elif v=='n':
            os.system('clear')
            print()
            print(Fore.GREEN+"[+]thankyou for using shadow password manager!!")
            time.sleep(1)
            cursor.close()
            mydb.close()
            exit()

    def string(a):
        a=a+'%'
        a='%'+a
        return a


    if access(masterpass):
        access_val=5
        print(Fore.GREEN+"                                                    _           _ ")
        print(Fore.GREEN+"                                                   | |         | |")
        print(Fore.GREEN+"  __ _  ___ ___ ___ ___ ___    __ _ _ __ __ _ _ __ | |_ ___  __| |")
        print(Fore.GREEN+" / _` |/ __/ __/ _ / __/ __|  / _` | '__/ _` | '_ \| __/ _ \/ _` |")
        print(Fore.GREEN+"| (_| | (_| (_|  __\__ \__ \ | (_| | | | (_| | | | | ||  __| (_| |")
        print(Fore.GREEN+" \__,_|\___\___\___|___|___/  \__, |_|  \__,_|_| |_|\__\___|\__,_|")
        print(Fore.GREEN+"                               __/ |                              ")
        print(Fore.GREEN+"                              |___/                               ")
        print()
        print("[+]initialising your options......")
        playsound('/root/Desktop/my_python/passmanager/accessgranted.wav')





        def display():
            os.system('clear')
            print(Fore.BLUE + "#######################################")
            print(Fore.BLUE + "#                                     #")
            print(Fore.BLUE +"#",Fore.GREEN + " WELCOME TO SHADOW PASSWORD MANAGER",Fore.BLUE + "#")
            print(Fore.BLUE + "#                                     #")
            print(Fore.BLUE + "#######################################")
            print(Fore.RED + "The place where your passwords are SAFE!!!")
            print()



        def choise():
            print()
            print(Fore.YELLOW + "1) Generate a new RANDOM password for you")
            print(Fore.YELLOW + "2) Retrieve a stored password")
            print(Fore.YELLOW + "3) Remove or edit a stored password")
            print(Fore.YELLOW + "4) Add a new password")
            print(Fore.YELLOW + "5) Exit")
            print()
            choise=int(input("enter your option>>>"))


            if choise==1:
                new_pass=""
                for i in range(4):
                    new_pass+=random.choice(alph)+random.choice(alphc)+random.choice(numbers)+random.choice(special)
                print()
                print("your new password >>>",new_pass)
                print()
                o=input("will you use this password?(y/n):")
                if o=='y':
                    d_name=input("please enter the domain name to store this password:")
                    u_name=input("please enter the user name to store the password:")
                    val=[d_name,u_name,new_pass]
                    cursor.execute("insert into passwords values(%s,%s,%s)",val)
                    mydb.commit()
                    print()
                    print(Fore.GREEN+'*'*50)
                    print(Fore.GREEN+"[+]your password is saved successfully!!!")
                    print('*'*50)
                    time.sleep(2)
                    print()
                    cont()
                elif o=='n':
                    print()
                    print("ok,i'll try to create better passwords!!!")
                    time.sleep(2)


            elif choise==2:
                domain=input("please enter the domain name to the stored password:")
                usern=input("please enter the user name to the stored password:")
                val1=[string(domain),string(usern)]

                try:
                    cursor.execute("select password from passwords.passwords where domain like %s and username like %s",val1)
                    for password in cursor:
                        for i in password:
                            new_str=i
                    print()
                    print("your password>>>",Fore.GREEN+new_str)
                    print()
                except:
                    print()
                    print(Fore.RED+"[-]password not found!!!")
                    print()
                cont()


            elif choise==3:
                if access(masterpass):
                    q=input("do you want to remove or edit(r/e):")
                    if q=='r':
                        domainame=input("enter the domain name of stored pass to remove:")
                        username=input("enter the user name of stored pass to remove:")
                        val2=[string(domainame),string(username)]
                        try:
                            cursor.execute("delete from passwords.passwords where domain like %s and username like %s",val2)
                            mydb.commit()
                            print()
                            print(Fore.GREEN+"[+]the password is successfully removed")
                            time.sleep(1)
                        except:
                            print()
                            print(Fore.RED+"[-]error removing the password!!!")
                            time.sleep(1)


                    elif q=='e':
                        domain1=input("enter the domain name of stored pass to edit:")
                        user1=input("enter the user name of stored pass to edit:")
                        print()
                        while True:
                            newpass=getpass.getpass(prompt="enter the new password:" ,stream=None)
                            re_newpass=getpass.getpass(prompt="re-type the new password:" ,stream=None)
                            if newpass==re_newpass:
                                break
                            else:
                                print()
                                print(Fore.RED+"the passwords does not match!!!")
                                time.sleep(1)
                                continue

                        val3=[newpass,string(domain1),string(user1)]
                        try:
                            cursor.execute("update passwords.passwords set password=%s where domain like %s and username like %s",val3)
                            mydb.commit()
                            print()
                            print(Fore.GREEN+"[+]password updated successfully!!!")
                            time.sleep(1)
                        except:
                            print()
                            print(Fore.RED+"[-]error updating the password!!!")
                            time.sleep(1)

                else:
                    print()
                    print(Fore.RED+"INCORRECT PASSWORD!!")
                    playsound('/root/Desktop/my_python/passmanager/beep_error.mp3')
                    time.sleep(1)



            elif choise==4:
                domain2=input("enter the domain name for the password:")
                username2=input("enter the username for the password:")
                print()
                while True:
                    newpass2=getpass.getpass(prompt="enter the password to be stored:" ,stream=None)
                    re_newpass2=getpass.getpass(prompt="re-type the password to be stored:" ,stream=None)
                    if newpass2==re_newpass2:
                        break
                    else:
                        print()
                        print(Fore.RED+"passwords does not match!!!")
                        time.sleep(1)
                        continue

                val4=[domain2,username2,newpass2]
                cursor.execute("insert into passwords.passwords values(%s,%s,%s)",val4)
                mydb.commit()
                print()
                print(Fore.GREEN+"password added successfully!!!")
                print()
                cont()


            elif choise==5:
                os.system('clear')
                print()
                print(Fore.GREEN+"thankyou for using shadow password manager !!!!!")
                time.sleep(2)
                exit()


            elif choise==99:
                if access(masterpass):
                    cursor.execute("select * from passwords")
                    print()
                    print()
                    print(Fore.GREEN+"DOMAIN  |  USERNAME  |  PASSWORD")
                    for row in cursor:
                        d=0
                        print()
                        print()
                        for i in row:
                            d+=1
                            if d==3:
                                print(i)
                            else:
                                print(Fore.WHITE+i,end="   ")

                    print()
                    print()
                    cont()

                else:
                    print()
                    print(Fore.RED+"INCORRECT PASSWORD!!")
                    playsound('/root/Desktop/my_python/passmanager/beep_error.mp3')

        while True:
            display()
            choise()


    else:
        access_val=access_val-1
        print(Fore.RED+"                                  _            _          _ ")
        print(Fore.RED+"                                 | |          (_)        | |")
        print(Fore.RED+"  __ _  ___ ___ ___ ___ ___    __| | ___ _ __  _  ___  __| |")
        print(Fore.RED+" / _` |/ __/ __/ _ / __/ __|  / _` |/ _ | '_ \| |/ _ \/ _` |")
        print(Fore.RED+"| (_| | (_| (_|  __\__ \__ \ | (_| |  __| | | | |  __| (_| |")
        print(Fore.RED+" \__,_|\___\___\___|___|___/  \__,_|\___|_| |_|_|\___|\__,_|")
        print()
        print(Fore.RED+"attempts remaining:",access_val)
        playsound('/root/Desktop/my_python/passmanager/accessdenied.wav')
        if access_val==0:
            print()
            print('#'*60)
            print(Fore.RED+"the entire password database is erased!!!!!!")
            print('#'*60)
            cursor.execute("drop database passwords")
            time.sleep(1)
