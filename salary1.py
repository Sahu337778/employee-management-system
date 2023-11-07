import tkinter as tk  #importing inbuilt library from python
import pymysql   #importing inbuilt library from python
import tkinter.messagebox as mb  #importing inbuilt library from python

def searchdata(): #user defined function for search button
    conn=pymysql.connect(host='localhost',user='root',password='Root@1234',database='employee_management') #to connect with database conn = user defined object
    cur=conn.cursor() #inbuilt method cursor()
    q="select * from employee where eid="+empid.get()+"" #to run the written query means to search the data queried
    cur.execute(q) #to execute query of 'q' from above line
    records=cur.fetchall() #to fetch all records

    for row in records: #loop to set the value
        d=str(row[0])+""+str(row[1])+""+str(row[2])+""+str(row[3])+""+str(row[4])+""+str(row[5])

        s.set(str(row[5]))

    conn.close()


def compute():  #user defined function for salary computation 
    s1=float(emsal.get()) #Basic employee salary
    if(s1<20000):  #condition
        h1=s1*2/100  #House rent calculation
        d1=s1*3/100  #Dearness allowance calculation
        m1=s1*2.5/100 #Medical allowance calculation
        pf=s1*4/100   #provident func calculation
    elif(s1>=20000 and s1<50000):  #condition
        h1=s1*2.5/100  #House rent calculation
        d1=s1*3.5/100  #Dearness allowance calculation
        m1=s1*3/100    #Medical allowance calculation
        pf=s1*4.5/100  #provident fund calculation
    else:           #condition
        h1=s1*3/100  #House rent calculation
        d1=s1*4/100  #Dearness allowance calculation
        m1=s1*3.5/100 #Medical allowance calculation
        pf=s1*5/100 #provident func calculation
    np=s1+h1+d1+m1-pf  #value calculation of net pay
    h.set(str(h1))  #set value of House rent allowance
    d.set(str(d1))  #set value of Deaness allowance
    m.set(str(m1))  #set value of Medical allowance
    p.set(str(pf))  #set value of provident fund allowance
    n.set(str(np))  #set value of net pay
    

def cleartext():   #user defined function for clear text from place of entry
    empid.delete(0,'end')  #to clear the entry space
    emsal.delete(0,'end')  #to clear the entry space
    emhra.delete(0,'end')  #to clear the entry space
    emda.delete(0,'end')   #to clear the entry space
    emma.delete(0,'end')   #to clear the entry space
    empf.delete(0,'end')   #to clear the entry space
    emgs.delete(0,'end')   #to clear the entry space

window=tk.Tk()  #to create window 
window.title("Salary Computation System") #providing title
window.geometry("700x700")  #providing size
window.configure(bg="cyan2")  #providing background colour
eid=tk.Label(window,text="Employee ID",fg="white",bg="orangered2",font=("Arial",12)) #creatng label 
eid.place(x=10,y=25) #placing the label
empid=tk.Entry(window,width="20",font=("Arial",12)) #creatng entry
empid.place(x=210,y=25) #placing the entry
s=tk.StringVar() #creating object
esal=tk.Label(window,text="Employee Basic Salary",fg="white",bg="orangered2",font=("Arial",12))  #creatng label
esal.place(x=10,y=75) #placing the label
emsal=tk.Entry(window,width="20",font=("Arial",12),textvariable=s) #creating entry
emsal.place(x=210,y=75) #placing the entry
h=tk.StringVar() #creating object
d=tk.StringVar() #creating object
m=tk.StringVar() #creating object
p=tk.StringVar() #creating object
n=tk.StringVar() #creating object
ehra=tk.Label(window,text="House Rent Allowance",fg="white",bg="orangered2",font=("Arial",12)) #creating label
ehra.place(x=10,y=125) #Placing the label
emhra=tk.Entry(window,width="20",font=("Arial",12),textvariable=h) #creating entry
emhra.place(x=210,y=125) #placing the entry
da=tk.Label(window,text="Dearness Allowance",fg="white",bg="orangered2",font=("Arial",12)) #creating label
da.place(x=10,y=175) #Placing the label
emda=tk.Entry(window,width="20",font=("Arial",12),textvariable=d) #creating entry
emda.place(x=210,y=175) #placing the entry
ma=tk.Label(window,text="Medical allowance",fg="white",bg="orangered2",font=("Arial",12)) #creaating label
ma.place(x=10,y=225) #placing the label
emma=tk.Entry(window,width="20",font=("Arial",12),textvariable=m) #creating entry
emma.place(x=210,y=225) #placing the entry
pf=tk.Label(window,text="Provident Fund",fg="white",bg="orangered2",font=("Arial",12)) #creating label
pf.place(x=10,y=275) #placing the label
empf=tk.Entry(window,width="20",font=("Arial",12),textvariable=p) #creating entry
empf.place(x=210,y=275) #placing the entry
gs=tk.Label(window,text="Net Salary",fg="white",bg="orangered2",font=("Arial",12)) #Creating the lbel
gs.place(x=10,y=325) #placing the label
emgs=tk.Entry(window,width="20",font=("Arial",12),textvariable=n) #creating the entry
emgs.place(x=210,y=325) #placing the entry
srem=tk.Button(window,text="Search Employee",fg="white",bg="forestgreen",font=("Arial",12),command=searchdata) #creating button
srem.place(x=120,y=450) #placing the button
csal=tk.Button(window,text="Compute Salary",fg="white",bg="forestgreen",font=("Arial",12),command=compute) #creating button
csal.place(x=300,y=450) #placing the button
clr=tk.Button(window,text="Clear All Text",fg="white",bg="forestgreen",font=("Arial",12),command=cleartext) #creating button
clr.place(x=471,y=450) #placing the button
window.mainloop() #to hold the window screen
