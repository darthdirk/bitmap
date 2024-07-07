from PIL import Image


def get_image_resolution(image_path):
    # Open BMP image
    with Image.open(image_path) as img:
        # Get image size (width, height)
        width, height = img.size
        return width, height


if __name__ == "__main__":
    # Provide the path to your BMP image
    bmp_image_path = "example.bmp"

    # Get image resolution
    width, height = get_image_resolution(bmp_image_path)
    print(f"Image resolution: {width}x{height} pixels")
