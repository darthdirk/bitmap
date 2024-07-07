from PIL import Image


def get_color_depth(image_path):
    # Open image
    with Image.open(image_path) as img:
        # Convert to 'RGB' mode if image is not in 'RGB'
        img = img.convert('RGB')

        # Get unique colors
        colors = img.getcolors()

        # Return the number of unique colors
        return len(colors)


if __name__ == "__main__":
    # Provide the path to your image
    image_path = "example.bmp"

    # Get color depth
    depth = get_color_depth(image_path)
    print(f"Color depth of the image: {depth} colors")
