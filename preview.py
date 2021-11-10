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
        tk.Label(self, image=self.example_img).grid(column=0, row=0, columnspan=2)

        # position of watermark

        tk.Label(self, text="Position: ", font=20).grid(column=0, row=1)
        self.positions = ['top-left', 'top-right', 'down-left', 'down-right', 'center']
        self.position = tk.StringVar(value=self.positions)
        self.position_entry = tk.Listbox(self, listvariable=self.position, height=5)
        self.position_entry.grid(column=0, row=2, rowspan=4, sticky=("W"))


        # watermaek size scale
        tk.Label(self, text="Size of watermark: ", font=20).grid(column=1, row=1)
        width = tk.IntVar()
        width.set(self.example_img.width() // 2)
        width_scale = tk.Scale(self, variable=width, from_=1, to=self.example_img.width(), length=300, orient=tk.HORIZONTAL)
        width_scale.grid(column=1, row=2, sticky="NE")


        # opacity scale
        tk.Label(self, text="Opacity: ", font=20).grid(column=1, row=3)
        opacity = tk.IntVar()
        opacity.set(50)
        opacity_scale = tk.Scale(self, variable=opacity, from_=1, to=100, length=300, orient=tk.HORIZONTAL)
        opacity_scale.grid(column=1, row=4, sticky="NE")


    def resize_image(self, img):
        img_width = img.width
        img_height = img.height

        new_width = 450
        prop = new_width / img_width

        new_height = int(img_height * prop)

        return img.resize((new_width, new_height))
    