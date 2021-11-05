import tkinter as tk
from watermark_picker import WatermarkPickerFrame
from photos_picker import PhotosPickerFrame
from preview import PreviewFrame


# create main frame, root(parent) is the main window.
class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.config(padx=30, pady=30)
        self.config(padx=30, pady=30)
        self.root.title("WaterMarker")
        self.root.geometry('1100x700')

        self.photos_frame = PhotosPickerFrame(self)
        self.watermark_frame = WatermarkPickerFrame(self)
        self.preview_frame = PreviewFrame(self)

        self.photos_frame.grid(column=0, row=0, sticky="NW")
        self.watermark_frame.grid(column=0, row=1, sticky="NW")
        self.preview_frame.grid(column=1, row=0, rowspan=2, sticky="NW")
        self.grid(column=0, row=0)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(parent=root)

    app.mainloop()