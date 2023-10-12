"""
This is a script using PIL (https://pillow.readthedocs.io/en/stable/) to convert an image to ASCII art.

You can choose which characters you would like your ASCII art to be made of by changing the ASCII_CHARS variable. Just be sure to order it with the "darkest" characters first, and the "lightest" characters last.

Icon type images > digital images >> photographs (in terms of quality of ASCII art)

"""

from PIL import Image # image processor library

# darkest to lightest
ASCII_CHARS = '@%#+=-. '

# map a grayscale value to an ASCII character
def map_pixel_to_ascii(pixel_value):
    num_chars = len(ASCII_CHARS)
    return ASCII_CHARS[int((pixel_value / 255) * (num_chars - 1))]

# convert an image to grayscale
def convert_image_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    return grayscale_image

# scale down a grayscale image to 16x16 pixels, this is to reduce the number of pixels to process individually
def scale_image(image, width, height):
    return image.resize((width, height))

# convert the resized grayscale image to ASCII art and save it to a text file
def convert_to_ascii_art(image_path, output_text_file):
    grayscale_image = convert_image_to_grayscale(image_path)
    scaled_image = scale_image(grayscale_image, 50, 20) # adjust this if your ascii art seems too squished or stretched
    width, height = scaled_image.size
    ascii_art = ""

    # mapping part
    for y in range(height):
        for x in range(width):
            pixel_value = scaled_image.getpixel((x, y))
            ascii_char = map_pixel_to_ascii(pixel_value)
            ascii_art += ascii_char
        ascii_art += '\n'

    # file path to output
    with open(output_text_file, 'w') as text_file:
        text_file.write(ascii_art)

if __name__ == '__main__':
    input_image_path = 'icon.jpg'
    # input_image_path = 'digital.png'
    # input_image_path = 'photo.png'

    output_text_file = 'output_art.txt'
    convert_to_ascii_art(input_image_path, output_text_file)
