from PIL import Image


# Function to create a transparent bitmap
def create_transparent_bitmap(filename, width, height):
    # Create a new RGBA image with transparent background
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # Convert the image to RGB mode (since bitmap does not support alpha channel)
    img = img.convert('RGB')

    # Save the image as a bitmap
    img.save(filename, format='BMP')


# Example usage
create_transparent_bitmap("transparent.bmp", 100, 100)
