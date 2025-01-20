from .core import RM500Q

class RM500QHTTP(RM500Q):
    """
    Basic HTTP GET/POST using AT+QHTTP commands or similar.
    """

    def http_get(self, url, timeout=60000):
        """Perform an HTTP GET to the specified URL."""
        # Example for Quectel: AT+QHTTPURL, AT+QHTTPGET, etc.
        # This is simplified; real usage might need more steps (bearer config, etc.)
        steps = [
            'AT+QIFGCNT=0',
            'AT+QICSGP=1,"YOUR_APN","USER","PASS",1',
            'AT+QIREGAPP',
            'AT+QIACT'
        ]
        for cmd in steps:
            ok, lines = self.send_command(cmd, timeout=5000)
            if not ok:
                return (False, lines)

        # Setup URL
        ok, lines = self.send_command(f'AT+QHTTPURL={len(url)},60', 5000)
        if not ok:
            return (False, lines)
        self.uart.write(url.encode("utf-8"))
        resp_line = self.read_response()
        if not resp_line:
            return (False, [])

        # GET
        ok, lines = self.send_command("AT+QHTTPGET=80", timeout)
        return (ok, lines)

    def http_post(self, url, data, timeout=60000):
        """Perform an HTTP POST."""
        steps = [
            'AT+QIFGCNT=0',
            'AT+QICSGP=1,"YOUR_APN","USER","PASS",1',
            'AT+QIREGAPP',
            'AT+QIACT'
        ]
        for cmd in steps:
            ok, lines = self.send_command(cmd, timeout=5000)
            if not ok:
                return (False, lines)

        ok, lines = self.send_command(f'AT+QHTTPURL={len(url)},60', 5000)
        if not ok:
            return (False, lines)
        self.uart.write(url.encode("utf-8"))
        resp_line = self.read_response()
        if not resp_line:
            return (False, [])

        # data
        ok, lines = self.send_command(f'AT+QHTTPPOST={len(data)},80,80', timeout=5000)
        if not ok:
            return (False, lines)
        # write data
        self.uart.write(data.encode("utf-8"))
        end_resp = self.read_response()
        if not end_resp:
            return (False, [])

        # wait final
        final_ok, final_lines = self.send_command("", timeout)
        return (final_ok, final_lines)
