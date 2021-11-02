import tkinter as tk
from tkinter import filedialog
from tkinter.constants import DISABLED


# create main frame, root(parent) is the main window.
class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.config(padx=30, pady=30)
        self.config(padx=30, pady=30)
        self.root.title("WaterMarker")
        self.root.geometry('600x300')

        self.photos_picker = PhotosPicker(self)
        self.watermark_picker = WatermarkPicker(self)

        self.photos_picker.grid(column=0, row=0)
        self.watermark_picker.grid(column=0, row=1)
        self.grid(column=0, row=0)


# create frame where the folder with photos will be selected
class PhotosPicker(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Choose a directory or a single photo"
        tk.LabelFrame.__init__(self, master=root, text=frame_label, padx=20, pady=20, *args, **kwargs)
        
        self.img_or_dir = tk.StringVar()
        self.img_or_dir.set("dir")

        # choose directory
        self.radio_dir = tk.Radiobutton(self, variable=self.img_or_dir, value="dir", command=self.switch_img_or_dir)
        self.radio_dir.grid(column=0, row=2)
        self.directory = tk.StringVar()
        self.dir_name_entry = tk.Entry(self, width=50, textvariable=self.directory)
        self.dir_name_entry.grid(column=1, row=2)
        self.dir_button = tk.Button(self, text='Pick folder', command=self.select_dir)
        self.dir_button.grid(column=2, row=2)

        # choose single photo
        self.radio_img = tk.Radiobutton(self, variable=self.img_or_dir, value="img", command=self.switch_img_or_dir)
        self.radio_img.grid(column=0, row=3)
        self.img_path = tk.StringVar()
        self.img_name_entry = tk.Entry(self, width=50, textvariable=self.img_path, state=tk.DISABLED)
        self.img_name_entry.grid(column=1, row=3)
        self.img_button = tk.Button(self, text='Pick single photo', command=self.select_photo, state=tk.DISABLED)
        self.img_button.grid(column=2, row=3)


    def switch_img_or_dir(self):        
        if self.img_or_dir.get() == 'img':
            self.dir_name_entry.config(state=tk.DISABLED)
            self.dir_button.config(state=tk.DISABLED)
            self.img_name_entry.config(state=tk.NORMAL)
            self.img_button.config(state=tk.NORMAL)

        elif self.img_or_dir.get() == 'dir':
            self.img_name_entry.config(state=tk.DISABLED)
            self.img_button.config(state=tk.DISABLED)
            self.dir_name_entry.config(state=tk.NORMAL)
            self.dir_button.config(state=tk.NORMAL)
        

    # open window with selceting direcory, next insert it into entry
    def select_dir(self):
        self.directory = filedialog.askdirectory()
        self.dir_name_entry.insert(0, self.directory)


    def select_photo(self):
        self.img_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("image files","*.jpg *.jpeg *.png"),("all files","*.*")))
        self.img_name_entry.insert(0, self.img_path)



class WatermarkPicker(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Choose a watermark"
        tk.LabelFrame.__init__(self, master=root, text=frame_label, padx=20, pady=20, *args, **kwargs)

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
        self.img_button = tk.Button(self, text='Pick single photo', command=self.select_photo, state=tk.DISABLED)
        self.img_button.grid(column=2, row=3)



    def switch_text_or_img(self):        
        if self.text_or_img.get() == 'text':
            self.img_name_entry.config(state=tk.DISABLED)
            self.img_button.config(state=tk.DISABLED)
            self.text_entry.config(state=tk.NORMAL)
            self.text_label.config(state=tk.NORMAL)

        elif self.text_or_img.get() == 'img':
            self.text_entry.config(state=tk.DISABLED)
            self.text_label.config(state=DISABLED)
            self.img_name_entry.config(state=tk.NORMAL)
            self.img_button.config(state=tk.NORMAL)
        

    # open window with selceting direcory, next insert it into entry
    def select_photo(self):
        self.img_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("image files","*.jpg *.jpeg *.png"),("all files","*.*")))
        self.img_name_entry.insert(0, self.img_path)


        self.grid(column=1, row=1)











if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(parent=root)

    app.mainloop()