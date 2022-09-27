# starte code 

import tkinter as tk  
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title("GUI")


# create label
name_label=ttk.Label(win,text="Enter Your Name : ")             # layout manager -- 1. pack()  2.grid()
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="Enter Your Mail : ")
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="Enter Your Age : ")
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="Select Your Gender : ")
gender_label.grid(row=3,column=0,sticky=tk.W)

# create entry box 

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

# create combo_box

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("Male","Female","Other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# create Radio button

user_type=tk.StringVar()

radiobtn1=ttk.Radiobutton(win,text='Teacher',value="Teacher",variable=user_type)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text='Student',value="Student",variable=user_type)
radiobtn2.grid(row=4,column=1)

# create check button

checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text=" Check if u want to subscribe",variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)

# create button

def action():
    username=name_var.get()
    usermail=email_var.get()
    userage=age_var.get()
    # print(f"{username} is {userage} old and has mail {usermail} ")
    usergender=gender_var.get()
    usertype=user_type.get()
    if checkbtn_var==0 :
        subscribed = "No"
    else :
        subscribed="Yes"
    # print(usergender,usertype,subscribed)

    # # to write in a file
    # with open("file.txt","a") as f :
    #     f.write(f"{username} , {userage} , {usermail} , {usergender} , {usertype} , {subscribed} \n")

    
    # to write in csv file

    with open("file.csv","a",newline="") as f :
        dict_writer=DictWriter(f,fieldnames=["UserName","UserEmail","UserAge","UserGender","UserType","Subscribed"])
        if os.stat("file.csv").st_size==0 :
            dict_writer.writeheader()
        dict_writer.writerow({
                "UserName" : username  ,
                "UserEmail":usermail  ,
                "UserAge" :userage  ,
                "UserGender" :usergender  ,
                "UserType" :usertype  ,
                "Subscribed" :subscribed 
         })


    name_entrybox.delete(0,tk.END)                    # entry box data removed
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)

    name_label.configure(foreground="Red")           # to change colour of txt after remove data 
    email_label.configure(foreground="#b388ff")
    age_label.configure(foreground="Blue")

    submit_button.configure(foreground="Green")


submit_button=tk.Button(win,text="Submit",command=action)
submit_button.grid(row=6,column=0)







win.mainloop()

