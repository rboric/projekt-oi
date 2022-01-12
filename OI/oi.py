import tkinter as tk

root = tk.Tk()
root.title("OI")

e = tk.Entry(root, width=50, borderwidth=5)
c = tk.Entry(root, width=50, borderwidth=5)

e.grid(row=0, column=0, padx=40, pady=20) 
c.grid(row=1, column=0, padx=45)

root.mainloop()