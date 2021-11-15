def resize_image(img, new_width):
    img_width = img.width
    img_height = img.height
    prop = new_width / img_width
    new_height = int(img_height * prop)
    return img.resize((new_width, new_height))