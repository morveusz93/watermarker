import tkinter as tk
from os import path
from os.path import join

from PIL import Image, ImageTk

from .utilities import resize_image


class PreviewFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Preview"
        tk.LabelFrame.__init__(
            self, master=self.root, text=frame_label, padx=20, pady=20, *args, **kwargs
        )

        # image
        self.preview_canvas = tk.Canvas(self, width=450)
        self.preview_canvas.grid(column=0, row=0, columnspan=2)
        self.preview_img_path = join("images", "example.jpg")
        self.open_perview_img()

        # position of watermark
        tk.Label(self, text="Position: ", font=20).grid(column=0, row=1)
        self.positions = ["top-left", "top-right", "down-left", "down-right", "center"]
        self.position = tk.StringVar(value=self.positions)
        self.position_entry = tk.Listbox(
            self, listvariable=self.position, height=5, exportselection=False
        )
        self.position_entry.selection_set(first=3)
        self.position_entry.grid(column=0, row=2, rowspan=4, sticky=("W"))

        # width_prop is percent of watermark width to full image width
        # watermaek size scale
        tk.Label(self, text="Size of watermark (percent): ", font=20).grid(
            column=1, row=1
        )
        self.width_prop = tk.IntVar()
        self.width_prop.set(25)
        self.width_scale = tk.Scale(
            self,
            variable=self.width_prop,
            from_=1,
            to=100,
            length=300,
            orient=tk.HORIZONTAL,
        )
        self.width_scale.grid(column=1, row=2, sticky="NE")

        # opacity scale
        tk.Label(self, text="Opacity: ", font=20).grid(column=1, row=3)
        self.opacity = tk.IntVar()
        self.opacity.set(125)
        self.opacity_scale = tk.Scale(
            self,
            variable=self.opacity,
            from_=1,
            to=255,
            length=300,
            orient=tk.HORIZONTAL,
        )
        self.opacity_scale.grid(column=1, row=4, sticky="NE")

    def open_perview_img(self):
        # open example img
        new_width = 450
        img = resize_image(Image.open(self.preview_img_path), new_width)
        self.preview_img = ImageTk.PhotoImage(img)
        self.preview_canvas.create_image(0, 0, anchor="nw", image=self.preview_img)
