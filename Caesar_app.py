import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QRadioButton, QButtonGroup, QMessageBox
from PyQt5.QtCore import Qt
from qtwidgets import AnimatedToggle
from PyQt5 import QtGui

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, text):
        result = ""
        for ch in text:
            if ch.isupper():
                result += chr((ord(ch) + self.shift - ord('A')) % 26 + ord('A'))
            elif ch.islower():
                result += chr((ord(ch) + self.shift - ord('a')) % 26 + ord('a'))
            else:
                result += ch
        return result

    def decrypt(self, text):
        result = ""
        for ch in text:
            if ch.isupper():
                result += chr((ord(ch) - self.shift - ord('A')) % 26 + ord('A'))
            elif ch.islower():
                result += chr((ord(ch) - self.shift - ord('a')) % 26 + ord('a'))
            else:
                result += ch
        return result

class CaesarCipherGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caesar Cipher")
        self.setGeometry(100, 100, 500, 400)  # Increased window size

        # Main Layout
        layout = QVBoxLayout()

        # Top Layout for Theme Indicator and Toggle
        top_layout = QHBoxLayout()
        
        # Theme Indicator
        self.theme_label = QLabel("Light Mode")
        self.theme_label.setAlignment(Qt.AlignLeft)
        top_layout.addWidget(self.theme_label)

        # Dark/Light Mode Toggle
        self.theme_toggle = AnimatedToggle()
        self.theme_toggle.setChecked(False)  # Start in Light Mode
        self.theme_toggle.stateChanged.connect(self.toggle_theme)
        top_layout.addWidget(self.theme_toggle, alignment=Qt.AlignRight)

        layout.addLayout(top_layout)

        # Text Entry
        self.text_label = QLabel("Enter text:")
        layout.addWidget(self.text_label)
        self.text_entry = QLineEdit()
        self.text_entry.setStyleSheet("border: 1px solid black; padding: 5px;")  # Initial style
        layout.addWidget(self.text_entry)

        # Process Selection Radio Buttons
        self.option_label = QLabel("Choose action:")
        layout.addWidget(self.option_label)
        action_layout = QHBoxLayout()
        self.encrypt_radio = QRadioButton("Encrypt with Key")
        self.decrypt_radio = QRadioButton("Decrypt with Key")
        self.brute_force_radio = QRadioButton("Brute Force Decrypt")

        # No default selection
        self.encrypt_radio.setChecked(False)
        self.decrypt_radio.setChecked(False)
        self.brute_force_radio.setChecked(False)

        self.operation_group = QButtonGroup()
        self.operation_group.addButton(self.encrypt_radio)
        self.operation_group.addButton(self.decrypt_radio)
        self.operation_group.addButton(self.brute_force_radio)

        action_layout.addWidget(self.encrypt_radio)
        action_layout.addWidget(self.decrypt_radio)
        action_layout.addWidget(self.brute_force_radio)
        layout.addLayout(action_layout)

        # Shift Direction Radio Buttons
        self.shift_direction_label = QLabel("Choose shift direction:")
        layout.addWidget(self.shift_direction_label)
        direction_layout = QHBoxLayout()
        self.forward_radio = QRadioButton("Forward")
        self.reverse_radio = QRadioButton("Reverse")

        # No default selection
        self.forward_radio.setChecked(False)
        self.reverse_radio.setChecked(False)

        self.shift_direction_group = QButtonGroup()
        self.shift_direction_group.addButton(self.forward_radio)
        self.shift_direction_group.addButton(self.reverse_radio)

        direction_layout.addWidget(self.forward_radio)
        direction_layout.addWidget(self.reverse_radio)
        layout.addLayout(direction_layout)

        # Shift Entry
        self.shift_label = QLabel("Enter shift key:")
        layout.addWidget(self.shift_label)
        self.shift_entry = QLineEdit()
        self.shift_entry.setStyleSheet("border: 1px solid black; padding: 5px;")  # Initial style
        layout.addWidget(self.shift_entry)

        # Process Button
        self.process_button = QPushButton("Process")
        self.process_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;")
        self.process_button.clicked.connect(self.process_text)
        layout.addWidget(self.process_button)

        # Result Display Area
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setStyleSheet("background-color: #f5f5f5; color: black; border: 1px solid black;")
        layout.addWidget(self.result_area)

        self.setLayout(layout)

        # Connect radio button selection change to update visibility of shift key entry
        self.encrypt_radio.toggled.connect(self.toggle_shift_input)
        self.decrypt_radio.toggled.connect(self.toggle_shift_input)
        self.brute_force_radio.toggled.connect(self.toggle_shift_input)

        # Initial toggle to set correct visibility on start
        self.toggle_shift_input()

        # Set input field focus effects
        self.text_entry.focusInEvent = self.create_focus_event(self.text_entry)
        self.text_entry.focusOutEvent = self.create_focus_event(self.text_entry, out=True)
        self.shift_entry.focusInEvent = self.create_focus_event(self.shift_entry)
        self.shift_entry.focusOutEvent = self.create_focus_event(self.shift_entry, out=True)

        # Set radio button focus effects
        self.encrypt_radio.toggled.connect(self.update_radio_effects)
        self.decrypt_radio.toggled.connect(self.update_radio_effects)
        self.brute_force_radio.toggled.connect(self.update_radio_effects)

    def create_focus_event(self, widget, out=False):
        def event(event):
            if out:
                widget.setStyleSheet("border: 1px solid black;")  # Normal border
            else:
                widget.setStyleSheet("border: 2px solid #00FF00;")  # Green glow effect
            super(QLineEdit, widget).focusInEvent(event)  # Call the original event
        return event

    def toggle_shift_input(self):
        # Show shift input only for Encrypt and Decrypt options
        if self.encrypt_radio.isChecked() or self.decrypt_radio.isChecked():
            self.shift_label.show()
            self.shift_entry.show()
        else:
            self.shift_label.hide()
            self.shift_entry.hide()

    def toggle_theme(self, checked):
        # Switch between light and dark mode
        if checked:  # Dark mode
            self.setStyleSheet("background-color: #2b2b2b; color: white;")
            self.result_area.setStyleSheet("background-color: #1e1e1e; color: white;")
            self.theme_label.setText("Dark Mode")
        else:  # Light mode
            self.setStyleSheet("background-color: white; color: black;")
            self.result_area.setStyleSheet("background-color: #f5f5f5; color: black;")
            self.theme_label.setText("Light Mode")

    def update_radio_effects(self):
        # Glow effect on selected radio button
        for button in [self.encrypt_radio, self.decrypt_radio, self.brute_force_radio]:
            if button.isChecked():
                button.setStyleSheet("border: 2px solid #00FF00;")  # Green glow effect
            else:
                button.setStyleSheet("border: none;")  # Normal border

    def adjust_input_size(self):
        # Automatically adjust the size of the input text box
        self.text_entry.setFixedWidth(self.text_entry.fontMetrics().width(self.text_entry.text()) + 20)

    def process_text(self):
        text = self.text_entry.text()
        direction = 1 if self.forward_radio.isChecked() else -1
        shift = self.get_shift() if (self.encrypt_radio.isChecked() or self.decrypt_radio.isChecked()) else None

        if self.encrypt_radio.isChecked():
            if shift is None:
                return
            shift *= direction
            cipher = CaesarCipher(shift)
            encrypted_text = cipher.encrypt(text)
            self.result_area.setHtml(f"<b>Encrypted text:</b> <span style='color: blue;'>{encrypted_text}</span>")

        elif self.decrypt_radio.isChecked():
            if shift is None:
                return
            shift *= direction
            cipher = CaesarCipher(shift)
            decrypted_text = cipher.decrypt(text)
            self.result_area.setHtml(f"<b>Decrypted text:</b> <span style='color: green;'>{decrypted_text}</span>")

        elif self.brute_force_radio.isChecked():
            results = []
            for shift in range(26):
                cipher = CaesarCipher(shift)
                decrypted_text = cipher.decrypt(text)
                results.append(f"<b>Shift {shift}:</b> <span style='color: red;'>{decrypted_text}</span>")
            self.result_area.setHtml("<br>".join(results))

    def get_shift(self):
        try:
            return int(self.shift_entry.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid shift key.")
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarCipherGUI()
    window.show()
    sys.exit(app.exec_())
