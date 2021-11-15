from PIL import Image, ImageFont, ImageDraw
from os import listdir, path
from os.path import join
import tkinter as tk
from main_frame import MainFrame
from resize_img import resize_image
from save_img import save_image



# def marking_with_text(dir_name, images, text, saving_dir):
#     opacity = int(input("opacity: "))
#     for img in images:
#         photo = Image.open(join(dir_name, img)).convert('RGBA')
#         text_img = Image.new('RGBA', photo.size, (255,255,255,0))
#         font = ImageFont.truetype("arial.ttf", 40)
#         draw = ImageDraw.Draw(text_img)
#         draw.text(xy=(0, 0), text=text, font=font, fill=(255,255,255,opacity))
#         marked_img = Image.alpha_composite(photo, text_img).convert('RGB')
#         save_image(marked_img, saving_dir, img)



class Watermarker:
    def __init__(self):
        self.root = tk.Tk()
        self.app = MainFrame(self.root)

        # bind ENTER key 
        self.app.confirm_button.config(command=self.main)



        self.app.mainloop()

    def set_paths(self):
        img_or_dir = self.app.photos_frame.img_or_dir.get()
        if img_or_dir == "dir":
            self.dir = self.app.photos_frame.directory
            self.saving_dir = join(self.dir, 'marked')
            self.images = [file for file in listdir(self.dir) if file.endswith(('.jpg', '.jpeg', '.png'))]

        elif img_or_dir == "img":
            img_path = self.app.photos_frame.img_path
            self.dir = path.dirname(img_path)
            self.saving_dir = join(dir, 'marked')
            self.images = [path.basename(img_path)]


    # size of watermark
    def resize_watermark(self):
        self.wm_width = self.app.preview_frame.width.get()
        self.watermark = resize_image(self.watermark, self.wm_width)


    def set_wm_opacity(self):
        self.wm_op = self.app.preview_frame.opacity.get()
        self.watermark.putalpha(self.wm_op)


    def main(self, *args):
        self.set_paths()

        self.wm_path = self.app.watermark_frame.img_path
        self.watermark = Image.open(self.wm_path)
        self.resize_watermark()
        self.set_wm_opacity()


        for img in self.images:
            photo = Image.open(join(self.dir, img))
            width, height = self.watermark.size
            image_width, image_height = photo.size
            wm_pos = (image_width - width, image_height - height)
            try:
                photo.paste(self.watermark, wm_pos, self.watermark)
            except ValueError:
                photo.paste(self.watermark, wm_pos)
            save_image(photo, self.saving_dir, img)




wm = Watermarker()
wm.main()