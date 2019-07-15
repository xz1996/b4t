# Batch operation for text files

## Introduction

You can easily use it to convert the whole project files whose newline character is ```CRLF``` into Unix style ```LF``` or Mac style ```CR```.

*Note: the Python version is 3.7.3*

## Usage

python ```b4t.py``` -h

```bash
| ___ \  /   |_   _|
| |_/ / / /| | | |
| ___ \/ /_| | | |
| |_/ /\___  | | |
\____/     |_/ \_/

usage: b4t.py [-h] [-s {win,mac,unix}] [--input_encoding INPUT_ENCODING]
              [--output_encoding OUTPUT_ENCODING] [-v]
              path

Script that convert the dos style file to other system style file

positional arguments:
  path                  The file path that you want to convert

optional arguments:
  -h, --help            show this help message and exit
  -s {win,mac,unix}, --system {win,mac,unix}
                        The operating system style that you want to convert
  --input_encoding INPUT_ENCODING
                        The encoding of files to be processed
  --output_encoding OUTPUT_ENCODING
                        The encoding of files after being processed
  -v, --verbose         Show detail information during conversion
```
