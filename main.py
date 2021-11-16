from PIL import Image, ImageFont, ImageDraw
from os import listdir, path
from os.path import join
import tkinter as tk
from main_frame import MainFrame
from resize_img import resize_image
from save_img import save_image




class Watermarker:
    def __init__(self):
        self.root = tk.Tk()
        self.app = MainFrame(self.root)

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
    def resize_watermark(self, image_width):
        wm_width_prop = self.app.preview_frame.width_prop.get()
        current_wm_width = int(image_width * wm_width_prop / 100)
        current_watermark = resize_image(self.watermark, current_wm_width)
        return current_watermark


    def set_wm_opacity(self):
        self.watermark.putalpha(self.wm_op)


    def marking_with_photo(self):
        for img in self.images:
            photo = Image.open(join(self.dir, img)).convert('RGBA')
            image_width, image_height = photo.size
            cur_wm = self.resize_watermark(image_width)
            wm_width, wm_height = cur_wm.size
            wm_pos = (image_width - wm_width, image_height - wm_height)
            try:
                photo.paste(cur_wm, wm_pos, cur_wm)
            except ValueError:
                photo.paste(cur_wm, wm_pos)

            save_image(photo.convert("RGB"), self.saving_dir, img)


    def marking_with_text(self):
        for img in self.images:
            photo = Image.open(join(self.dir, img)).convert('RGBA')
            text_img = Image.new('RGBA', photo.size, (255,255,255,0))
            font = ImageFont.truetype("arial.ttf", 40)
            draw = ImageDraw.Draw(text_img)
            text = self.app.watermark_frame.text.get()
            draw.text(xy=(0, 0), text=text, font=font, fill=(255,255,255, self.wm_op))
            marked_img = Image.alpha_composite(photo, text_img).convert("RGB")
            save_image(marked_img, self.saving_dir, img)



    def main(self, *args):
        self.set_paths()
        self.wm_path = self.app.watermark_frame.img_path
        self.wm_op = self.app.preview_frame.opacity.get()
        wm_or_text = self.app.watermark_frame.text_or_img.get()
        if wm_or_text == 'img':
            self.watermark = Image.open(self.wm_path)
            self.set_wm_opacity()
            self.marking_with_photo()
        elif wm_or_text == 'text':
            self.marking_with_text()





wm = Watermarker()
wm.main()