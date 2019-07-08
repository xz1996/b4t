import os
import asyncio
import argparse
import datetime
from typing import List

BANNER = r'''
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
'''
print(BANNER)

newline_dict = {"win": "\r\n", "mac": "\r", "unix": "\n"}
parser = argparse.ArgumentParser(description="Script that convert the dos style file to other system style file")
parser.add_argument("path", help="The file path that you want to convert", type=str)
parser.add_argument("-s", "--system", type=str, choices=list(newline_dict.keys()), default="unix", help="The operating system style that you want to convert")
parser.add_argument("-v", "--verbose", action="store_true", help="Show detail information during conversion")
args = parser.parse_args()

def list_files(file_path: str) -> List[str]:

    file_path_list = []
    for (dirpath, dirnames, files) in os.walk(file_path):
        file_path_list.extend(os.path.join(dirpath, f) for f in files)

    return file_path_list

async def read_file(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as f:
            content_lines = f.readlines()
        return content_lines
    except UnicodeDecodeError as e:
        print("read file [{}] error: {}".format(file_path, e))
        return None

async def write_file(file_path: str, content_lines: List[str]) -> None:
    with open(file_path, 'w', newline=newline_dict.get(args.system)) as f:
        f.writelines(content_lines)
    if args.verbose:
        print("{} conversion success at [{}].".format(file_path, datetime.datetime.now()))

async def func_with_cb(func, callback, arg):
    result = await func(arg)
    if result:
        await callback(arg, result)

async def process():
    for fp in list_files(args.path):
        asyncio.create_task(func_with_cb(read_file, write_file, fp))

if __name__ == '__main__':

    asyncio.run(process())
    print("Conversion over.")






