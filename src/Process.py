from typing import List

class Process(object):

    def __init__(self, file_path: str, newline: str, i_encoding=None, o_encoding=None):
        super().__init__()
        self._file_path = file_path
        self._newline = newline
        self._i_encoding = i_encoding
        self._o_encoding = o_encoding

    def __read_file(self) -> List[str]:
        try:
            with open(self._file_path, 'r', encoding=self._i_encoding) as f:
                content_lines = f.readlines()
            return content_lines
        except UnicodeDecodeError as e:
            print("read file [{}] error: {}".format(self._file_path, e))
            return None

    def __write_file(self, content_lines: List[str]) -> None:
        if content_lines:
            with open(self._file_path, 'w', encoding=self._o_encoding, newline=self._newline) as f:
                f.writelines(content_lines)

    def run(self):
        self.__write_file(self.__read_file())
