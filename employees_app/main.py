from tkinter import *
from crud_fns import insertData, updateData, getData, deleteData, showDataInListBox, resetFields

window = Tk()
window.title("Employees App")

appWidth, appHeight = 600, 270
screenWidth, screenHeight = window.winfo_screenwidth(), window.winfo_screenheight()
centerPositionX = (screenWidth // 2) - (appWidth // 2)
centerPositionY = (screenHeight // 2) - (appHeight // 2)

window.geometry(f"{appWidth}x{appHeight}+{centerPositionX}+{centerPositionY}")

empId = Label(window, text="Employee ID", font=('Serif', 12)); empId.place(x=20,y=30)
empName = Label(window, text="Employee Name", font=('Serif', 12)); empName.place(x=20, y=60)
empDept = Label(window, text="Employee Dept", font=('Serif', 12)); empDept.place(x=20, y=90)

enterId = Entry(window); enterId.place(x=170, y=30)
enterName = Entry(window); enterName.place(x=170, y=60)
enterDept = Entry(window); enterDept.place(x=170, y=90)

lbShowData = Listbox(window, width=30, height=10); lbShowData.place(x=330, y=30)

insertBtn = Button(window, text="Insert", font=('Sans', 12), bg="white", command=lambda: insertData(enterId, enterName, enterDept, lbShowData)); insertBtn.place(x=20, y=160)
updateBtn = Button(window, text="Update", font=('Sans', 12), bg="white", command=lambda: updateData(enterId, enterName, enterDept, lbShowData)); updateBtn.place(x=80, y=160)
getBtn = Button(window, text="Fetch", font=('Sans', 12), bg="white", command=lambda: getData(enterId, enterName, enterDept)); getBtn.place(x=150, y=160)
deleteBtn = Button(window, text="Delete", font=('Sans', 12), bg="white", command=lambda: deleteData(enterId, enterName, enterDept, lbShowData)); deleteBtn.place(x=210, y=160)
resetBtn = Button(window, text="Reset", font=('Sans', 12), bg="white", command=lambda: resetFields(enterId, enterName, enterDept)); resetBtn.place(x=20, y=210)

showDataInListBox(lbShowData)

window.mainloop()