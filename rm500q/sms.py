from .core import RM500Q

class RM500QSMS(RM500Q):
    """
    SMS-related functions for RM500Q-GL.
    """

    def set_sms_format(self, fmt="1"):
        """Set SMS format (0 = PDU, 1 = text)."""
        return self.send_command(f'AT+CMGF={fmt}')

    def send_sms(self, number, message):
        """Send an SMS to 'number' with body 'message'."""
        self.set_sms_format("1")
        ok, _ = self.send_command(f'AT+CMGS="{number}"')
        if not ok:
            return (False, "SMS initiation failed.")
        self.uart.write(message + chr(26))
        lines = []
        while True:
            line = self.read_response()
            if not line:
                return (False, lines)
            lines.append(line)
            if line == "OK":
                return (True, lines)
            if line.startswith("ERROR"):
                return (False, lines)

    def read_sms(self, index=1):
        """Read SMS at a given index."""
        return self.send_command(f'AT+CMGR={index}')

    def delete_sms(self, index):
        """Delete SMS at a given index."""
        return self.send_command(f'AT+CMGD={index}')

    def read_all_sms(self):
        """Read all SMS messages."""
        return self.send_command('AT+CMGL="ALL"')

    def delete_all_sms(self):
        """Delete all SMS messages."""
        return self.send_command('AT+CMGDA="DEL ALL"')
