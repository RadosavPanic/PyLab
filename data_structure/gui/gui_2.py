from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Python App")

lblChoosePLs = Label(window, text="Choose your favorite programming languages:")
frame = Frame(window)

chkPython = Checkbutton(frame, text="Python")
chkJava = Checkbutton(frame, text="Java")
chkJavaScript = Checkbutton(frame, text="JavaScript")
chkCSharp = Checkbutton(frame, text="C#")

lblChooseGender = Label(frame, text="Choose your gender:")
var = StringVar(value="M")
rbMale = Radiobutton(frame, text="Male", variable=var, value="M")
rbFemale = Radiobutton(frame, text="Female", variable=var, value="F")

lblChoosePLs.pack()
frame.pack()
chkPython.pack(); chkJava.pack(); chkJavaScript.pack(); chkCSharp.pack()
lblChooseGender.pack(); rbMale.pack(); rbFemale.pack()

window.mainloop()