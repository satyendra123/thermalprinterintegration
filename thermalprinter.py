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
