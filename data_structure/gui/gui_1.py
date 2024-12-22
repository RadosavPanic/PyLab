from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Python App")

appWidth, appHeight = 260, 170
screenWidth, screenHeight = window.winfo_screenwidth(), window.winfo_screenheight()

centerPositionX = (screenWidth // 2) - (appWidth // 2)
centerPositionY = (screenHeight // 2) - (appHeight // 2)

window.geometry(f"{appWidth}x{appHeight}+{centerPositionX}+{centerPositionY}")

lblTitle = Label(window, text="Python - GUI Exercise", bg="white", fg="blue", font=('Serif', 16, 'underline'))

img = Image.open("py_icon.png")
logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo)

username = Label(window, text="Username", font=('Serif', 12))
inputUsername = Entry(window)
btnStart = Button(window, text="Let's start")

lblTitle.pack()
image.pack()
username.place(x=20, y=97)
inputUsername.place(x=120, y=100)
btnStart.place(x=100, y=130)

window.mainloop()