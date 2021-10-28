from PIL import Image
from os import listdir, mkdir
from os.path import join




def marking(dir_name, images, watermark, saving_dir):
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



def main():
    #---------------------------- images ----------------------------#
    print("Name of dir with images: ")
    dir_name = input().lower()
    saving_dir = join(dir_name, 'marked')
    # create list of files in directory with images
    images = [file for file in listdir(dir_name) if file.endswith(('.jpg', '.jpeg', '.png'))]

    #---------------------------- watermark ----------------------------#
    print("\nfilename of your watermark:")
    # path to watermark
    wm = input().lower()
    watermark = Image.open(wm)

    # opacity 0 = 0%, 255 = 100%
    print("opacity of watermark(0-255): ")
    opacity = int(input())
    watermark.putalpha(opacity)

    # size of watermark
    print("size of your watermark: ")
    wm_width, wm_height = input().split()
    wm_width, wm_height = int(wm_width), int(wm_height)
    watermark = watermark.resize((wm_width, wm_height))

    marking(dir_name, images, watermark, saving_dir)


if __name__ == '__main__':
    main()