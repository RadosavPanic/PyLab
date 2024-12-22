from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Python App")

appWidth, appHeight = 260, 200
screenWidth, screenHeight = window.winfo_screenwidth(), window.winfo_screenheight()

centerPositionX = (screenWidth // 2) - (appWidth // 2)
centerPositionY = (screenHeight // 2) - (appHeight // 2)

window.geometry(f"{appWidth}x{appHeight}+{centerPositionX}+{centerPositionY}")

def showWelcomeMessage():
    messagebox.showinfo("Welcome to Python App", "Welcome to our app.\nExplore our catalogue and pick your choice.\nGood luck!")

lblTitle = Label(window, text="Python - GUI Exercise", bg="white", fg="blue", font=('Serif', 16, 'underline'))

img = Image.open("py_icon.png")
logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo)

lblUsername = Label(window, text="Username", font=('Serif', 12))
inputUsername = Entry(window)

def greetUser(event=None):
    username = inputUsername.get()
    if username == "":
        messagebox.showwarning("No username inserted", "Please insert your username first. Try again.")
        return
    messagebox.showinfo("Success", f"Successful login! Welcome {username}!")

btnStart = Button(window, text="Welcome!", command=showWelcomeMessage)
btnLogin = Button(window, text="Login"); btnLogin.bind('<Button-1>', greetUser)

lblTitle.pack()
image.pack()
lblUsername.place(x=20, y=97)
inputUsername.place(x=120, y=100)
btnStart.place(x=100, y=130)
btnLogin.place(x=110, y=160)

window.mainloop()