import argparse
import sys
from colorama import init, Fore
from utils.make import Make

init(autoreset=True)

banner = Fore.RED + """
                    _________ _______           _        _______  _______  ______  
            |\\     /|\\__   __/(  ____ \\|\\     /|( \\      (  ___  )(  ___  )(  __  \\ 
            | )   ( |   ) (   | (    \\/| )   ( || (      | (   ) || (   ) || (  \\  )
            | | _ | |   | |   | (_____ | (___) || |      | |   | || (___) || |   ) |
            | |( )| |   | |   (_____  )|  ___  || |      | |   | ||  ___  || |   | |
            | || || |   | |         ) || (   ) || |      | |   | || (   ) || |   ) |
            | () () |___) (___/\\____) || )   ( || (____/\\| (___) || )   ( || (__/  )
            (_______)\\_______/\\_______)|/     \\|(_______/(_______)|/     \\|(______/ 
                        By: fth
                """

class Wishload:
    def __init__(self):
        pass


if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser(description='Make polyglot payloads as per your Wish')
    parser.add_argument('-st', '--strong', type=int, default=1, help='Strength of the payload')
    parser.add_argument('-p', '--payload', type=str, help='Payload to be encoded')
    parser.add_argument('-c', '--camel', type=str, help='Payload to be camelcased')
    parser.add_argument('-s', '--symbol', type=str, help='Symbol to be used')
    parser.add_argument('-pad', '--padding', type=str, help='Padding character to be used')
    parser.add_argument('--padding-length', type=int, help='Total length of the padded payload')  # Padding length
    parser.add_argument('--left', action='store_true', help='Apply padding to the left of the payload')
    parser.add_argument('--right', action='store_true', help='Apply padding to the right of the payload')
    parser.add_argument('--center', action='store_true', help='Apply padding to the center of the payload')
    parser.add_argument('-e', '--encoding', type=str, help='Encoding to be used')
    parser.add_argument('-f', '--file', type=str, help='File to read the payload from')  # For file input
    parser.add_argument('--unicode', action='store_true', help='Convert payload to Unicode escape sequences')
    parser.add_argument('--js_escape', action='store_true', help='Convert payload to JavaScript escape sequences')

    args = parser.parse_args()
    strong = args.strong
    payload = args.payload
    padding = args.padding
    padding_length = args.padding_length
    encoding = args.encoding
    symbol = args.symbol
    file_path = args.file
    left = args.left
    right = args.right
    center = args.center
    camel = args.camel

    # If payload is not provided and file is given, read the file's contents
    if payload is None and file_path:
        try:
            with open(file_path, 'r') as file:
                payload = file.read()
        except Exception as e:
            print(Fore.RED + f"Error reading file: {e}")
            sys.exit(1)

    # If payload is still not provided, check for stdin
    if payload is None and not file_path:
        # If the user pipes input (e.g., cat hello.txt | python wishload.py)
        payload = sys.stdin.read()

    # If no payload is provided
    if payload is None:
        
        print(Fore.RED + "Error: No payload provided. Please provide a payload either via -p, pipe it, or provide a file.")
        sys.exit(1)

    mk = Make(strong)


    # Process transformations (padding, encoding, escapes, etc.)
    final_payload = payload

    # Padding before encoding/escaping
    if padding and padding_length:
        # Apply padding based on the chosen direction (left, right, center)
        padding_args = {
            'left': left,
            'right': right,
            'center': center
        }
        applied_padding = False
        for direction, flag in padding_args.items():
            if flag:
                final_payload = mk.padding(padding_length, padding, **{direction: True}, payload=final_payload)
                applied_padding = True
                break  # Apply only one padding direction

        # Default to left padding if no direction was chosen
        if not applied_padding:
            final_payload = mk.padding(padding_length, padding, left=True, payload=final_payload)

    # Unicode escape after padding (if specified)
    if args.unicode:
        final_payload = mk.unicode_escape(final_payload, symbol=symbol)

    # JavaScript escape after padding (if specified)
    elif args.js_escape:
        final_payload = mk.js_escape(final_payload, symbol=symbol)

    # Symbol encoding if symbol is provided
    elif symbol:
        final_payload = mk.symboling(encoding, symbol, final_payload)
        
    # Encoding if encoding is specified
    elif camel:
        final_payload = mk.cameling(payload)
    elif encoding:
        final_payload = mk.encoding(encoding, final_payload)

    else:
        final_payload = mk.normaling(encoding, symbol, final_payload)



    print(Fore.YELLOW + f"{str(final_payload)}")
