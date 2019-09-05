#!/usr/bin/python3

#Importing GUI library Tkinter
import tkinter as ttk 
#Importing MySQL Lib
import mysql.connector as mysql

#Connecting to Database
db=mysql.connect(host="localhost",user="#MYSQLUSER",password="#MYSQLPASS",database="#MYSQLDATABASE")

#Creating Cursor object to take actions through script
cursor=db.cursor()

pin=input("Please enter the Pin to ENTER: ")

while pin == "7580":
    option=input("""Would you like to ADD or FETCH?
                    ADD = 1 
                    FETCH = 2
                    quit=Q: """)
    if option == '1':
        nickname=input("Enter a nickname for this save: ")
        email=input("Enter your email: ")
        pwd=input("Enter your password: ")
    elif option=='2':
        nick=input("Enter the nickname: ")
    elif option=="Q" or "q":
        break
    else: 
        print("You have selected wrong option!")

def commandExe(command):
    cursor.execute(command)


def manager():
    while pin == "7580":
        option=input("""\nWould you like to ADD or FETCH?
                        ADD = 1 
                        FETCH = 2
                        quit=Q: """)
        if option == '1':
            nickname=input("Enter a nickname for this save: ")
            usrname=input("Enter username for this save: ")
            email=input("Enter your email: ")
            pwd=input("Enter your password: ")
            add="INSERT INTO users(NICKNAME,USERNAME,EMAIL,PASS) VALUES ('%s','%s','%s','%s')"%(nickname,usrname,email,pwd)
            commandExe(add)
            db.commit()
            continue
        elif option=='2':
            output=cursor.fetchall()
            print ("Select your Nickname ID: \n")
            for x in output:
                print (x[0], ":" ,x[2])
            fetchID=int(input("\n ENTER ID: ") )  

            print ("""\nThis is your USERNAME: {}
This is your EMAIL: {}
This is your PASSWORD: {}  """.format( output[fetchID-1][1],output[fetchID-1][3],output[fetchID-1][4] ))         
        elif option=="Q" or "q":
            break
        else: 
            print("You have selected wrong option!")

#Fetching all data from DB
fetch="SELECT * FROM users"
commandExe(fetch)

manager()

db.close()