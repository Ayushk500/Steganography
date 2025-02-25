# Secure Data Hiding in Images Using Steganography

## Introduction
This project demonstrates the use of steganography to securely hide and extract confidential messages within images. By leveraging advanced encryption techniques and a user-friendly graphical user interface (GUI), this project aims to provide an effective solution for secure data transmission while maintaining the integrity of the cover image.

## Features
- **Interactive and Responsive GUI**: A user-friendly interface created using `tkinter` that allows users to easily embed and extract secret messages.
- **Advanced Encryption**: Utilizes AES (128 Bit) encryption to secure the secret message before embedding it into the image.
- **Double Protection**: The secret message is first encrypted using a password and then hidden within the image.
- **Versatile**: Supports different image formats (PNG, JPG, JPEG).

## Technology Used
- **Libraries**: PIL, OS, Hashlib, Tkinter, filedialog, messagebox
- **Language**: Python 3
- **System Configuration**:
  - Operating System: Windows 10 or above
  - Processor: AMD 5500U
  - RAM: 16 GB 
  - Software: Visual Studio Code

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Ayushk500/Steganography.git
   ```

2. Navigate to the project directory:

```sh 
  cd Steganography
```

3. Install the required libraries:

```sh
pip install -r requirements.txt
```

## Usage
Running the Application

Run the GUI application:

```sh
  python gui.py
```

To Embed a Secret Message:

Select a cover image.
Enter the secret message and password.
Click "Embed Message" to generate the stego image.

To Extract a Hidden Message:

Select the encrypted image.
Enter the password used while encrypting (for decryption).
Click "Extract Message" to retrieve the secret message.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact Information
For any questions or suggestions, feel free to contact:

**Ayush Kant**

Email: [ayush06edu@gmail.com.com](mailto:ayush06edu@gmail.com)


## Future Scope

- **Advanced Encryption Methods:** 
  - Integrating more robust encryption methods like AES-256, AES-512, and RSA.

- **Multiple Cover File Types:** 
  - Enabling the selection of various types of cover files, such as music, video, PDF, and more.

- **Choice of Encryption Standards:** 
  - Providing users with options to choose between multiple encryption standards.

- **Hiding Different File Formats:** 
  - Expanding the capability to hide various file formats, including MP4 videos, audio files, and documents.

