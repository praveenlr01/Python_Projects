from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename


#backend
def open_():
    file_path=askopenfilename(filetypes=[("TextFile","*.txt"),("All Files","*.*")])
    if not file_path:
        return
    text.delete(1.0,END)
    with open(file_path,'r') as input_file:
        text_=input_file.read()
        text.insert(END,text_)
    root.title(f'sample Notepad - {file_path}')


def save_():
    file_path=asksaveasfilename(defaultextension="*.txt",filetypes=[("textfile","*.txt"),("allfile","*.*")])
    if not file_path:
        return
    with open(file_path,'w') as output_file:
        txt=text.get(1.0,END)
        output_file.write(txt)
    root.title(f"sample Notepad - {file_path}")


#frontend
root=Tk()
root.title("Sample NotePad")

text=Text(root)

frame=Frame(root,relief=GROOVE,borderwidth=3)
frame.grid(row=1,column=0,sticky='new')

but_open=Button(frame,text="Open",fg='black',activebackground="blue",command=open_)
but_open.grid(row=1,column=0,sticky='n')
but_save=Button(frame,text="Save",fg='black',activebackground="blue",command=save_)
but_save.grid(row=1,column=1,sticky='n')

text.grid(row=2,column=0,sticky="nsew")

root.mainloop()
