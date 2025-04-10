from utils.encoder import Encoder
import string

types = [
    "utf-8", "utf-16", "utf-16le", "utf-16be", "iso-8859-1", "windows-1252",
    "shift_jis", "gb18030", "big5", "euc-jp", "koi8-r", "macroman", "tis-620",
    "base64", "ascii", "octal", "hex", "binary", "urlencode", "uri", "gb2312",
    "macintosh", "x-user-defined", "utf-32", "utf-32le", "utf-32be", "koi8-u",
    "iso-8859-2", "iso-8859-3", "iso-8859-4", "iso-8859-5", "iso-8859-6",
    "iso-8859-7", "iso-8859-8", "iso-8859-9", "iso-8859-10", "iso-8859-11",
    "iso-8859-12", "iso-8859-13", "iso-8859-14", "iso-8859-15", "iso-8859-16",
    "mac_cyrillic", "x-mac-cyrillic", "x-mac-roman", "x-mac-ukranian", "windows-874",
    "windows-1250", "windows-1251", "windows-1253", "windows-1254", "windows-1255",
    "windows-1256", "windows-1257", "windows-1258"
]

symbol_list = ['(', '!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', '?', ',', '.', '/', '|', '\\', '`', '~']

# Extend with all lowercase and uppercase letters
symbol_list += list(string.ascii_lowercase)
symbol_list += list(string.ascii_uppercase)

class Make():
    def __init__(self):
        self.strong = 1

    def symboling(self, encoding, symbol, payload):
        """ Encode the symbols in the payload using the specified encoding """
        if encoding is None:
            encoding = "utf-8"  # Default encoding if none is provided

        if self.strong == 1:
            if symbol:
                if isinstance(symbol, str):  # Handle string of symbols
                    for s in symbol:
                        if s in symbol_list:
                            payload = payload.replace(s, Encoder.encode(s, encoding))
                elif isinstance(symbol, list):  # Handle list of symbols
                    for s in symbol:
                        if s in symbol_list:
                            payload = payload.replace(s, Encoder.encode(s, encoding))
                else:
                    raise Exception(f"Unsupported symbol type: {type(symbol)}")
                return payload
            else:
                raise Exception(f"Unsupported symbol: {symbol}")
        return None

    def encoding(self, encoding, payload):
        """ Apply encoding to the payload """
        if encoding and encoding in types:
            return Encoder.encode(payload, encoding)
        else:
            raise Exception(f"Unsupported encoding: {encoding}")
        return None

    def normaling(self, encoding, symbol, payload):
        """ Normalize payload by replacing symbols with UTF-8 encoding """
        if payload:
            for i in symbol_list:
                if i in payload:
                    payload = payload.replace(i, Encoder.encode(i, 'utf-8'))
        else:
            raise Exception(f"Unsupported encoding: {encoding}")
        return payload

    def padding(self, total, chars, left=False, payload=None, right=False, center=False):
        """ Apply padding to the payload """
        if isinstance(payload, str):
            if left:
                return payload.ljust(total, chars)  # Left padding
            elif right:
                return payload.rjust(total, chars)  # Right padding
            elif center:
                return payload.center(total, chars)  # Center padding
            else:
                raise ValueError("Padding direction must be specified (left, right, or center).")
        else:
            raise TypeError("Payload must be a string.")  # Ensure the payload is a string

    def unicode_escape(self, payload, symbol=None):
        if symbol:
            for s in symbol:
                payload = payload.replace(s, f'\\u{ord(s):04x}')
        else:
            unicode_payload = ''.join([f'\\u{ord(c):04x}' for c in payload])
            return unicode_payload
        return payload

    def js_escape(self, payload, symbol=None):

        if symbol:
            for s in symbol:
                payload = payload.replace(s, f'\\x{ord(s):02x}')
        else:
            js_payload = ''.join([f'\\x{ord(c):02x}' for c in payload])
            return js_payload
        return payload
