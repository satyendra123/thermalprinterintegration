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
'''
import serial
import time

class PrinterControl:
    def __init__(self, port, baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=5)
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
'''
'''
import serial
import time

class PrinterControl:
    def __init__(self, port, baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=5)
            print(f"Printer connected successfully on {port}.")
        except serial.SerialException as e:
            print(f"Error: Could not open port {port}. Details: {e}")
            raise

    def send_command(self, command):
        """Send command to the printer (ensuring it is in byte format)."""
        if isinstance(command, str):
            command = command.encode('utf-8')
        self.ser.write(command)
        self.ser.flush()
        time.sleep(0.1)

    def reset_printer(self):
        """Reset the printer using ESC/POS command."""
        print("Resetting printer...")
        self.send_command("\x1b\x40")

    def set_bold_text(self, enable=True):
        """Enable or disable bold text."""
        if enable:
            self.send_command("\x1b\x45\x01")
        else:
            self.send_command("\x1b\x45\x00")

    def set_alignment(self, align="left"):
        """Set text alignment (left, center, right)."""
        alignments = {"left": 0, "center": 1, "right": 2}
        self.send_command(f"\x1b\x61{chr(alignments.get(align, 0))}")

    def print_text(self, text, bold=False, align="left"):
        """Print text with optional bold and alignment settings."""
        self.set_alignment(align)
        self.set_bold_text(bold)
        self.send_command(text + "\n")
        self.set_bold_text(False)  # Reset bold after text

    def feed_lines(self, lines=1):
        """Feed lines (advance paper)."""
        self.send_command(f"\x1b\x64{chr(lines)}")  # ESC d n

    def cut_paper(self):
        """Cut the paper using ESC/POS command."""
        self.send_command("\x1d\x56\x00")  # ESC i - Cut paper

    def print_receipt(self):
        """Print a properly formatted receipt."""
        self.reset_printer()
        time.sleep(1)
        self.print_text("RECEIPT EXAMPLE", bold=True, align="center")
        self.print_text("Thank you for your purchase!", align="center")
        self.feed_lines(1)
        self.print_text("Item: Apples      $10.00")
        self.print_text("Item: Bananas     $5.00")
        self.feed_lines(1)
        self.print_text("TOTAL: $15.00", bold=True)
        self.feed_lines(2)
        self.print_text("Visit Again!", align="center")
        self.feed_lines(2)
        self.cut_paper()  # Cut the paper after printing

if __name__ == "__main__":
    try:
        printer = PrinterControl(port='COM10')  # Adjust port if needed
        printer.print_receipt()
    except Exception as e:
        print(f"Error: {e}")
'''

import serial
import time

class PrinterControl:
    def __init__(self, port, baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=5)
            print(f"Printer connected successfully on {port}.")
        except serial.SerialException as e:
            print(f"Error: Could not open port {port}. Details: {e}")
            raise

    def send_command(self, command):
        """Send command to the printer."""
        if isinstance(command, str):
            command = command.encode('utf-8')
        self.ser.write(command)
        self.ser.flush()
        time.sleep(0.05)  # Reduce delay for faster execution

    def reset_printer(self):
        """Reset the printer."""
        self.send_command("\x1b\x40")  # ESC @ reset

    def set_bold_text(self, enable=True):
        """Enable or disable bold text."""
        self.send_command("\x1b\x45" + chr(1 if enable else 0))  # ESC E n

    def set_alignment(self, align="left"):
        """Set text alignment (left, center, right)."""
        alignments = {"left": 0, "center": 1, "right": 2}
        self.send_command("\x1b\x61" + chr(alignments.get(align, 0)))  # ESC a n

    def set_line_spacing(self, spacing=30):
        """Set line spacing (default is 30)."""
        self.send_command("\x1b\x33" + chr(spacing))  # ESC 3 n (sets line spacing)

    def print_text(self, text, bold=False, align="left"):
        """Print text with optional bold and alignment settings."""
        self.set_alignment(align)
        self.set_bold_text(bold)
        self.send_command(text)  # Send text without extra newline
        self.send_command("\n")  # Add controlled newline
        self.set_bold_text(False)  # Reset bold

    def feed_lines(self, lines=0):
        """Feed specified number of lines."""
        self.send_command("\x1b\x10" + chr(lines))  # ESC d n (feed n lines)

    def cut_paper(self):
        """Cut the paper."""
        self.send_command("\x1d\x56\x00")  # ESC i (cut paper)

    def print_receipt(self):
        """Print a properly formatted receipt with better spacing."""
        self.reset_printer()
        self.set_line_spacing(24)  # Reduce default spacing
        
        self.print_text("RECEIPT EXAMPLE", bold=True, align="center")
        self.print_text("Thank you for your purchase!", align="center")
        
        self.feed_lines(1)
        self.print_text("Item: Apples      $10.00")
        self.print_text("Item: Bananas     $5.00")
        
        self.feed_lines(1)
        self.print_text("TOTAL: $15.00", bold=True)
        
        self.feed_lines(1)
        self.print_text("Visit Again!", align="center")
        
        self.feed_lines(2)
        self.cut_paper()

if __name__ == "__main__":
    try:
        printer = PrinterControl(port='COM10')  # Adjust to your printer's port
        printer.print_receipt()
    except Exception as e:
        print(f"Error: {e}")
