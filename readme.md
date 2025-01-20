# RM500Q MicroPython Driver

This repository provides a MicroPython driver for the Quectel RM500Q-GL module, featuring:

- **Core** functionality (AT commands, UART setup, power/reset control)
- **SMS** functions (send, read, delete, etc.)
- **Voice call** basics (dial, hang up, answer)
- **HTTP** utilities (simple HTTP GET/POST via AT commands)

---

## Structure


- **`rm500q/core.py`**:  
  Defines the `RM500Q` class that sets up the UART and provides a method to send AT commands, plus optional power/reset control.

- **`rm500q/sms.py`**:  
  Inherits from `RM500Q` to provide SMS-related functions (`send_sms`, `read_sms`, etc.).

- **`rm500q/voice.py`**:  
  Inherits from `RM500Q` to provide basic voice call operations (`dial_call`, `hang_up`, `answer_call`).

- **`rm500q/http.py`**:  
  Inherits from `RM500Q` to provide simple HTTP GET/POST functions via relevant AT commands.

- **`main.py`**:  
  A sample script showing how to import and use the driver classes.

---

## Usage

1. Copy this project to your MicroPython-capable device or emulator.
2. Adjust pins/baud rates in `core.py` as needed.
3. In `main.py` (or your own script), create instances of the relevant classes and call their methods. For example:
   ```python
   from rm500q.sms import RM500QSMS

   def main():
       modem = RM500QSMS(uart_id=1, baudrate=115200, tx_pin=17, rx_pin=16)
       ok, lines = modem.send_command("AT")
       print("AT response:", ok, lines)

       # Send an SMS
       success, resp = modem.send_sms("+1234567890", "Hello from RM500Q!")
       print("SMS send result:", success, resp)

   if __name__ == "__main__":
       main()
Modify APN and credentials in http.py for HTTP connections if required.