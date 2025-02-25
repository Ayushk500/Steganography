import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import embed_message  # assuming encryption.py has the embed_message function
from decryption import extract_message  # assuming decryption.py has the extract_message function
import os


class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography GUI")
        self.root.geometry("1024x800")

        # Encryption Section
        self.encrypt_label = tk.Label(root, text="Embed Message", font=("Arial", 14))
        self.encrypt_label.pack(pady=10)

        self.cover_image_label = tk.Label(root, text="Cover Image:")
        self.cover_image_label.pack()
        self.cover_image_entry = tk.Entry(root, width=40)
        self.cover_image_entry.pack(pady=5)
        self.cover_image_button = tk.Button(root, text="Browse", command=self.load_cover_image)
        self.cover_image_button.pack(pady=5)

        self.message_label = tk.Label(root, text="Secret Message:")
        self.message_label.pack()
        self.message_entry = tk.Entry(root, width=40)
        self.message_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, width=40, show="*")
        self.password_entry.pack(pady=5)

        self.encrypt_button = tk.Button(root, text="Embed Message", command=self.embed_message)
        self.encrypt_button.pack(pady=10)

        self.encrypted_image_label = tk.Label(root, text="Encrypted Image:")
        self.encrypted_image_label.pack()
        self.encrypted_image_entry = tk.Entry(root, width=40)
        self.encrypted_image_entry.pack(pady=5)

        # Decryption Section
        self.decrypt_label = tk.Label(root, text="Extract Message", font=("Arial", 14))
        self.decrypt_label.pack(pady=10)

        self.stego_image_label = tk.Label(root, text="Stego Image:")
        self.stego_image_label.pack()
        self.stego_image_entry = tk.Entry(root, width=40)
        self.stego_image_entry.pack(pady=5)
        self.stego_image_button = tk.Button(root, text="Browse", command=self.load_stego_image)
        self.stego_image_button.pack(pady=5)

        self.decrypted_message_label = tk.Label(root, text="Decrypted Message:")
        self.decrypted_message_label.pack()
        self.decrypted_message_display = tk.Label(root, text="", width=40, height=4, relief="solid")
        self.decrypted_message_display.pack(pady=5)

        self.password_label_decrypt = tk.Label(root, text="Password (for Decryption):")
        self.password_label_decrypt.pack()
        self.password_entry_decrypt = tk.Entry(root, width=40, show="*")
        self.password_entry_decrypt.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Extract Message", command=self.extract_message)
        self.decrypt_button.pack(pady=10)

    def load_cover_image(self):
        image_path = filedialog.askopenfilename(title="Select Cover Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            self.cover_image_entry.delete(0, tk.END)
            self.cover_image_entry.insert(0, image_path)

    def load_stego_image(self):
        image_path = filedialog.askopenfilename(title="Select Stego Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            self.stego_image_entry.delete(0, tk.END)
            self.stego_image_entry.insert(0, image_path)

    def embed_message(self):
        try:
            cover_image = self.cover_image_entry.get()
            secret_message = self.message_entry.get()
            password = self.password_entry.get()

            if not cover_image or not secret_message or not password:
                raise ValueError("All fields must be filled!")

            output_image_path = "stego_image.png"  # Save the encrypted image to a default file
            result = embed_message(cover_image, secret_message, password, output_image_path)

            if "An error occurred" in result:
                messagebox.showerror("Error", result)
            else:
                self.encrypted_image_entry.delete(0, tk.END)
                self.encrypted_image_entry.insert(0, result)
                messagebox.showinfo("Success", f"Message successfully embedded! Saved as {result}")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def extract_message(self):
        try:
            stego_image = self.stego_image_entry.get()
            password = self.password_entry_decrypt.get()

            if not stego_image or not password:
                raise ValueError("All fields must be filled!")

            secret_message = extract_message(stego_image, password)

            if "An error occurred" in secret_message:
                messagebox.showerror("Error", secret_message)
            else:
                self.decrypted_message_display.config(text=secret_message)
                messagebox.showinfo("Success", "Message successfully extracted!")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


def run_gui():
    root = tk.Tk()
    app = StegoApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()

