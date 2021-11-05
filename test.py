import tkinter as tk
from PIL import ImageTk, Image


def resize_image(img):
    img_width = img.width
    img_height = img.height
    print(img_height, img_width)


root = tk.Tk()
example_img = ImageTk.PhotoImage(file="images/example.png")



resize_image(example_img)