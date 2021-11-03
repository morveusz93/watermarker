import tkinter as tk
from tkinter import filedialog
from watermark_picker import WatermarkPicker
from photos_picker import PhotosPicker


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


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(parent=root)

    app.mainloop()