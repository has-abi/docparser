from io import BufferedReader
from typing import Dict, Union

import docparser.constants as CS
from docparser.doc_reader import DocReader
from docparser.exceptions import (InvalidArgumentTypeException,
                                  UnsupportedFileFormatException)
from docparser.utils import get_file_extension
from docparser.xml_parser import XMLParser


class DocParser:
    def __init__(self, input_file: Union[str, BufferedReader]) -> None:
        self.__file_ext = get_file_extension(input_file)
        self.__check(input_file, self.__file_ext)
        self.__reader = DocReader(input_file, self.__file_ext)
        self.xml_parser = XMLParser(self.__reader.zip_file, self.__file_ext)
        self.__reader.zip_file.close()
        self.__reader.clean_up()

    def __check(self, input_file: Union[str, BufferedReader], file_ext: str) -> None:
        if not isinstance(input_file, (str, BufferedReader)):
            raise InvalidArgumentTypeException(
                "input_file must be a file path or a binary file."
            )
        if file_ext not in CS.ALLOWED_EXTS:
            raise UnsupportedFileFormatException(file_ext)

    def get_text(self, split: bool = False) -> Union[str, Dict[str, str]]:
        return self.xml_parser.extract_text(split)
