import os
import xml.etree.ElementTree as ET
from io import BufferedReader
from typing import Union
from zipfile import ZipFile

import aspose.words as aw

from docparser.exceptions import (
    InvalidArgumentTypeException,
    UnsupportedFileFormatException,
)
from docparser.utils import get_file_extension

TEMP_DOCX_FILE = "temp/temp_doc.docx"
DOCX_EXT = "docx"
DOC_EXT = "doc"
ALLOWED_EXTS = [DOCX_EXT, DOC_EXT]
XML_DOC = "word/document.xml"


class DocParser:
    def __init__(self, input_file: Union[str, BufferedReader]) -> None:
        self.__check(input_file)
        self.__file_extension = get_file_extension(input_file)
        if self.__file_extension == DOC_EXT:
            self.__doc2docx(input_file)
        self.xml_file = ET.fromstring(
            self.__read_as_xml(
                input_file if self.__file_extension == DOCX_EXT else TEMP_DOCX_FILE
            )
        )

    def __check(self, input_file: Union[str, BufferedReader]) -> None:
        if not isinstance(input_file, (str, BufferedReader)):
            raise InvalidArgumentTypeException(
                "input_file must be a file path or a binary file."
            )
        if isinstance(input_file, str):
            file_format = get_file_extension(input_file)
            if file_format not in ALLOWED_EXTS:
                raise UnsupportedFileFormatException(file_format)

    def __read_as_xml(self, input_file: Union[str, BufferedReader]) -> bytes:
        with ZipFile(input_file) as zipfile:
            xml_file = zipfile.read(XML_DOC)
        self.__clear_temp()
        return xml_file

    def __doc2docx(self, input_file: Union[str, BufferedReader]):
        doc = aw.Document(input_file, load_options=None)  # type: ignore
        doc.save(TEMP_DOCX_FILE, save_options=None)  # type: ignore

    def __clear_temp(self):
        if os.path.isfile(TEMP_DOCX_FILE):
            os.remove(TEMP_DOCX_FILE)
