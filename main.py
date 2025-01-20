from rm500q.sms import RM500QSMS
from rm500q.voice import RM500QCall
from rm500q.http import RM500QHTTP

def main():
    # Example usage with SMS features
    sms_modem = RM500QSMS()
    ok, lines = sms_modem.send_command("AT")
    print("AT response:", ok, lines)

    # Example: send SMS
    # success, resp = sms_modem.send_sms("+1234567890", "Hello from RM500Q!")
    # print("SMS send result:", success, resp)

    # Example usage with Voice
    call_modem = RM500QCall()
    # dial_res, dial_lines = call_modem.dial_call("+1234567890")
    # print("Dial call result:", dial_res, dial_lines)

    # Example usage with HTTP
    http_modem = RM500QHTTP()
    # http_ok, http_resp = http_modem.http_get("https://example.com")
    # print("HTTP GET result:", http_ok, http_resp)

if __name__ == "__main__":
    main()
