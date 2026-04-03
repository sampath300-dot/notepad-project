import tkinter as tk
from tkinter import filedialog
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.tk.call('tk', 'scaling', 1.5)
root.title("My Notepad")
root.geometry("800x600")

text_area = tk.Text(
    root,
    font=("Segoe UI", 14),
    bg="white",
    fg="black",
    insertbackground="black"
)
text_area.pack(fill="both", expand=1, padx=10, pady=10)

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, file.read())

def save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file:
        file.write(text_area.get(1.0, tk.END))

dark_mode = False

def toggle_dark_mode():
    global dark_mode
    
    if dark_mode:
        text_area.config(bg="white", fg="black", insertbackground="black")
        dark_mode = False
    else:
        text_area.config(bg="#1e1e1e", fg="white", insertbackground="white")
        dark_mode = True

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))

view_menu = tk.Menu(menu)
menu.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)

root.bind("<Control-s>", lambda e: save_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-n>", lambda e: new_file())
root.mainloop()