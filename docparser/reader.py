import os
from io import BufferedReader
from typing import Union
from zipfile import ZipFile

import docparser.constants as CS
from docparser.exceptions import (
    InvalidArgumentTypeException,
    UnsupportedFileFormatException,
)


class Reader:
    def __init__(self, input_file: Union[str, BufferedReader], file_ext: str) -> None:
        self.__check(input_file, file_ext)
        self.zip_file = self.__to_zip(input_file)

    def __check(self, input_file: Union[str, BufferedReader], file_ext: str) -> None:
        if not isinstance(input_file, (str, BufferedReader)):
            raise InvalidArgumentTypeException(
                "input_file must be a file path or a binary file."
            )
        if file_ext not in CS.ALLOWED_EXTS:
            raise UnsupportedFileFormatException(file_ext)

    def __to_zip(self, input_file: Union[str, BufferedReader]) -> ZipFile:
        zip_file = ZipFile(input_file)
        return zip_file

    def clean_up(self):
        if os.path.isfile(CS.TEMP_DOCX_FILE):
            os.remove(CS.TEMP_DOCX_FILE)
