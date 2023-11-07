import tkinter as tk  #importing inbuilt library from python
import pymysql  #importing inbuilt library from python
import os   #importing inbuilt library from python
import sys   #importing inbuilt library from python
def login(): #user defined function for login into database
    conn=pymysql.connect(host="localhost",user="root",password="Root@1234",database="employee_management")
    cur=conn.cursor()
    u=euid.get()
    p=epass.get()
    q="select * from login where userid='" + u + "' and password='" + p + "'"
    cur.execute(q)
    records=cur.fetchall()
    for row in records:
        os.system('python mainpage.py')
        break
    else:
        print("no data found")
    conn.close()
window=tk.Tk()  #to create window
window.title("Login form")  #providing title
window.geometry("500x300")  #providing size
luid=tk.Label(window,text="User Id :") #creating label
luid.place(x=100,y=50) #placing the label
euid=tk.Entry(window) #creating entry
euid.place(x=200,y=50) #placing the entry
lpass=tk.Label(window,text="Password :") #creating label
lpass.place(x=100,y=80)  #placing the label
epass=tk.Entry(window,show="*") #creating entry
epass.place(x=200,y=80)   #placing the entry
lb=tk.Button(window,text="Login",command=login) #creating button
lb.place(x=220,y=120) #placing the button
window.mainloop() #to hold the window screen
