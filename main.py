from PIL import Image, ImageFont, ImageDraw
from os import listdir, mkdir
from os.path import join

import tkinter as tk
from tkinter import ttk



def marking(dir_name, images, watermark, saving_dir):
    for img in images:
        photo = Image.open(join(dir_name, img))
        wm_width, wm_height = watermark.size
        image_width, image_height = photo.size
        wm_pos = (image_width - wm_width, image_height - wm_height)
        try:
            photo.paste(watermark, wm_pos, watermark)
        except ValueError:
            photo.paste(watermark, wm_pos)
        save_image(photo, saving_dir, img)




def marking_with_text(dir_name, images, text, saving_dir):
    opacity = int(input("opacity: "))
    for img in images:
        photo = Image.open(join(dir_name, img)).convert('RGBA')
        text_img = Image.new('RGBA', photo.size, (255,255,255,0))
        font = ImageFont.truetype("arial.ttf", 40)
        draw = ImageDraw.Draw(text_img)
        draw.text(xy=(0, 0), text=text, font=font, fill=(255,255,255,opacity))
        marked_img = Image.alpha_composite(photo, text_img).convert('RGB')
        save_image(marked_img, saving_dir, img)


def save_image(img, saving_dir, img_name):
    try:
        img.save(join(saving_dir, img_name))
    except FileNotFoundError:
        mkdir(saving_dir)
        img.save(join(saving_dir, img_name))



def main():
    #---------------------------- images ----------------------------#
    print("Name of dir with images: ")
    dir_name = input().lower()
    saving_dir = join(dir_name, 'marked')
    images = [file for file in listdir(dir_name) if file.endswith(('.jpg', '.jpeg', '.png'))]

    print("watermark with \n 1. Image \n2. Text")
    users_choice = int(input())
    if users_choice == 1:
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

    elif users_choice == 2:
        text = input("text to watermark: ")
        marking_with_text(dir_name, images, text, saving_dir)




def mark(*args):

    dir = dir_name.get()
    wm = wm_name.get()
    width = wm_width.get()
    height = wm_height.get()
    op = opacity.get()

    images = [file for file in listdir(dir) if file.endswith(('.jpg', '.jpeg', '.png'))]
    watermark = Image.open(wm)
    watermark = watermark.resize((width, height))
    watermark.putalpha(op)
    saving_dir = join(dir, 'marked')
    for img in images:
        photo = Image.open(join(dir, img))
        width, height = watermark.size
        image_width, image_height = photo.size
        wm_pos = (image_width - width, image_height - height)
        try:
            photo.paste(watermark, wm_pos, watermark)
        except ValueError:
            photo.paste(watermark, wm_pos)
        save_image(photo, saving_dir, img)



window = tk.Tk()
window.title('Watermarker')
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)
mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=('N, W, E, S'))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)


ttk.Label(mainframe, text="Folder name").grid(column=0, row=1, sticky='W')
dir_name = tk.StringVar()
dir_name_entry = ttk.Entry(mainframe, width=15, textvariable=dir_name)
dir_name_entry.grid(column=1, row=1, sticky=('W, E'))

ttk.Label(mainframe, text="watermark name").grid(column=0, row=2, sticky='W')
wm_name = tk.StringVar()
wm_name_entry = ttk.Entry(mainframe, width=15, textvariable=wm_name)
wm_name_entry.grid(column=1, row=2, sticky=('W, E'))

ttk.Label(mainframe, text="watermark's width: ").grid(column=0, row=3, sticky='W')
wm_width = tk.IntVar()
wm_width_entry = ttk.Entry(mainframe, width=5, textvariable=wm_width)
wm_width_entry.grid(column=1, row=3, sticky=('W, E'))

ttk.Label(mainframe, text="watermark's height: ").grid(column=0, row=4, sticky='W')
wm_height = tk.IntVar()
wm_height_entry = ttk.Entry(mainframe, width=5, textvariable=wm_height)
wm_height_entry.grid(column=1, row=4, sticky=('W, E'))

ttk.Label(mainframe, text="opacity: ").grid(column=0, row=5, sticky='W')
opacity = tk.IntVar()
opacity_entry = ttk.Entry(mainframe, width=5, textvariable=opacity)
opacity_entry.grid(column=1, row=5, sticky=('W, E'))

ttk.Button(text="Do it!", command=mark).grid(column=3, row=6, sticky=('S, E'))


window.bind("<Return>", mark)
window.mainloop()
