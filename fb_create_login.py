from tkinter import *

db={}
root=Tk()
root.geometry("421x421")
root.title("FACEBOOK")

label_f=Label(root,text="Facebook",bg="blue",fg="white")
label_f.pack()

label_u=Label(root,text="Username")
label_u.place(x=70,y=50)
label_p=Label(root,text="Password")
label_p.place(x=70,y=90)
label_d=Label(root,text=" ")
label_d.place(x=110,y=150)

entry_1=Entry(root)
entry_1.place(x=140,y=50)
entry_2=Entry(root)
entry_2.place(x=140,y=90)

def display():
    u=entry_1.get()
    p=entry_2.get()
    db.update({u:p})
    label_d.configure(text="created successfully")
    entry_1.delete(0,END)
    entry_2.delete(0,END)

def login():
    u=entry_1.get()
    for i in db:
        if i == u:
            p=entry_2.get()
            if p==db[u]:
                label_d.configure(text="Login successfully..")
                entry_1.delete(0,END)
                entry_2.delete(0,END)
                break
            else:
                label_d.configure(text="Incorrect password")
                entry_2.delete(0,END)
                break
    else:
        label_d.configure(text="Invalid  username..")
        entry_2.delete(0,END)
        
button_1=Button(root,text="Create",bg="blue",fg="white",command=display)
button_1.place(x=120,y=120)
button_2=Button(root,text="Login",bg="blue",fg="white",command=login)
button_2.place(x=180,y=120)

root.mainloop()
