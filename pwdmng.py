#!/usr/bin/python3


from tkinter import* 

import mysql.connector as mysql


db=mysql.connect(host="localhost",user="#MYSQLUSER",password="#MYSQLPASS",database="#MYSQLDATABASE")


cursor=db.cursor()

fields=[]
entries=[]
checkPin=[]

def raise_frame(frame):
    frame.tkraise()

def add_DB():
    nickname=entries[0].get()
    username=entries[1].get()
    email=entries[2].get()
    pwd=entries[3].get()
    add="INSERT INTO users(NICKNAME,USERNAME,EMAIL,PASS) VALUES ('%s','%s','%s','%s')"%(nickname,username,email,pwd)
    cursor.execute(add)
    db.commit()
    

root=Tk()
root.wm_title("Password Manager")
root.geometry('300x300')
#FRAMES

entryFrame=Frame(root)
mainFrame=Frame(root)
addFrame=Frame(root)
fetchFrame=Frame(root)
lastFrame=Frame(root)

for frame in (entryFrame,mainFrame,addFrame, fetchFrame,lastFrame):
    frame.grid(row=0, column=0, sticky='news')



def check():
    pinCheck=checkPin[0].get()
    if int(pinCheck)==7580:
        
        mainapp()


def mainapp():
    raise_frame(mainFrame)
    addBtn=Button(mainFrame, text="ADD", command=lambda:raise_frame(addFrame)).pack()
    fetchBtn=Button(mainFrame, text="FETCH", command=lambda: raise_frame(fetchFrame)).pack()

    #ADD FRAME 

    L_nick=Label(addFrame, text="Nick Name").grid(row=0,column=0)
    L_user=Label(addFrame, text="User Name").grid(row=1,column=0)
    L_email=Label(addFrame, text="Email").grid(row=2,column=0)
    L_pass=Label(addFrame, text="Password").grid(row=3,column=0)

    for i in range(4):
        var=StringVar()
        entry=Entry(addFrame, textvariable=var).grid(row=i,column=1)
        entries.append(var)
        fields.append(entry)

    addUserBtn=Button(addFrame, text="Add User", command=add_DB).grid(row=4,column=1)

    #Fetch Frame
    cursor.execute("SELECT * FROM users")
    userData=cursor.fetchall()
    fetchLB=Listbox(fetchFrame,selectmode='single' )

    for nicknames in userData: 
        
        fetchLB.insert(END,nicknames[1])

    def fetch_DB():
        picknick=fetchLB.curselection()
        if len(picknick)>0:
            picknick_text=int(picknick[0])

            lastFrame.tkraise()

            Label(lastFrame, text=userData[picknick_text][2]).grid(row=0,column=1)
            Label(lastFrame, text=userData[picknick_text][3]).grid(row=1,column=1)
            Label(lastFrame, text=userData[picknick_text][4]).grid(row=2,column=1)
    fetchThis=Button(fetchFrame, text="Fetch This",command=fetch_DB)

    fetchData=["Username: ","Email: ","Password: "]

    for field in range(len(fetchData)):
        Label(lastFrame, text=fetchData[field]).grid(row=field,column=0)

    fetchLB.pack()
    fetchThis.pack()

pinVar=StringVar()
pin=Entry(entryFrame,textvariable=pinVar, show="*" ).grid(row=0,column=1)
checkPin.append(pinVar)
entryBtn=Button(entryFrame, text="ENTER", command=check).grid(row=1,column=2)


raise_frame(entryFrame)
root.mainloop()