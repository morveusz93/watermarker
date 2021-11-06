import tkinter as tk
from tkinter import StringVar, filedialog, colorchooser
from tkinter import font
from tkinter.constants import DISABLED

class WatermarkPickerFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Choose a watermark"
        tk.LabelFrame.__init__(self, master=self.root, text=frame_label, padx=20, pady=20, *args, **kwargs)

        self.text_or_img = tk.StringVar()
        self.text_or_img.set('text')

        # choose a photo
        self.radio_img = tk.Radiobutton(self, variable=self.text_or_img, value="img", command=self.switch_text_or_img)
        self.radio_img.grid(column=0, row=2)
        self.photo_label = tk.Label(self, text="Watermark with a PHOTO", state=DISABLED)
        self.photo_label.grid(column=1, row=2, sticky="W")
        self.img_path = tk.StringVar()
        self.img_name_entry = tk.Entry(self, width=50, textvariable=self.img_path, state=tk.DISABLED)
        self.img_name_entry.grid(column=1, row=3)
        self.img_button = tk.Button(self, text='Pick a photo', command=self.select_photo, state=tk.DISABLED)
        self.img_button.grid(column=2, row=3)


        # choose a text
        self.text_label = tk.Label(self, text="Watermark with a TEXT")
        self.text_label.grid(column=1, row=4, sticky="W")
        self.radio_text = tk.Radiobutton(self, variable=self.text_or_img, value="text", command=self.switch_text_or_img)
        self.radio_text.grid(column=0, row=4)
        self.text = tk.StringVar()
        self.text_entry = tk.Entry(self, width=50, textvariable=self.text)
        self.text_entry.grid(column=1, row=5)

        # FONT SIZE
        tk.Label(self, text="Font size: ").grid(column=1, row=6, sticky="W")
        self.font_size = tk.IntVar()
        self.font_size.set(12)
        self.font_size_entry = tk.Spinbox(self, textvariable=self.font_size, from_=1, to=100)
        self.font_size_entry.grid(column=1, row=7, sticky="W")
        
        # FONT COLOR
        tk.Label(self, text="Font color: ").grid(column=1, row=8, sticky="W")
        self.font_color = StringVar(value="#000000")
        self.font_color_entry = tk.Entry(self, width=25, textvariable=self.font_color, state=tk.DISABLED)
        self.font_color_entry.grid(column=1, row=9, sticky="W")

        self.font_color_button = tk.Button(self, text="Pick color", command=self.select_color)
        self.font_color_button.grid(column=1, row=9)

    def switch_text_or_img(self):        
        if self.text_or_img.get() == 'text':
            self.img_name_entry.config(state=tk.DISABLED)
            self.img_button.config(state=tk.DISABLED)
            self.photo_label.config(state=tk.DISABLED)
            self.text_entry.config(state=tk.NORMAL)
            self.text_label.config(state=tk.NORMAL)
            self.font_size_entry.config(state=tk.NORMAL)
            self.font_color_entry.config(state=tk.NORMAL)

        elif self.text_or_img.get() == 'img':
            self.text_entry.config(state=tk.DISABLED)
            self.text_label.config(state=tk.DISABLED)
            self.font_size_entry.config(state=tk.DISABLED)
            self.font_color_entry.config(state=tk.DISABLED)
            self.img_name_entry.config(state=tk.NORMAL)
            self.photo_label.config(state=tk.NORMAL)
            self.img_button.config(state=tk.NORMAL)
        

    # open window with selceting direcory, next insert it into entry
    def select_photo(self):
        self.img_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("image files","*.jpg *.jpeg *.png"),("all files","*.*")))
        self.img_name_entry.insert(0, self.img_path)

    def select_color(self):
        self.font_color.set(colorchooser.askcolor(title="Font color:")[1])
        if self.font_color.get() == 'None':
            self.font_color.set("#000000")