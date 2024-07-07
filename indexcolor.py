from PIL import Image


def convert_to_indexed_color(image_path):
    # Open BMP image
    with Image.open(image_path) as img:
        # Convert to indexed color mode
        img_indexed = img.convert("P", palette=Image.ADAPTIVE)

        # Save the converted image
        output_path = image_path.replace('.bmp', '_indexed_color.bmp')
        img_indexed.save(output_path)
        print(f"Image converted to indexed color saved to: {output_path}")


if __name__ == "__main__":
    # Provide the path to your BMP image
    bmp_image_path = "~/file.bmp"

    # Convert to indexed color
    convert_to_indexed_color(bmp_image_path)
