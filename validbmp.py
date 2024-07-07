import os


def is_valid_bmp(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return False

    # Check if the file has .bmp extension
    if not file_path.lower().endswith('.bmp'):
        print("Error: File is not a BMP file.")
        return False

    # Check if the file size is at least 54 bytes (minimum size for BMP header)
    if os.path.getsize(file_path) < 54:
        print("Error: File is too small to be a BMP file.")
        return False

    # Check if the first two bytes are 'BM' (signature for BMP file)
    with open(file_path, 'rb') as f:
        signature = f.read(2)
        if signature != b'BM':
            print("Error: File signature does not match BMP format.")
            return False

    return True


def save_as_bmp(image_data, output_file):
    with open(output_file, 'wb') as f:
        f.write(image_data)


input_file = '~/inputfile.bmp'
output_file = '~outputfile.bmp'

if is_valid_bmp(input_file):
    with open(input_file, 'rb') as f:
        image_data = f.read()

    save_as_bmp(image_data, output_file)
    print(f"File saved as '{output_file}'.")
else:
    print("File could not be saved as BMP.")
