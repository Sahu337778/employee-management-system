import tkinter as tk #importing inbuilt library from python
import pymysql   #importing inbuilt library from python
import tkinter.messagebox as mb  #importing inbuilt library from python
import os #importing inbuilt library from python
def adddata(): #user defined function to add new employee data
    conn=pymysql.connect(host="localhost",user="root",password="Root@1234",database="employee_management") #to connect with database conn = user defined object
    cur=conn.cursor()  #inbuilt method cursor()
    q="insert into employee(eid,ename,egender,ecity,edesig,esalary)values("+eid.get()+",'"+en.get()+"','"+gender.get()+"','"+ec.get()+"','"+ed.get()+"',"+es.get()+")" #to run the written query means to get data inserted
    cur.execute(q) #to execute query of 'q' from above line
    conn.commit() #to confirm the action

    eid.delete(0,'end')  #to clear the Entry box
    en.delete(0,'end')   #to clear the Entry box
    ec.delete(0,'end')   #to clear the Entry box 
    ed.delete(0,'end')   #to clear the Entry box
    es.delete(0,'end')   #to clear the Entry box

    eid.focus()

    mb.showinfo("",str(cur.rowcount)+"Record inserted successfully") #to show pop-up message once the new data added
    conn.close()  #to close the connection

def searchdata():  #user defined function to add new employee data
    conn=pymysql.connect(host="localhost",user="root",password="Root@1234",database="employee_management")
    cur=conn.cursor()  #inbuilt method cursor()
    q="select * from employee where eid="+eid.get()+""
    cur.execute(q)
    records=cur.fetchall()

    list1.delete(0,'end')

    for row in records:
        d=str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5])
        n.set(str(row[1]))
        c.set(str(row[3]))
        deg.set(str(row[4]))
        s.set(str(row[5]))
    list1.insert(list1.size()+1,d)
    conn.close()   

def showdata():  #user defined function to show the already added / recorded data in the database
    conn=pymysql.connect(host="localhost",user="root",password="Root@1234",database="employee_management")
    cur=conn.cursor()
    q="select * from employee"
    cur.execute(q)
    records=cur.fetchall()

    list1.delete(0,'end')

    for row in records:
        d=str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5])
        list1.insert(list1.size()+1,d)
    conn.close()
    
def updatedata():  #user defined function to update the existing record
    conn=pymysql.connect(host="localhost",user="root",password="Root@1234",database="employee_management")
    cur=conn.cursor()
    q="update employee set ename='"+en.get()+"',egender='"+gender.get()+"',ecity='"+ec.get()+"',edesig='"+ed.get()+"',esalary="+es.get()+" where eid="+eid.get()+""
    cur.execute(q)
    conn.commit()
    list1.delete(0,'end')
    eid.delete(0,'end')
    en.delete(0,'end')
    ec.delete(0,'end')
    ed.delete(0,'end')
    es.delete(0,'end')
    mb.showinfo("",str(cur.rowcount)+" Record Update Successfully")
    eid.focus()

    conn.close()


def deletedata(): #user defined function to delete record from the data
    conn=pymysql.connect(host="localhost",user="root",password="Root@1234",database="employee_management")
    cur=conn.cursor()
    q="delete from employee where eid="+eid.get()+""
    cur.execute(q)
    conn.commit()
    mb.showinfo("",str(cur.rowcount)+"Record successfully deleted")
    conn.close()
def cleardata():  #user defined function to clear the entry screen
    list1.delete(0,'end')
    eid.delete(0,'end')
    en.delete(0,'end')
    ec.delete(0,'end')
    ed.delete(0,'end')
    es.delete(0,'end')
def next1():  #user defined function to run the salary computation screen after clicking on salary compute button
    os.system('python salary1.py')
    
window=tk.Tk()  #creating window
window.title("Employee Management System") #providing name to window
window.geometry("700x700") #setting up the size of window
window.configure(bg="cyan2") #setting up the background colour of the window screen
empid=tk.Label(window,text="Employee ID",fg="white",bg="orangered2",font=("Arial",12))  #Creating label
empid.place(x=10,y=25) #placing the label
eid=tk.Entry(window,width="25",font=("Arial",10))  #creating entry
eid.place(x=150,y=25) #placing the entry
n=tk.StringVar() #creating string object
c=tk.StringVar() #creating string object
deg=tk.StringVar() #creating string object
s=tk.StringVar() #creating string object
ename=tk.Label(window,text="Employee Name",fg="white",bg="orangered2",font=("Arial",12)) #creating label
ename.place(x=10,y=67) #placing the label
en=tk.Entry(window,width="25",font=("Arial",10),textvariable=n) #creating entry
en.place(x=150,y=65) #placing the entry
empg=tk.Label(window,text="Gender",fg="white",bg="orangered2",font=("Arial",12)) #creating label
empg.place(x=10,y=110) #placing the label
gender=tk.StringVar() #creating string object
male=tk.Radiobutton(window,text="Male",value="M",bg="cyan2",variable=gender) #creating RadioButton
male.place(x=150,y=110)  #placing the RadioButton
female=tk.Radiobutton(window,text="Female",value="F",bg="cyan2",variable=gender) #creating RadioButton
female.place(x=210,y=110) #placing the RadioButton
empc=tk.Label(window,text="Employee City",fg="white",bg="orangered2",font=("Arial",12))  #creating Label
empc.place(x=10,y=155) #placing the label
ec=tk.Entry(window,width="25",font=("Arial",10),textvariable=c) #creating entry
ec.place(x=150,y=155)  #placing the entry
empd=tk.Label(window,text="Employee Designation",fg="white",bg="orangered2",font=("Arial",12)) #creating label
empd.place(x=10,y=200) #placing the label
ed=tk.Entry(window,width="25",font=("Arial",10),textvariable=deg)  #creating entry
ed.place(x=210,y=200)  #placing the entry
emps=tk.Label(window,text="Employee Salary",fg="white",bg="orangered2",font=("Arial",12)) #Creating label
emps.place(x=10,y=245)  #placing the label
es=tk.Entry(window,width="25",font=("Arial",10),textvariable=s) #creating entry
es.place(x=180,y=245)  #placing the entry
ademp=tk.Button(window,text="Add Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=adddata)  #creating button
ademp.place(x=93,y=500) #placing the button
sremp=tk.Button(window,text="Search Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=searchdata)  #creating button
sremp.place(x=210,y=500) #placing the button
shemp=tk.Button(window,text="Show All Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=showdata)  #creating button
shemp.place(x=347,y=500) #placing the button
uemp=tk.Button(window,text="Update Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=updatedata)  #creating button
uemp.place(x=495,y=500) #placing the button 
demp=tk.Button(window,text="Delete Emp.",fg="white",bg="forestgreen",font=("Arial",12),command=deletedata)  #creating button
demp.place(x=629,y=500) #placing the button
clr=tk.Button(window,text="Clear All Text",fg="white",bg="forestgreen",font=("Arial",12),command=cleardata)  #creating button
clr.place(x=750,y=500)  #placing the button
sal=tk.Button(window,text="Salary Compute",fg="white",bg="forestgreen",font=("Arial",12),command=next1)  #creating button
sal.place(x=880,y=500)  #placing the button
list1=tk.Listbox(width='100',height='22') # creating listbox
list1.place(x=500,y=25) #placing the listbox
window.mainloop()#to hold the window screen
