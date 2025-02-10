from tkinter import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
# Thêm một nút nhấn Click Me
btn = Button(window, text="Click Me", bg="orange", fg="red")
# Thiết lập vị trí của nút nhấn có màu nền và màu chữ
btn.grid(column=1, row=0)

window.mainloop()
