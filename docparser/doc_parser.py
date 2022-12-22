import xml.etree.ElementTree as ET
from io import BufferedReader
from typing import Union
from zipfile import ZipFile

from docparser.exceptions import (
    InvalidArgumentTypeException,
    UnsupportedFileFormatException,
)
from docparser.utils import get_file_extension


class DocParser:
    def __init__(self, input_file: Union[str, BufferedReader]) -> None:
        self.__check(input_file)
        self.xml_file = ET.fromstring(self.__read_as_xml(input_file))

    def __check(self, input_file: Union[str, BufferedReader]) -> None:
        if not isinstance(input_file, (str, BufferedReader)):
            raise InvalidArgumentTypeException(
                "input_file must be a file path or a binary file."
            )
        if isinstance(input_file, str):
            file_format = get_file_extension(input_file)
            if file_format not in ["docx", "doc"]:
                raise UnsupportedFileFormatException(file_format)

    def __read_as_xml(self, input_file: Union[str, BufferedReader]) -> bytes:
        with ZipFile(input_file) as zipfile:
            return zipfile.read("word/document.xml")
