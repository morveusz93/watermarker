import tkinter as tk

from .photos_picker import PhotosPickerFrame
from .preview import PreviewFrame
from .watermark_picker import WatermarkPickerFrame


# create main frame, root(parent) is the main window.
class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.config(padx=30, pady=30)
        self.config(padx=30, pady=30)
        self.root.title("WaterMarker")
        self.root.geometry("2400x1200")

        # all frames
        self.photos_frame = PhotosPickerFrame(self)
        self.watermark_frame = WatermarkPickerFrame(self)
        self.preview_frame = PreviewFrame(self)

        # set them into main frame
        self.photos_frame.grid(column=0, row=0, sticky="NW")
        self.watermark_frame.grid(column=0, row=1, sticky="NW")
        self.preview_frame.grid(column=1, row=0, rowspan=2, sticky="NW")
        self.grid(column=0, row=0)

        # create confirm button
        self.confirm_button = tk.Button(self.root, text="Confirm")
        self.confirm_button.grid(column=0, row=1, sticky="SE")
