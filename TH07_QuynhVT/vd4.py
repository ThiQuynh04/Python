from tkinter import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Hàm khi nút được nhấn
def clicked():
    lbl.configure(text="Button was clicked !!")

# Gọi hàm clicked khi nút được nhấn
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()
