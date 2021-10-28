from PIL import Image, ImageFont, ImageDraw
from os import listdir, mkdir
from os.path import join




def marking(dir_name, images, watermark, saving_dir):
    for img in images:
        image = Image.open(join(dir_name, img))
        wm_width, wm_height = watermark.size
        image_width, image_height = image.size
        wm_pos = (image_width - wm_width, image_height - wm_height)
        try:
            image.paste(watermark, wm_pos, watermark)
        except ValueError:
            image.paste(watermark, wm_pos)
        try:
            image.save(join(saving_dir, img))
        except FileNotFoundError:
            mkdir(saving_dir)
            image.save(join(saving_dir, img))



def marking_with_text(dir_name, images, saving_dir):
    for img in images:
        image = Image.open(join('images', img)).convert('RGBA')
        text_img = Image.new('RGBA', image.size, (255,255,255,0))
        font = ImageFont.truetype("arial.ttf", 40)
        draw = ImageDraw.Draw(text_img)
        draw.text(xy=(0, 0), text="SIEMA", font=font, fill=(255,255,255,255))
        marked_img = Image.alpha_composite(image, text_img).convert('RGB')

        try:
            marked_img.save(join(saving_dir, img))
        except FileNotFoundError:
            mkdir(saving_dir)
            marked_img.save(join(saving_dir, img))





def main():
    #---------------------------- images ----------------------------#
    print("Name of dir with images: ")
    dir_name = input().lower()
    saving_dir = join(dir_name, 'marked')
    images = [file for file in listdir(dir_name) if file.endswith(('.jpg', '.jpeg', '.png'))]

    #---------------------------- watermark ----------------------------#
    print("\nfilename of your watermark:")
    wm = input().lower()
    watermark = Image.open(wm)

    # opacity 0 = 0%, 255 = 100%
    print("opacity of watermark(0-255): ")
    opacity = int(input())
    watermark.putalpha(opacity)

    print("size of your watermark: ")
    wm_width, wm_height = input().split()
    wm_width, wm_height = int(wm_width), int(wm_height)
    watermark = watermark.resize((wm_width, wm_height))

    marking(dir_name, images, watermark, saving_dir)


if __name__ == '__main__':
    main()