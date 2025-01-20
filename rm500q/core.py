import machine
import time

class RM500Q:
    """
    Core class for RM500Q-GL:
      - Manages UART.
      - Provides basic AT command sending.
      - Optional power/reset pin control.
    """

    def __init__(self, uart_id=1, baudrate=115200, tx_pin=17, rx_pin=16, pwr_pin=None, rst_pin=None):
        self.uart = machine.UART(uart_id, baudrate=baudrate, tx=tx_pin, rx=rx_pin)
        self.pwr_pin = None
        if pwr_pin is not None:
            self.pwr_pin = machine.Pin(pwr_pin, machine.Pin.OUT)
            self.pwr_pin.value(1)
        self.rst_pin = None
        if rst_pin is not None:
            self.rst_pin = machine.Pin(rst_pin, machine.Pin.OUT)
            self.rst_pin.value(1)

    def send_command(self, command, timeout=2000):
        """Send an AT command and await final response."""
        cmd_str = command.strip() + "\r\n"
        self.uart.write(cmd_str.encode("utf-8"))
        lines = []
        start = time.ticks_ms()
        while True:
            line = self._read_line(timeout)
            if not line:
                return (False, lines)
            lines.append(line)
            if line == "OK":
                return (True, lines)
            elif line.startswith("ERROR"):
                return (False, lines)
            if time.ticks_diff(time.ticks_ms(), start) > timeout:
                return (False, lines)

    def read_response(self):
        """Read a single line from UART."""
        return self._read_line()

    def _read_line(self, timeout=1000):
        """Internal: read until newline or timeout."""
        start = time.ticks_ms()
        buf = b""
        while True:
            if self.uart.any():
                c = self.uart.read(1)
                if c == b'\n':
                    return buf.decode("utf-8").strip()
                buf += c
            if time.ticks_diff(time.ticks_ms(), start) > timeout:
                return None

    def power_on(self):
        if self.pwr_pin:
            self.pwr_pin.value(1)
            time.sleep_ms(100)

    def power_off(self):
        if self.pwr_pin:
            self.pwr_pin.value(0)
            time.sleep_ms(100)

    def reset_modem(self, duration_ms=200):
        if self.rst_pin:
            self.rst_pin.value(0)
            time.sleep_ms(duration_ms)
            self.rst_pin.value(1)
