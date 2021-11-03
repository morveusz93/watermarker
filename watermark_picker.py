import tkinter as tk
from tkinter import filedialog

class WatermarkPicker(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Choose a watermark"
        tk.LabelFrame.__init__(self, master=self.root, text=frame_label, padx=20, pady=20, *args, **kwargs)

        self.text_or_img = tk.StringVar()
        self.text_or_img.set('text')

        # choose a text
        self.radio_text = tk.Radiobutton(self, variable=self.text_or_img, value="text", command=self.switch_text_or_img)
        self.radio_text.grid(column=0, row=2)
        self.text = tk.StringVar()
        self.text_entry = tk.Entry(self, width=50, textvariable=self.text)
        self.text_entry.grid(column=1, row=2)
        self.text_label = tk.Label(self, text="TEXT")
        self.text_label.grid(column=2, row=2)


        # choose a photo
        self.radio_img = tk.Radiobutton(self, variable=self.text_or_img, value="img", command=self.switch_text_or_img)
        self.radio_img.grid(column=0, row=3)
        self.img_path = tk.StringVar()
        self.img_name_entry = tk.Entry(self, width=50, textvariable=self.img_path, state=tk.DISABLED)
        self.img_name_entry.grid(column=1, row=3)
        self.img_button = tk.Button(self, text='Pick a photo', command=self.select_photo, state=tk.DISABLED)
        self.img_button.grid(column=2, row=3)



    def switch_text_or_img(self):        
        if self.text_or_img.get() == 'text':
            self.img_name_entry.config(state=tk.DISABLED)
            self.img_button.config(state=tk.DISABLED)
            self.text_entry.config(state=tk.NORMAL)
            self.text_label.config(state=tk.NORMAL)

        elif self.text_or_img.get() == 'img':
            self.text_entry.config(state=tk.DISABLED)
            self.text_label.config(state=tk.DISABLED)
            self.img_name_entry.config(state=tk.NORMAL)
            self.img_button.config(state=tk.NORMAL)
        

    # open window with selceting direcory, next insert it into entry
    def select_photo(self):
        self.img_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("image files","*.jpg *.jpeg *.png"),("all files","*.*")))
        self.img_name_entry.insert(0, self.img_path)

