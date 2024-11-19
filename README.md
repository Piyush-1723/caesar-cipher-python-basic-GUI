# Caesar Cipher GUI Application

A modern, user-friendly graphical user interface (GUI) application for encrypting and decrypting text using the Caesar Cipher technique. This application is built using Python and PyQt5, offering various features such as theme toggling, interactive styles, and enhanced usability options.

## Features

- **Encryption & Decryption**: Encrypt or decrypt text using a customizable shift key.
- **Brute Force Mode**: Decrypt text by attempting all possible shifts.
- **Theme Toggling**: Switch between Light and Dark modes with an animated toggle.
- **Interactive UI**:
  - Glow effect for input fields and radio buttons when selected.
  - Modern styled buttons with hover effects.
  - Auto-resizing input text field for lengthy text.
- **Modern Output Display**:
  - Displays results in an easy-to-read format.
  - Scrollbar styled for a sleek, modern look.
- **Error Handling**: Provides warnings for invalid shift key input.

## Screenshots
_(Add screenshots here to showcase the application's interface and features.)_

## Requirements

- Python 3.7 or later
- PyQt5
- qtwidgets

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Piyush-1723/caesar-cipher-python-basic-GUI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd caesar-cipher-python-basic-GUI
   ```
3. Install the required dependencies:
   ```bash
   pip install PyQt5 qtwidgets
   ```

## Usage

1. Run the application:
   ```bash
   python caesar_app.py
   ```
2. Use the input field to enter the text you want to encrypt or decrypt.
3. Choose an action:
   - Encrypt with Key
   - Decrypt with Key
   - Brute Force Decrypt
4. If applicable, enter a shift key and select the shift direction (Forward or Reverse).
5. Click "Process" to view the results in the output area.
6. Use the theme toggle to switch between Light and Dark modes.

## Future Enhancements

- Support for additional encryption techniques.
- Save and load text files for encryption and decryption.
- Enhanced animations and font customization.
- Unit tests for improved reliability.

## Contributing

Contributions are welcome! If you'd like to improve this application, feel free to fork the repository, make your changes, and submit a pull request.
