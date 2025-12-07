from tkinter import *
from PIL import Image,ImageTk

root = Tk()

canvas = Canvas(root, width = 500, height = 400)
canvas.pack()

img = Image.open("logo.jpg")
tk_img = img.PhotoImage(img)

canvas.create_image(250, 200, image = tk_img)

canvas.image = tk_img

root.mainloop()
