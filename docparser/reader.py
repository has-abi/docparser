__doc__ = """
This module is a single class, namely :class:`Reader`, which
handles the file reading as a zip file.

Classes & methods
-----------------

Below is listed the class within :py:mod:`docparser.reader`
along with possessed methods.
"""


import os
from io import BufferedReader
from zipfile import ZipFile

import docparser.constants as CS
from docparser.exceptions import (
    InvalidArgumentTypeError,
    UnsupportedFileFormatError,
)


class Reader:
    """Docparser `Reader` class that reads a docx file as a zip file.

    Args:
        input_file (str | BufferedReader): Input file that could be a file
            or a file path.
        file_ext (str): The input file extension.
    """

    def __init__(self, input_file: str | BufferedReader, file_ext: str) -> None:
        """Docparser `Reader` class that reads a docx file as a zip file.

        Args:
            input_file (str | BufferedReader): Input file that could be a file
                or a file path.
            file_ext (str): The input file extension.
        """
        self.__check(input_file, file_ext)
        self.input_file = input_file
        self.zip_file = self.to_zip()

    def __check(self, input_file: str | BufferedReader, file_ext: str) -> None:
        """Check the input arguments of the class constructor for invalid
        types or values.

        Args:
            input_file (str | BufferedReade): Input file that could be a file
                or a file path.
            file_ext (str): The input file extension.

        Raises:
            InvalidArgumentTypeError: Thrown if any argument has an invalid
                type.
            UnsupportedFileFormatError: Thrown if the input file has unsupported
                format.
            FileNotFoundError: Thrown if the input file don't exist in disque or
                not found.
        """
        if not isinstance(input_file, (str, BufferedReader)):
            raise InvalidArgumentTypeError(
                "input_file must be a file path or a binary file."
            )

        if file_ext not in CS.ALLOWED_EXTS:
            raise UnsupportedFileFormatError(file_ext)

        if isinstance(input_file, str) and not os.path.isfile(input_file):
            raise FileNotFoundError(f"File not found: {input_file}")

    def to_zip(self) -> ZipFile:
        """Convert the input file to a zip file.

        Returns:
            ZipFile: The converted zip file.
        """
        zip_file = ZipFile(self.input_file)
        return zip_file
