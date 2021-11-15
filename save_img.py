from os import mkdir
from os.path import join

def save_image(img, saving_dir, img_name):
    try:
        img.save(join(saving_dir, img_name))
    except FileNotFoundError:
        mkdir(saving_dir)
        img.save(join(saving_dir, img_name))