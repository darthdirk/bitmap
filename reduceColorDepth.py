from PIL import Image


def reduce_color_depth(image_path, colors=4):
    # Open BMP image
    with Image.open(image_path) as img:
        # Reduce color depth
        img = img.quantize(colors=colors)

        # Save modified image
        output_path = image_path.replace('.bmp', '_reduced.bmp')
        img.save(output_path)
        print(f"Image with reduced color depth saved to: {output_path}")


if __name__ == "__main__":
    # Provide the path to your BMP image
    bmp_image_path = "~/file.bmp"

    # Reduce color depth (default: 256 colors)
    reduce_color_depth(bmp_image_path)
