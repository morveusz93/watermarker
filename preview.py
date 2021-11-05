import tkinter as tk
from PIL import ImageTk, Image as Pil_image


class PreviewFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        self.root = parent
        frame_label = "Preview"
        tk.LabelFrame.__init__(self, master=self.root, text=frame_label, padx=20, pady=20, *args, **kwargs)




