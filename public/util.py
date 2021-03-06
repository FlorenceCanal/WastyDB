from PIL import Image, ImageFilter


def create_image_placeholder(img):
    placeholder = Image.open(img)
    (width, height) = placeholder.size
    new_size = (width // 30, height // 30)
    placeholder = placeholder.resize(new_size, Image.ANTIALIAS)
    placeholder = placeholder.filter(ImageFilter.BLUR)
    return placeholder
