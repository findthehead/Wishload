import argparse
import base64
import binascii
import random
import urllib.parse
import threading
import inspect


class Fire():
    def __init__(self,payload):
        self.payload = payload

    def apostrephemask(self):
        return self.payload.replace("'", "%EF%BC%87")


    def apostrephenullify(self):
        return self.payload.replace("'", "%00%27")


    def appendnull(self):
        return self.payload + "%00"


    def base64encode(self):
        return base64.urlsafe_b64encode(self.payload.encode()).decode()


    def booleanmask(self):
        r = {
            "or": "%7C%7C", "OR": "%7C%7C",
            "AND": "%26%26", "and": "%26%26"
        }
        for k, v in r.items():
            self.payload = self.payload.replace(k, v)
        return self.payload


    def doubleurlencode(self):
        encoded = urllib.parse.quote(urllib.parse.quote(self.payload))
        return encoded.replace("_", "%5F").replace(".", "%2E")


    def enclosebrackets(self):
        return ''.join(f"[{c}]" if c.isdigit() else c for c in self.payload)


    def escapequotes(self):
        return self.payload.replace("'", "\\'").replace('"', '\\"')


    def lowercase(self):
        return self.payload.lower()


    def lowlevelunicodecharacter(self):
        r = {
            "1": "\u00B9", "2": "\u00B2", "3": "\u00B3", "D": "\u00D0",
            "T": "\u00DE", "Y": "\u00DD", "a": "\u00AA", "e": "\u00F0",
            "o": "\u00BA", "t": "\u00FE", "y": "\u00FD", "|": "\u00A6",
            "d": "\u00D0", "A": "\u00AA", "E": "\u00F0", "O": "\u00BA"
        }
        for k, v in r.items():
            self.payload = self.payload.replace(k, v)
        return self.payload


    def maskenclosebrackets(self):
        result = []
        apho = "%EF%BC%87"
        for c in self.payload:
            if c.isdigit():
                result.append(f"[{apho}{c}{apho}]")
            else:
                result.append(c)
        return ''.join(result)


    def modsec(self):
        return f"/*!00000{self.payload}*/"


    def modsecspace2comment(self):
        return f"/*!00000{self.payload.replace(' ', '/**/')}*/"


    def obfuscatebyhtml(self):
        return self.payload.translate(str.maketrans({
            " ": "&nbsp;", "<": "&lt;", ">": "&gt;",
            "&": "&amp;", '"': "&quot;", "'": "&apos;"
        }))


    def obfuscatebyordinal(self):
        result = []
        for c in self.payload:
            if c in "%&<>/\\;'\"":
                encoded = "%{0:02x}".format((ord(c) * 10) // 7)
                result.append(encoded)
            else:
                result.append(c)
        return ''.join(result)


    def prependnull(self):
        return "%00" + self.payload


    def randomcase(self):
        return ''.join(random.choice([c.lower(), c.upper()]) for c in self.payload)


    def randomcomments(self):
        return ''.join("/**/" + c if c.isalpha() and random.randint(0, 2) == 1 else c for c in self.payload)


    def randomtabify(self):
        return ''.join("        " if c == " " and random.randint(0, 1) else ("\t" if c == " " else c) for c in self.payload)


    def randomunicode(self):
        result = []
        for c in self.payload:
            if random.randint(0, 9) == 3:
                for _ in range(6):
                    rand_hex = binascii.hexlify(bytes([random.randint(0, 255) for _ in range(2)])).decode()
                    try:
                        s2 = bytes.fromhex(rand_hex).decode('utf-16', errors='ignore')
                        result.append(s2)
                    except Exception:
                        continue
            result.append(c)
        return ''.join(result)


    def space2comment(self):
        return self.payload.replace(" ", "/**/")


    def space2doubledashes(self):
        return self.payload.replace(" ", "--")


    def space2hash(self):
        rand_hex = binascii.hexlify(bytes([random.randint(0, 255) for _ in range(2)])).decode()
        return ''.join(f"%%23{rand_hex}%%0A" if c == " " else c for c in self.payload)


    def space2multicomment(self):
        result = []
        for c in self.payload:
            if c == " ":
                base = "/**/"
                result.append(base * random.randint(1, 3))
            else:
                result.append(c)
        return ''.join(result)


    def space2null(self):
        return self.payload.replace(" ", "%00")


    def space2plus(self):
        return self.payload.replace(" ", "+")


    def space2randomblank(self):
        return ''.join(f"%0{random.choice('9ACD0')}" if c == " " else c for c in self.payload)


    def tabifyspacecommon(self):
        return self.payload.replace(" ", "\t")


    def tabifyspaceuncommon(self):
        return self.payload.replace(" ", "        ")


    def tripleurlencode(self):
        encoded = urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(self.payload)))
        return encoded.replace("_", "%255F").replace(".", "%252E")


    def uppercase(self):
        return self.payload.upper()


    def urlencode(self):
        return urllib.parse.quote(self.payload)


    def urlencodeall(self):
        return ''.join(f"%{binascii.hexlify(c.encode()).decode()}" for c in self.payload)


    def htmlencodeall(self):
        return ''.join(f"&#x{binascii.hexlify(c.encode()).decode()};" for c in self.payload)


    def space2slash(self):
        return self.payload.replace(" ", "/")


    def level1usingutf8(self):
        r = {"<": "%C0%BC", ">": "%C0%BE", "'": "%C0%A7", '"': "%C0%A2"}
        for k, v in r.items():
            self.payload = self.payload.replace(k, v)
        return self.payload


    def level2usingutf8(self):
        r = {"<": "%E0%80%BC", ">": "%E0%80%BE", "'": "%E0%80%A7", '"': "%E0%80%A2"}
        for k, v in r.items():
            payload = self.payload.replace(k, v)
        return payload


    def level3usingutf8(self):
        r = {"<": "%F0%80%80%BC", ">": "%F0%80%80%BE", "'": "%F0%80%80%A7", '"': "%F0%80%80%A2"}
        for k, v in r.items():
            payload = self.payload.replace(k, v)
        return payload
    
    def fire(self):
        methods = [
            getattr(self, name)
            for name in dir(self)
            if callable(getattr(self, name)) and not name.startswith('__') and name != 'fire'
        ]

        results = []
        threads = []

        def run(method):
            result = method()
            results.append(result)

        for method in methods:
            t = threading.Thread(target=run, args=(method,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return '\n'.join(results)
