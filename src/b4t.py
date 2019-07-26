import argparse
import asyncio
import os
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait
from time import time
from typing import List

from Process import Process

BANNER = r'''
______    ___ _____
| ___ \  /   |_   _|
| |_/ / / /| | | |
| ___ \/ /_| | | |
| |_/ /\___  | | |
\____/     |_/ \_/
'''
print(BANNER)

newline_dict = {"win": "\r\n", "mac": "\r", "unix": "\n"}
parser = argparse.ArgumentParser(
    description="Script that convert the dos style file to other system style file")
parser.add_argument(
    "path", help="The file path that you want to convert", type=str)
parser.add_argument("-s", "--system", type=str, choices=list(newline_dict.keys()),
                    default="unix", help="The operating system style that you want to convert")
parser.add_argument("--input_encoding", type=str,
                    help="The encoding of files to be processed")
parser.add_argument("--output_encoding", type=str,
                    help="The encoding of files after being processed")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show detail information during conversion")
args = parser.parse_args()


def list_files(file_path: str) -> List[str]:

    file_path_list = []
    for (dirpath, dirnames, files) in os.walk(file_path):
        file_path_list.extend(os.path.join(dirpath, f) for f in files)
    return file_path_list


def main():
    start = time()
    future_tasks = []
    with ThreadPoolExecutor(max_workers=40, thread_name_prefix='b4t-') as executor:
        for fp in list_files(args.path):
            p = Process(fp, newline_dict.get(
                args.system), i_encoding=args.input_encoding, o_encoding=args.output_encoding, verbose=args.verbose)
            future_tasks.append(executor.submit(p.run))

    wait(future_tasks, return_when=ALL_COMPLETED)
    print("Processing over, totally cost {:.2f} s.".format(time() - start))


if __name__ == '__main__':
    main()
