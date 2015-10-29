import abc

import typing


class IOBase(metaclass=abc.ABCMeta):
    def __init__(self, file_path: str, *args, **kwargs) -> None:
        self.original_path = file_path

    def extract(self) -> typing.List[str]:
        pass

    def substitute(self, texts: typing.List[str]) -> None:
        pass

    def save(self, dest_file_path: str=None) -> None:
        """
        :param dest_file_path: When this parameter is None, overwrite the original file.
        """
        pass


class TextIO(IOBase):
    def __init__(self, file_path: str, *args, **kwargs) -> None:
        super().__init__(file_path)
        with open(file_path) as f:
            self.text = f.read()

    def extract(self) -> typing.List[str]:
        return [self.text]

    def substitute(self, texts: typing.List[str]) -> None:
        self.text = texts[0]

    def save(self, dest_file_path: str=None) -> None:
        with open(dest_file_path or self.original_path, 'w') as f:
            f.write(self.text)
