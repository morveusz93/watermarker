import tkinter as tk
from tkinter import filedialog

# create frame where the folder with photos will be selected
class PhotosPickerFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Choose a directory or a single photo"
        tk.LabelFrame.__init__(self, master=self.root, text=frame_label, padx=20, pady=20, *args, **kwargs)
        
        self.img_or_dir = tk.StringVar()
        self.img_or_dir.set("dir")

        # choose directory
        self.radio_dir = tk.Radiobutton(self, variable=self.img_or_dir, value="dir", command=self.switch_img_or_dir)
        self.radio_dir.grid(column=0, row=2)
        self.dir_label = tk.Label(self, text="Choose a directory")
        self.dir_label.grid(column=1, row=2, sticky="W")
        self.directory = tk.StringVar()
        self.dir_name_entry = tk.Entry(self, width=50, textvariable=self.directory)
        self.dir_name_entry.grid(column=1, row=3)
        self.dir_button = tk.Button(self, text='Pick folder', command=self.select_dir)
        self.dir_button.grid(column=2, row=3)

        # choose single photo
        self.radio_img = tk.Radiobutton(self, variable=self.img_or_dir, value="img", command=self.switch_img_or_dir)
        self.radio_img.grid(column=0, row=4)
        self.img_label = tk.Label(self, text="Choose a single photo", state=tk.DISABLED)
        self.img_label.grid(column=1, row=4, sticky="W")
        self.img_path = tk.StringVar()
        self.img_name_entry = tk.Entry(self, width=50, textvariable=self.img_path, state=tk.DISABLED)
        self.img_name_entry.grid(column=1, row=5)
        self.img_button = tk.Button(self, text='Pick photo', command=self.select_photo, state=tk.DISABLED)
        self.img_button.grid(column=2, row=5)


    def switch_img_or_dir(self):        
        if self.img_or_dir.get() == 'img':
            self.dir_name_entry.config(state=tk.DISABLED)
            self.dir_button.config(state=tk.DISABLED)
            self.dir_label.config(state=tk.DISABLED)
            self.img_name_entry.config(state=tk.NORMAL)
            self.img_button.config(state=tk.NORMAL)
            self.img_label.config(state=tk.NORMAL)

        elif self.img_or_dir.get() == 'dir':
            self.img_name_entry.config(state=tk.DISABLED)
            self.img_button.config(state=tk.DISABLED)
            self.img_label.config(state=tk.DISABLED)
            self.dir_name_entry.config(state=tk.NORMAL)
            self.dir_button.config(state=tk.NORMAL)
            self.dir_label.config(state=tk.NORMAL)
        

    # open window with selceting direcory, next insert it into entry
    def select_dir(self):
        self.directory = filedialog.askdirectory()
        self.dir_name_entry.insert(0, self.directory)


    def select_photo(self):
        self.img_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("image files","*.jpg *.jpeg *.png"),("all files","*.*")))
        self.img_name_entry.insert(0, self.img_path)