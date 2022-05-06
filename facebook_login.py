from tkinter import *
from tkinter import messagebox
import mysql.connector

#backend
# mysql_database
class facebook:
    def __init__(self,db):
        self.db=db
    def dc(self):
        u_name = name_.get()
        u_passwd = passwd_.get()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="facebook"
        )
        db_cursor = self.db.cursor()
        db_cursor.execute("SELECT user_name FROM facebook.create_acct")
        for i in db_cursor:
            if u_name == i[0]:
                messagebox.showinfo("STATUS","Username is already Taken..")
                break
        else:
            sql = "INSERT INTO create_acct(user_name,user_passwd) VALUES (%s,%s)"
            data = (u_name, u_passwd)
            db_cursor.execute(sql, data)
            self.db.commit()
            messagebox.showinfo("STATUS", "Created Successfully.")

    def dl(self):
        u_n = name_.get()
        u_p = passwd_.get()
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="facebook"
        )
        db_cursor = self.db.cursor()
        db_cursor.execute("SELECT user_name,user_passwd FROM facebook.create_acct")

        for i in db_cursor:
            if u_n == i[0]:
                if u_p==i[1]:
                    messagebox.showinfo("STATUS","Login Successfully.")
                    break
                else:
                    messagebox.showinfo("STATUS","Incorrect password")
                    break
        else:
            messagebox.showinfo("STATUS","Invalid Username")

f = facebook(db="")


# frontend
root = Tk()
root.geometry("421x421")
root.title("FACEBOOK")

label_f = Label(root, text="Facebook", bg="blue", fg="white")
label_f.pack()

label_u = Label(root, text="Username")
label_u.place(x=70, y=50)
label_p = Label(root, text="Password")
label_p.place(x=70, y=90)
label_d = Label(root, text=" ")
label_d.place(x=110, y=150)

name_ = Entry(root)
name_.place(x=140, y=50)
passwd_ = Entry(root)
passwd_.place(x=140, y=90)
button_1 = Button(root, text="Create", bg="blue", fg="white",command=f.dc)
button_1.place(x=120, y=120)
button_2 = Button(root, text="Login", bg="blue", fg="white",command=f.dl)
button_2.place(x=180, y=120)

root.mainloop()

