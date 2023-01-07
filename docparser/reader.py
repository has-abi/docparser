import os
from io import BufferedReader
from typing import Union
from zipfile import ZipFile

import docparser.constants as CS
from docparser.exceptions import (
    FileNotFoundException,
    InvalidArgumentTypeException,
    UnsupportedFileFormatException,
)


class Reader:
    def __init__(self, input_file: Union[str, BufferedReader], file_ext: str) -> None:
        self.__check(input_file, file_ext)
        self.input_file = input_file
        self.zip_file = self.to_zip()

    def __check(self, input_file: Union[str, BufferedReader], file_ext: str) -> None:
        if not isinstance(input_file, (str, BufferedReader)):
            raise InvalidArgumentTypeException(
                "input_file must be a file path or a binary file."
            )

        if file_ext not in CS.ALLOWED_EXTS:
            raise UnsupportedFileFormatException(file_ext)

        if isinstance(input_file, str) and not os.path.isfile(input_file):
            raise FileNotFoundException(f"File not found: {input_file}")

    def to_zip(self) -> ZipFile:
        zip_file = ZipFile(self.input_file)
        return zip_file
