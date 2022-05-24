from tkinter import *
from tkinter import messagebox

#backend
def fahrenheit_to_celsius():
    try:
        f=entry_f.get()
        c=(5/9)*(float(f)-32)
        label_fc.config(text=f"{round(c,2)} \N{DEGREE CELSIUS}")
    except ValueError:
        messagebox.showinfo("Error","Enter value")
    except Exception as e:
        messagebox.showinfo("Error","Invalid Input")
        
def celsius_to_fahrenheit():
    try:
        c=entry_c.get()
        f=(float(c)*9/5)+32
        label_cf.config(text=f'{round(f,2)}\N{DEGREE FAHRENHEIT}')
    except ValueError:
        messagebox.showinfo("Error","Enter value")
    except Exception as e:
        messagebox.showinfo("Error","Invalid Input")
     
#frontend
root = Tk()
root.title("Workout")
root.geometry("421x421")

title_lab=Label(root,text="Converting From \N{DEGREE FAHRENHEIT}  To  \N{DEGREE CELSIUS}",bg='Yellow')
title_lab.place(x=100,y=0)

entry_f=Entry(root,width='5')
entry_f.place(x=50,y=50)
entry_c=Entry(root,width='5')
entry_c.place(x=50,y=100)

label_f=Label(root,text="\N{DEGREE FAHRENHEIT}",bg='red',width='3')
label_f.place(x=80,y=50)
label_c=Label(root,text="\N{DEGREE CELSIUS}",bg="red",width='3')
label_c.place(x=80,y=100)

button_1=Button(root,text='\N{RIGHTWARDS BLACK ARROW}',width='5',command=fahrenheit_to_celsius)
button_1.place(x=110,y=46)
button_2=Button(root,text="\N{RIGHTWARDS BLACK ARROW}",width='5',command=celsius_to_fahrenheit)
button_2.place(x=110,y=96)

label_fc=Label(root,text='\N{DEGREE CELSIUS}',bg='green',fg='white',width='6')
label_fc.place(x=160,y=50)
label_cf=Label(root,text="\N{DEGREE FAHRENHEIT}",bg='green',fg='white',width='6')
label_cf.place(x=160,y=100)

root.mainloop()
