import tkinter as tk
from tkinter import messagebox, ttk

C = "0123456789ABCDEF"

def to_dec(s, b):
    r = 0
    for x in s.strip().upper():
        if x not in C[:b]: raise ValueError()
        r = r * b + C.index(x)
    return r

def from_dec(n, b):
    if n == 0: return "0"
    r = ""
    while n > 0:
        r = C[n % b] + r
        n //= b
    return r

root = tk.Tk()
root.title("Calculatrice")
root.maxsize(450, 400)

m = tk.Frame(root, padx=10, pady=10)
m.pack()

ent = tk.Text(m, height=2, width=30, font=("Arial", 12))
ent.grid(row=0, column=0, columnspan=5, pady=5)

def click(v):
    if v == "=":
        try:
            res = eval(ent.get("1.0", tk.END))
            ent.delete("1.0", tk.END)
            ent.insert(tk.END, str(res))
        except: messagebox.showerror("Erreur", "Calcul impossible")
    else: ent.insert(tk.END, v)

btns = ["7","8","9","/", "4","5","6","*", "1","2","3","-", "0",".","+","="]
for i, b in enumerate(btns):
    tk.Button(m, text=b, width=5, height=2, command=lambda x=b: click(x)).grid(row=i//4+1, column=i%4)

fh = tk.Frame(m)
for i, l in enumerate("ABCDEF"):
    tk.Button(fh, text=l, width=5, height=2, command=lambda x=l: click(x)).grid(row=i, column=0)

c1 = ttk.Combobox(m, values=[2, 8, 10, 16], width=5, state="readonly")
c1.current(2)
c1.grid(row=6, column=1, pady=5)

c2 = ttk.Combobox(m, values=[2, 8, 10, 16], width=5, state="readonly")
c2.current(3)
c2.grid(row=6, column=2, pady=5)

def update(e=None):
    if c1.get() == "16": fh.grid(row=1, column=4, rowspan=5, padx=5)
    else: fh.grid_forget()
    root.geometry("")

c1.bind("<<ComboboxSelected>>", update)
update()

def convert():
    try:
        val = ent.get("1.0", tk.END).strip()
        res = from_dec(to_dec(val, int(c1.get())), int(c2.get()))
        ent.delete("1.0", tk.END)
        ent.insert(tk.END, res)
    except: messagebox.showerror("Erreur", "Saisie incorrecte")

tk.Button(m, text="Effacer", width=24, command=lambda: ent.delete("1.0", tk.END)).grid(row=5, column=0, columnspan=4)
tk.Button(m, text="Convertir", command=convert, height=2).grid(row=6, column=3, columnspan=2, sticky="ew")

root.mainloop()