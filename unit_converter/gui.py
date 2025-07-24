import tkinter as tk
from tkinter import ttk
from update import Update
from convert import Convert

window = tk.Tk()
window.title("Unit Converter")

width, height = 400, 350
window.geometry(f"{width}x{height}")
window.resizable(False, False)

sirinaEkrana = window.winfo_screenwidth()
visinaEkrana = window.winfo_screenheight()
x = (sirinaEkrana // 2) - (width // 2)
y = (visinaEkrana // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TCombobox", font=("Segoe UI", 11))

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor="center")

lblTitle = tk.Label(frame, text="Unit Converter", font=("Segoe UI", 16, "bold"), fg="blue")
lblTitle.grid(row=0, column=0, columnspan=2, pady=(0, 15))

varCategory = tk.StringVar(value="Length")
category = ttk.Combobox(frame, textvariable=varCategory, state="readonly")
category['values'] = ("Length", "Mass", "Temperature", "Time", "Area", "Speed", "Energy")
category.grid(row=1, column=1, sticky="w", padx=10, pady=10)

lblCategory = tk.Label(frame, text="Category:")
lblCategory.grid(row=1, column=0, sticky="e", padx=10, pady=10)

tk.Label(frame, text="Value:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
inputValue = tk.Entry(frame, font=("Segoe UI", 11), width=17)
inputValue.grid(row=2, column=1, sticky="w", padx=10, pady=10)

tk.Label(frame, text="From unit:").grid(row=3, column=0, sticky="e", padx=10, pady=10)
varFrom = tk.StringVar()
menuFrom = ttk.Combobox(frame, textvariable=varFrom, state="readonly")
menuFrom.grid(row=3, column=1, sticky="w", padx=10, pady=10)

tk.Label(frame, text="To unit:").grid(row=4, column=0, sticky="e", padx=10, pady=10)
varTo = tk.StringVar()
menuTo = ttk.Combobox(frame, textvariable=varTo, state="readonly")
menuTo.grid(row=4, column=1, sticky="w", padx=10, pady=10)

btnConvert = tk.Button(frame, text="Convert")
btnConvert.grid(row=5, column=0, columnspan=2, pady=15)

lblResult = tk.Label(frame, text="", font=("Segoe UI", 14))
lblResult.grid(row=6, column=0, columnspan=2, pady=5)

lblFunFact = tk.Label(frame, text="A fun fact will show up here", fg="blue")
lblFunFact.grid(row=7, column=0, columnspan=2, pady=10)

update = Update(varCategory, menuFrom, varFrom, menuTo, varTo)
convert = Convert(inputValue, varCategory, varFrom, varTo, lblResult, lblFunFact)

category.bind("<<ComboboxSelected>>", update.updateUnits)
btnConvert.config(command=convert.convert)

update.updateUnits()

window.mainloop()
