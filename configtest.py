#!/usr/bin/python3
import os
import configparser
from tkinter import *
from Crypto.Cipher import AES

#Functions

def raise_frame(frame):
    frame.tkraise()

def addNewUser():

    new_username=new_user[0].get()
    new_userPin=new_user[1].get()
    key = AES.new(new_userPin*4, AES.MODE_CFB, new_userPin*4)
    en_userPin=key.encrypt(new_userPin)
    en_userPin=str(en_userPin)
    config=configparser.ConfigParser()

    configfile_name="config-"+new_username+".ini"

    if not os.path.isfile(configfile_name):
        cfgfile=open(configfile_name,'w+')

        #Adding data

        config.add_section(new_username)
        config.set(new_username,"Pin",en_userPin)

        config.write(cfgfile)
        cfgfile.close()

def login():
    logUserName=log_user[0].get()
    logUserPin=log_user[1].get()
    key = AES.new(logUserPin*4, AES.MODE_CFB, logUserPin*4)
    en_userPin=key.encrypt(logUserPin)
    en_userPin=str(en_userPin)
    config=configparser.ConfigParser()

    configfile_name="config-"+logUserName+".ini"
    if os.path.isfile(configfile_name):
        cfgfile=config.read(configfile_name)
        checkPin=config.get(logUserName,'Pin')
        if checkPin==en_userPin:
            
            raise_frame(mainFrame)
            
        else:
            Label(loginFrame,text="Wrong pin").grid(row=4,column=0)




#Tkinter Setup
root=Tk()
root.wm_title("Password Manager")
root.geometry('300x300')

#Frames

welcomeFrame=Frame(root)
signUpFrame=Frame(root)
loginFrame=Frame(root)
mainFrame=Frame(root)

for frame in (welcomeFrame,signUpFrame,loginFrame,mainFrame):
    frame.grid(row=0,column=0,sticky='news')

#Welcome Frame
Label(welcomeFrame,text="Welcome to Password Manager").grid(row=0,column=0)
addUserBtn=Button(welcomeFrame, text="ADD USER", command=lambda:raise_frame(signUpFrame)).grid(row=1,column=0)
loginBtn=Button(welcomeFrame, text="Log In", command=lambda: raise_frame(loginFrame)).grid(row=2,column=0)

#Signup Frame
new_user=[]

for i in range(2):
    var=StringVar()
    entry=Entry(signUpFrame, textvariable=var).grid(row=i,column=1)
    new_user.append(var)


addUserBtn=Button(signUpFrame, text="ADD USER", command=addNewUser).grid(row=2,column=1)

#Login Frame
log_user=[]
for i in range(2):
    logVar=StringVar()
    entry=Entry(loginFrame, textvariable=logVar).grid(row=i,column=1)
    log_user.append(logVar)

checkUserBtn=Button(loginFrame,text="Log In", command=login).grid(row=2,column=1)

#main Frame

Label(mainFrame,text="Logged In").grid(row=0,column=0)

raise_frame(welcomeFrame)
root.mainloop()