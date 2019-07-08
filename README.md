# A simple util to transform the dos style file to other system style file

## Introduction

You can easily use it to convert the whole project files whose newline character is ```CRLF``` into Unix style ```LF``` or Mac style ```CR```.

*Note: the Python version is 3.7.3*

## Usage

python ```w2u.py``` -h

```bash
                  .-''-.
                .' .-.  )
       _     _ / .'  / /
 /\    \\   //(_/   / /
 `\\  //\\ //      / /
   \`//  \'/      / /         _    _
    \|   |/      . '         | '  / |
     '          / /    _.-').' | .' |
              .' '  _.'.-'' /  | /  |
             /  /.-'_.'    |   `'.  |
            /    _.'       '   .'|  '/
           ( _.-'           `-'  `--'

usage: w2u.py [-h] [-s {win,mac,unix}] [-v] path

Script that convert the dos style file to other system style file

positional arguments:
  path                  The file path that you want to convert

optional arguments:
  -h, --help            show this help message and exit
  -s {win,mac,unix}, --system {win,mac,unix}
                        The operating system style that you want to convert
  -v, --verbose         Show detail information during conversion
```
