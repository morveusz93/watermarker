from PIL import Image
from os import listdir, mkdir
from os.path import join, isfile


# name of directory where are all images
dir_name = 'images'
# saving images to the same direcotry but in special dir - 'marked'
saving_dir = join(dir_name, 'marked')
# opacity 0 = 0%, 255 = 100%
opacity = 30 

# path to watermark
wm = join('watermark', 'wm.jpg')
# size of watermark
wm_size = (100,100)
watermark = Image.open(wm)
watermark = watermark.resize(wm_size)
# put opacity
watermark.putalpha(opacity)

# create list of files in directory with images
images = [file for file in listdir(dir_name) if file.endswith(('.jpg', '.jpeg', '.png'))]

for img in images:
    image = Image.open(join(dir_name, img))
    # get size of image and watermark to calculate the position of watermark
    wm_width, wm_height = watermark.size
    image_width, image_height = image.size
    wm_pos = (image_width - wm_width, image_height - wm_height)
    # paste watermark into image
    # try: if there is opacity, we need to add mask - the third argument
    try:
        image.paste(watermark, wm_pos, watermark)
    # if there is'nt opacity paste will raise 'ValueError', then we simply paste watermark without mask
    except ValueError:
        image.paste(watermark, wm_pos)
    # save the image with watermark. 
    # if there is no directory created ('marked') it will raise except 'FileNotFoundError' then we will create the dir
    try:
        image.save(join(saving_dir, img))
    except FileNotFoundError:
        mkdir(saving_dir)
        image.save(join(saving_dir, img))
