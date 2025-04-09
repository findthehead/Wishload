# Wishload

**Wishload** is a powerful tool that allows you to craft and manipulate polyglot payloads. With a variety of encoding and escape options, this tool is designed to help security researchers, penetration testers, and developers create complex payloads for web applications and beyond. Whether you're looking to encode your payload in multiple formats, apply padding, or convert characters to escape sequences, **Wishload** makes it simple and efficient.

## Features

- **Customizable Padding**: Add padding characters to the left, right, or center of your payload.
- **Multiple Encodings**: Choose from a wide variety of encoding types (UTF-8, Base64, URL Encoding, etc.).
- **Escape Sequences**: Convert your payload to Unicode escape sequences or JavaScript escape sequences.
- **Symbol Encoding**: Encode specific symbols within your payload using a chosen encoding type.
- **File and Pipe Input**: Accept input directly from files or pipes for flexibility.
- **Strong Payload Strength**: Choose the level of payload strength based on your needs.

## Installation

To get started with **Wishload**, simply clone this repository or download the latest release.

### Clone the Repository

```bash
git clone https://github.com/findthehead/Wishload.git
cd wishload
```

### Install Dependencies

**Wishload** is written in Python, so you'll need Python 3.x installed on your system.

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Arguments

**Wishload** provides a wide range of command-line options to tailor your payload creation.

```bash
usage: wishload.py [-h] [-strong STRONG] [-p PAYLOAD] [-s SYMBOL] [-pad PADDING]
                   [--padding-length PADDING_LENGTH] [--left] [--right]
                   [--center] [-e ENCODING] [-f FILE] [--unicode] [--js_escape]

Make polyglot payloads as per your Wish
```

#### Arguments:

- `-p`, `--payload`: **Payload to be encoded** (e.g., `"<script>alert('Hello!');</script>"`).
- `-s`, `--symbol`: **Symbols to be encoded** (e.g., `"<>;"`).
- `-pad`, `--padding`: **Padding character** (e.g., `"#"`).
- `--padding-length`: **Total length** of the padded payload (e.g., `20`).
- `--left`: Apply padding to the **left** of the payload.
- `--right`: Apply padding to the **right** of the payload.
- `--center`: Apply padding to the **center** of the payload.
- `-e`, `--encoding`: **Encoding to be used** (e.g., `utf-8`, `base64`, `ascii`, etc.).
- `-f`, `--file`: **Path to a file** to read the payload from.
- `--unicode`: Convert the payload to **Unicode escape sequences** (e.g., `\uXXXX`).
- `--js_escape`: Convert the payload to **JavaScript escape sequences** (e.g., `\xXX`).
- `-strong`, `--strong`: **Strength of the payload** (default is `1`).

### Examples

#### Basic Usage: Encoding and Padding

```bash
python wishload.py -p "hello <world" --padding "#" --padding-length 20 --center
```

This will:
- Add padding characters (`#`) to the center of the payload `"hello <world"` so that the total length becomes `20`.

#### Unicode Escape Sequences

```bash
python wishload.py -p "hello <world" --unicode
```

This will:
- Convert the payload `"hello <world"` to Unicode escape sequences (e.g., `hello \u003cworld`).

#### JavaScript Escape Sequences

```bash
python wishload.py -p "hello <world" --js_escape
```

This will:
- Convert the payload `"hello <world"` to JavaScript escape sequences (e.g., `hello \x3cworld`).

#### File Input

```bash
python wishload.py -f "input.txt" --padding "#" --padding-length 50 --center
```

This will:
- Read the payload from the `input.txt` file and apply padding to the center.

## Example Output

For the following command:

```bash
python wishload.py -p "hello <world" --padding "#" --padding-length 20 --center --js_escape
```

**Output**:

```text
Final Payload: ####hello \x3cworld####
```

### Notes:

- The padding operation will adjust the total length of the payload as per your specified length.
- You can chain different transformations together (e.g., padding + encoding + escape sequences).
- By default, **Wishload** will apply left padding if no padding direction is specified.

## Contributing

We welcome contributions from the community! To contribute, please fork the repository, create a feature branch, and submit a pull request. Be sure to include tests for any new features or bug fixes.

### Steps to Contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -am 'Add new feature'`
4. Push to your forked repository: `git push origin feature-name`
5. Open a pull request with a detailed description of your changes



### Docker Setup

To run the **Wishload** project inside a Docker container, follow these steps:

1. **Build the Docker Image**

   In your project directory (where the `Dockerfile` is located), build the Docker image using the following command:

   ```bash
   docker build -t wishload .
   ```

   This will create a Docker image named `wishload`.

2. **Run the Docker Container**

   After building the image, run the container with the following command:

   ```bash
   docker run --rm wishload -p "hello <world" --padding "#" --padding-length 20 --center
   ```



## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.



### **Wishload**: Make polyglot payloads with ease!
