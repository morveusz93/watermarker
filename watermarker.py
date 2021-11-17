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
            current_wm = self.resize_watermark(photo.width)
            wm_pos = self.get_position_of_wm(img=photo, wm=current_wm)
            try:
                photo.paste(current_wm, wm_pos, current_wm)
            except ValueError:
                photo.paste(current_wm, wm_pos)

            save_image(photo.convert("RGB"), self.saving_dir, img)


    def get_position_of_wm(self, img, wm):
        img_width, img_height = img.size
        wm_width, wm_height = wm.size
        if self.wm_position == 'down-right':
            wm_pos = (img_width - wm_width, img_height - wm_height)
        elif self.wm_position == 'down-left':
            wm_pos = (0, img_height - wm_height)
        elif self.wm_position == 'top-left':
            wm_pos = (0, 0)
        elif self.wm_position == 'top-right':
            wm_pos = (img_width - wm_width, 0)
        elif self.wm_position == 'center':
            wm_pos = (img_width // 2 - wm_width // 2, img_height // 2 - wm_height // 2)
        return wm_pos



    def marking_with_text(self):
        font_family = 'arial.ttf'
        font_color = self.app.watermark_frame.font_color.get()[1:-1].split(', ')
        for img in self.images:
            photo = Image.open(join(self.dir, img)).convert('RGBA')
            text_img = Image.new('RGBA', photo.size, (255,255,255,0))
            # set font size
            font_size = int(self.app.preview_frame.width_prop.get() / 100 * photo.height)
            font = ImageFont.truetype(font_family, font_size)
            draw = ImageDraw.Draw(text_img)
            text = self.app.watermark_frame.text.get()
            wm_pos = self.get_position_of_wm(img=photo, wm=draw)
            draw.text(xy=(0,0), text=text, font=font, fill=(int(font_color[0]), int(font_color[1]), int(font_color[2]), self.wm_op))
            marked_img = Image.alpha_composite(photo, text_img).convert("RGB")
            save_image(marked_img, self.saving_dir, img)



    def main(self, *args):
        self.set_paths()
        self.wm_path = self.app.watermark_frame.img_path
        self.wm_op = self.app.preview_frame.opacity.get()
        wm_or_text = self.app.watermark_frame.text_or_img.get()
        self.wm_position = self.app.preview_frame.position_entry.selection_get()
        

        if wm_or_text == 'img':
            self.watermark = Image.open(self.wm_path)
            self.set_wm_opacity()
            self.marking_with_photo()
        elif wm_or_text == 'text':
            self.marking_with_text()