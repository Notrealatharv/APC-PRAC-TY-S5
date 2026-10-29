# COMPLETE TKINTER PROGRAM - ALL WIDGETS

import tkinter as tk
from tkinter import ttk, messagebox

# Create main window
root = tk.Tk()
root.title("Python Tkinter All Widgets")
root.geometry("500x750")

# 1. LABEL
tk.Label(root, text="PYTHON GUI APPLICATION",
         font=("Arial", 16, "bold")).pack(pady=5)

# 2. ENTRY
tk.Label(root, text="Enter your name:").pack()
entry = tk.Entry(root)
entry.pack(pady=3)

# 3. BUTTON
def show_name():
    name = entry.get()
    messagebox.showinfo("Welcome", "Hello " + name)

tk.Button(root, text="Submit", command=show_name).pack(pady=3)

# 4. CHECKBUTTON
tk.Label(root, text="Select hobbies:").pack()
hobby1 = tk.IntVar()
hobby2 = tk.IntVar()

tk.Checkbutton(root, text="Reading", variable=hobby1).pack()
tk.Checkbutton(root, text="Music", variable=hobby2).pack()

# 5. RADIOBUTTON
tk.Label(root, text="Select gender:").pack()
gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").pack()

# 6. LISTBOX
tk.Label(root, text="Select a language:").pack()
languages = tk.Listbox(root, height=3)
for item in ["Python", "Java", "C++"]:
    languages.insert(tk.END, item)
languages.pack(pady=3)

# 7. COMBOBOX
tk.Label(root, text="Select a course:").pack()
combo = ttk.Combobox(root, values=["CSE", "IT", "ENTC"])
combo.set("CSE")
combo.pack(pady=3)

# 8. SCALE
tk.Label(root, text="Select a value:").pack()
scale = tk.Scale(root, from_=0, to=100,
                 orient=tk.HORIZONTAL)
scale.pack()

# 9. SPINBOX
tk.Label(root, text="Select your age:").pack()
spin = tk.Spinbox(root, from_=1, to=100, width=10)
spin.pack(pady=3)

# 10. TEXT - MULTILINE INPUT
tk.Label(root, text="Enter your message:").pack()
text = tk.Text(root, height=3, width=35)
text.pack(pady=3)
text.insert(tk.END, "Hello Python!")

# 11. FRAME
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="This is a Frame").pack()

# 12. MESSAGE
tk.Message(root, text="Tkinter is used to create GUI applications.",
           width=300).pack(pady=3)

# 13. CANVAS
canvas = tk.Canvas(root, width=150, height=40,
                   bg="white")
canvas.pack(pady=3)
canvas.create_line(10, 10, 140, 30)
canvas.create_text(75, 20, text="Canvas")

# 14. MENU
menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New",
                     command=lambda: text.delete("1.0", tk.END))
filemenu.add_command(label="Exit", command=root.destroy)

# 15. MENUBUTTON
mb = tk.Menubutton(root, text="More Options",
                   relief=tk.RAISED)
mb_menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb_menu
mb_menu.add_command(label="About",
                    command=lambda: messagebox.showinfo(
                        "About", "Tkinter Demo"))
mb.pack(pady=3)

# 16. TOPLEVEL - SEPARATE WINDOW
def open_window():
    win = tk.Toplevel(root)
    win.title("New Window")
    tk.Label(win, text="This is a separate window").pack(padx=20, pady=20)

tk.Button(root, text="Open New Window",
          command=open_window).pack(pady=3)

# Run application
root.mainloop()