# creating labels, entrybox with loop

import tkinter as tk
from tkinter import ttk 
win = tk.Tk()
win.title("LOOP")

# Labels

labels=["what is your name : ","what is your age : ","what is your gender : ","country : ","state : ","city : "]

# name_label=ttk.Label(win,text="what is your name :")
# name_label.grid(row=0,column=0,sticky=tk.W)

for i in range(len(labels)) :
    cur_label="Label"+str(i)
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

# Entry box

# namevar=tk.StringVar()
# name_entry=ttk.Entry(win,width=16,textvariable=namevar)
# name_entry.grid(row=0,column=1)

user_info={
            "Name" : tk.StringVar(),
            " Age" : tk.StringVar(),
            "Gender" : tk.StringVar(),
            "Country" : tk.StringVar(),
            "State" : tk.StringVar(),
            "City" : tk.StringVar(),
}
counter=0
for i in user_info:
    cur_entry="entry"+i
    cur_entry=ttk.Entry(win,width=16,textvariable=user_info[i])
    cur_entry.grid(row=counter,column=1)
    counter+=1

# Submit Button

def submit ():
    for i in user_info :
        print(user_info[i].get())

submit_button=ttk.Button(win,text="Submit",command=submit)
submit_button.grid(row=counter,columnspan=2)


win.mainloop()