from PIL import Image
import hashlib
import os

def bin_to_string(binary_data):
    """Convert binary data back into a string."""
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def extract_message(image_path, password):
    try:
        # Check if image file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Stego image '{image_path}' not found.")
        
        # Open the image
        image = Image.open(image_path)
        pixels = image.load()

        binary_message = ''
        for y in range(image.height):
            for x in range(image.width):
                pixel = list(pixels[x, y])

                for i in range(3):  # RGB channels
                    binary_message += str(pixel[i] & 1)

        # Extract the message bits and remove the delimiter
        message = bin_to_string(binary_message)
        message = message.split('ÿ')[0]  # Stop at the delimiter

        return message

    except FileNotFoundError as fnf_error:
        return fnf_error
    except Exception as e:
        return f"An error occurred during extraction: {e}"