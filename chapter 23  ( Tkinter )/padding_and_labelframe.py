import tkinter as tk
from tkinter import ttk 
winner=tk.Tk()
win = tk.Tk()
win.title("LOOP")
winner.title("Label Frame")


# Padding ---> create spaces

labels=["what is your name : ","what is your age : ","what is your gender : ","country : ","state : ","city : "]

for i in range(len(labels)) :
    cur_label="Label"+str(i)
    cur_label=ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W,padx=50,pady=50)




label_frame=ttk.LabelFrame(winner,text="Enter your detail below")
label_frame.grid(row=0,column=0,pady=30)

labels=["what is your name : ","what is your age : ","what is your gender : ","country : ","state : ","city : "]

for i in range(len(labels)) :
    cur_label="Label"+str(i)
    cur_label=ttk.Label(label_frame,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)


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
    cur_entry=ttk.Entry(label_frame,width=16,textvariable=user_info[i])
    cur_entry.grid(row=counter,column=1)
    counter+=1

Submit_frame=ttk.LabelFrame(winner,text="Submit Here")
Submit_frame.grid(row=1,column=0,pady=30)

submit_button=ttk.Button(Submit_frame,text="submit")
submit_button.grid(row=0,columnspan=2)

for child in label_frame.winfo_children() :
    child.grid_configure(padx=10,pady=10)



win.mainloop()
