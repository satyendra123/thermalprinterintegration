'''
import serial
import time

class PrinterControl:
    def __init__(self, port, baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=5)  # Increased timeout
            print("Printer connected successfully.")
        except serial.SerialException as e:
            print(f"Error: Could not open port {port}. Details: {e}")
            raise

    def send_command(self, command):
        """Send command to the printer."""
        if isinstance(command, str):
            command = command.encode('utf-8')  # Ensure it's encoded as bytes
        self.ser.write(command)
        print(f"Sent command: {command}")
        time.sleep(0.5)

    def reset_printer(self):
        """Reset the printer."""
        self.send_command("\x1b\x40")

    def print_text(self, text):
        """Print plain text."""
        self.send_command(text + "\n")

    def print_receipt(self):
        """Print a simple receipt."""
        self.reset_printer()
        time.sleep(1)
        self.print_text("Test print")
        self.send_command("\x1b\x64\x03")

if __name__ == "__main__":
    printer = PrinterControl(port='COM10')  # Adjust to your port
    printer.print_receipt()
'''

import serial
import time

class PrinterControl:
    def __init__(self, port, baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=5)  # Increased timeout
            print(f"Printer connected successfully on {port}.")
        except serial.SerialException as e:
            print(f"Error: Could not open port {port}. Details: {e}")
            raise

    def send_command(self, command):
        """Send command to the printer."""
        if isinstance(command, str):
            command = command.encode('utf-8')  # Ensure it's encoded as bytes
        self.ser.write(command)
        print(f"Sent command: {command}")
        time.sleep(0.5)  # Add delay to ensure commands are processed properly

    def reset_printer(self):
        """Reset the printer."""
        print("Resetting printer...")
        self.send_command("\x1b\x40")  # ESC @ to reset the printer

    def print_text(self, text):
        """Print plain text."""
        print(f"Printing text: {text}")
        self.send_command(text + "\n")  # Add a newline after text

    def feed_lines(self, lines=1):
        """Feed lines (optional for spacing)."""
        for _ in range(lines):
            self.send_command("\x1b\x64\x03")  # Feed 3 lines

    def cut_paper(self):
        """Cut the paper (optional)."""
        self.send_command("\x1d\x56\x00")  # ESC 0 to cut the paper

    def print_receipt(self):
        """Print a simple receipt."""
        self.reset_printer()
        time.sleep(1)
        self.print_text("Receipt Example")
        self.print_text("Thank you for your purchase!")
        self.feed_lines(2)
        self.print_text("Item: Apples      $10.00")
        self.print_text("Item: Bananas     $5.00")
        self.print_text("Total: $15.00")
        self.feed_lines(2)
        self.print_text("Thank you for shopping with us!")
        self.feed_lines(2)
        self.cut_paper()  # Cut the paper after printing

if __name__ == "__main__":
    try:
        printer = PrinterControl(port='COM10')  # Adjust to your port
        printer.print_receipt()
    except Exception as e:
        print(f"Error: {e}")
