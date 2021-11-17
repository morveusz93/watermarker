from os import mkdir
from os.path import join

def save_image(img, saving_dir, img_name):
    try:
        img.save(join(saving_dir, img_name))
    except FileNotFoundError:
        mkdir(saving_dir)
        img.save(join(saving_dir, img_name))



def resize_image(img, new_width):
    img_width = img.width
    img_height = img.height
    prop = new_width / img_width
    new_height = int(img_height * prop)
    return img.resize((new_width, new_height))