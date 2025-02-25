from PIL import Image
import hashlib
import os

def string_to_bin(text):
    """Convert a string into binary representation."""
    return ''.join(format(ord(c), '08b') for c in text)

def embed_message(image_path, message, password, output_image_path):
    try:
        # Check if image file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Cover image '{image_path}' not found.")
        
        # Open the image
        image = Image.open(image_path)
        pixels = image.load()

        # Convert message to binary and append a delimiter (to mark the end of the message)
        binary_message = string_to_bin(message) + '1111111111111110'

        # Generate a hash from the password (for later decryption)
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        message_index = 0
        for y in range(image.height):
            for x in range(image.width):
                pixel = list(pixels[x, y])

                for i in range(3):  # RGB channels
                    if message_index < len(binary_message):
                        # Modify the least significant bit of the pixel
                        pixel[i] = pixel[i] & 0xFE | int(binary_message[message_index])
                        message_index += 1

                # Update the pixel with the new value
                pixels[x, y] = tuple(pixel)

                # If all message bits are embedded, stop
                if message_index >= len(binary_message):
                    break
            else:
                continue
            break

        # Save the new image with the hidden message
        image.save(output_image_path)
        return output_image_path  # Return the path of the saved stego image

    except FileNotFoundError as fnf_error:
        return fnf_error
    except Exception as e:
        return f"An error occurred: {e}"