import mysql.connector
from tkinter import *
from tkinter import messagebox

def dc():
    name = name_e.get()
    phone = phone_e.get()
    adds = addr_e.get()
    db = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        passwd='123456',
        database='database_ether'
    )
    db_cursor = db.cursor()
    try:
        sql ="INSERT INTO `database_ether`.`emoployee_ether` (`empname`, `empphone`, `empadd`) VALUES (%s,%s,%s)"
        val = (name,phone,adds)
        db_cursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("STATUS","Created successfully...")
    except Exception as e:
        messagebox.showinfo("Error:", e)
        db.rollback()
        db.close()

r = Tk()
r.title("Employee Database")
r.geometry("300x420")

Label(r,text="ETHER_INFO",bg="white",fg="green",font=("Times",20)).pack()
Label(r,text="Employee Name").place(x=10,y=60)
Label(r,text="Phone Number").place(x=10,y=120)
Label(r,text="Address").place(x=10,y=180)

name_e=Entry(r)
name_e.place(x=110,y=60)
phone_e=Entry(r)
phone_e.place(x=110,y=120)
addr_e=Entry(r)
addr_e.place(x=110,y=180)

Button(r,text="CREATE",bg="blue",fg="white",width=8,height=1,command=dc).place(x=100,y=230)

r.mainloop()
