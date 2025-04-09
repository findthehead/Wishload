import urllib.parse
import base64
import binascii

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

class Encoder:
    @staticmethod
    def encode(text:str, encoding_type) -> str:
        try:
            if encoding_type not in types:
                raise ValueError(f"Unsupported encoding type: {encoding_type}")
            
            if encoding_type in ["utf-8", "utf-16", "utf-16le", "utf-16be", "iso-8859-1", "windows-1252", "shift_jis", "gb18030", "euc-jp", "koi8-r", "macroman", "tis-620", "utf-32", "utf-32le", "utf-32be"]:
                
                encoded_bytes = text.encode(encoding_type)
                return ''.join(f'\\x{hex(b)[2:].zfill(2)}' for b in encoded_bytes)
            
            elif encoding_type == "base64":
                encoded_bytes = base64.b64encode(text.encode())
                return ''.join(f'\\x{hex(b)[2:].zfill(2)}' for b in encoded_bytes)
            
            elif encoding_type == "hex":
                encoded_bytes = binascii.hexlify(text.encode())
                return ''.join(f'\\x{hex(b)[2:].zfill(2)}' for b in encoded_bytes)
            
            elif encoding_type == "binary":
                return ''.join(f'\\x{bin(ord(c))[2:].zfill(8)}' for c in text)
            
            elif encoding_type == "urlencode":
                return urllib.parse.quote(text)
            
            elif encoding_type == "uri":
                return urllib.parse.quote_plus(text)
            
            else:
                raise ValueError(f"Unsupported encoding type: {encoding_type}")
        
        except ValueError as e:
            print(f"Encoding error: {e}")
            return None
