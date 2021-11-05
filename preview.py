import tkinter as tk
from PIL import ImageTk, Image


class PreviewFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Preview"
        tk.LabelFrame.__init__(self, master=self.root, text=frame_label, padx=20, pady=20, *args, **kwargs)


        # open example img
        img = self.resize_image(Image.open("images/ekko_0.jpg"))
        self.example_img = ImageTk.PhotoImage(img)
        
    
        # insert IMAGE on screen
        tk.Label(self, image=self.example_img).grid(column=0, row=0)


    def resize_image(self, img):
        img_width = img.width
        img_height = img.height
        print(img.width, img.height)

        new_width = 450
        prop = new_width / img_width

        new_height = int(img_height * prop)

        return img.resize((new_width, new_height))
    