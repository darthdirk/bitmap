from PIL import Image


def remove_metadata(image_path):
    # Open BMP image
    with Image.open(image_path) as img:
        # Copy image without metadata
        image_without_metadata = img.copy()
        image_without_metadata.info = {}

        # Save the image without metadata
        output_path = image_path.replace('.bmp', '_no_metadata.bmp')
        image_without_metadata.save(output_path)
        print(f"Image without metadata saved to: {output_path}")


if __name__ == "__main__":
    # Provide the path to your BMP image
    bmp_image_path = "~/file.bmp"

    # Remove metadata
    remove_metadata(bmp_image_path)
