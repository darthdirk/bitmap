from PIL import Image


def resize_image(image_path, new_width, new_height):
    # Open BMP image
    with Image.open(image_path) as img:
        # Resize image
        resized_img = img.resize((new_width, new_height))

        # Save resized image
        output_path = image_path.replace('.bmp', '_resized.bmp')
        resized_img.save(output_path)
        print(f"Resized image saved to: {output_path}")


if __name__ == "__main__":
    # Provide the path to your BMP image
    bmp_image_path = "example.bmp"

    # Specify the new width and height
    new_width = 640  # New width in pixels
    new_height = 480  # New height in pixels

    # Resize image
    resize_image(bmp_image_path, new_width, new_height)
