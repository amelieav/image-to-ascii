# ASCII Art Converter using PIL
This Python script allows you to convert images into ASCII art using the Python Imaging Library (PIL). You can customize the ASCII characters used for the conversion to achieve various levels of detail in your ASCII art.

## Prerequisites
Make sure you have the PIL library installed. You can install it with pip:

`pip install pillow`

## Usage
Define the ASCII characters you want to use for the conversion. The characters should be arranged from the darkest to the lightest, as they will represent varying shades in the image. You can change the ASCII_CHARS variable to suit your preferences.

Set the `input_image_path` variable to point to your image.

Choose the desired output file name and set it in the `output_text_file` variable. This is where your ASCII art will be saved.

Run the script.


## Notes

Icon-type images tend to produce better results compared to digital images and photographs due to their simplicity.


## Version History

v1.0 - Initial release
// TODO v1.1 - patch problem with transparent backgrounds in pngs