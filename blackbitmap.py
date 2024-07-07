from PIL import Image

# Function to create a black bitmap image
def create_black_bitmap(width, height):
    # Create a new black image with the specified dimensions
    img = Image.new('RGB', (width, height), color='black')

    # Save the image as a bitmap
    img.save("black_image.bmp", format='BMP')

# Create a black bitmap image with dimensions 160x48 pixels
create_black_bitmap(160, 48)