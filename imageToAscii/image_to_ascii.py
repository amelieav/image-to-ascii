from PIL import Image

ASCII_CHARS = '@%#+=-. '

def map_pixel_to_ascii(pixel_value):
    num_chars = len(ASCII_CHARS)
    return ASCII_CHARS[int((pixel_value / 255) * (num_chars - 1))]

def convert_image_to_grayscale(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    return grayscale_image

def scale_image(image, width, height):
    return image.resize((width, height))

def convert_to_ascii_art(image_path, output_text_file, scale_width=50, scale_height=20):
    grayscale_image = convert_image_to_grayscale(image_path)
    scaled_image = scale_image(grayscale_image, scale_width, scale_height)
    width, height = scaled_image.size
    ascii_art = ""

    for y in range(height):
        for x in range(width):
            pixel_value = scaled_image.getpixel((x, y))
            ascii_char = map_pixel_to_ascii(pixel_value)
            ascii_art += ascii_char
        ascii_art += '\n'

    with open(output_text_file, 'w') as text_file:
        text_file.write(ascii_art)
