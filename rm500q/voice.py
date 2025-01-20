from .core import RM500Q

class RM500QCall(RM500Q):
    """
    Basic call-handling features for RM500Q-GL.
    """

    def dial_call(self, number):
        """Initiate a voice call to the given number."""
        return self.send_command(f'ATD{number};')

    def hang_up(self):
        """Hang up any ongoing voice call."""
        return self.send_command("ATH")

    def answer_call(self):
        """Answer an incoming voice call."""
        return self.send_command("ATA")

    def set_call_vol(self, level=5):
        """Example: set call volume (range depends on modem)."""
        # Typically, for Quectel modules, might be AT+CLVL or similar
        # This is an example; actual command may differ.
        return self.send_command(f'AT+CLVL={level}')
