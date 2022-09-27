
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as m_box
win=tk.Tk()

# label frame

label_frame=ttk.LabelFrame(win,text="Details")
label_frame.grid(row=0,column=0,pady=20)

# labels

name_label=ttk.Label(label_frame,text="Enter tour Name : ", font=('Helvetica',16,"bold"))
age_label=ttk.Label(label_frame,text="Enter tour age : ", font=('Helvetica',16,"bold"))

# Entry Box Variable

name_var = tk.StringVar()
age_var = tk.StringVar()

# Entry Box

name_entry=ttk.Entry(label_frame,width=24,textvariable=name_var)
age_entry=ttk.Entry(label_frame,width=24,textvariable=age_var)

# Grid

name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)


def submit() :
    name=name_var.get()
    age=age_var.get()

    if name=='' or age=='' :
        m_box.showerror("Error","Fill both name and age")
    else :
        # age="ikgdeswab"
        # age="18"
        try :
            age=int(age)
        except ValueError:
            m_box.showerror("Error","Enter age in integer")
        else :
            name1=name.title()
            print(f'{name1} : {age}')




submit_button=ttk.Button(win,text="Submit",command=submit)
submit_button.grid(row=1,columnspan=2)


win.mainloop()