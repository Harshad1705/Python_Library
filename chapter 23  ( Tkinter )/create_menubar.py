import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("Menubar")

def func():
    print("func called")

menubar=tk.Menu(win)

# ****************** Simple MenuBar ****************************
# menubar.add_command(label="save",command=func)
# menubar.add_command(label="copy",command=func)
# menubar.add_command(label="paste",command=func)

main_menu=tk.Menu(win)

file_menu=tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="save",command=func)
file_menu.add_command(label="New file",command=func)
file_menu.add_separator()                                       # for line b/w two command
file_menu.add_command(label="settings",command=func)

edit_menu=tk.Menu(main_menu)
edit_menu.add_command(label="clear",command=func)
edit_menu.add_command(label="copy",command=func)


main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)

win.config(menu=main_menu)
win.mainloop()