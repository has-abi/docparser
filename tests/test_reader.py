import unittest

from docparser.exceptions import (
    InvalidArgumentTypeException,
    UnsupportedFileFormatException,
)
from docparser.reader import Reader

DOC_FILE_PATH = "/tests/doc_example.doc"
DOCX_FILE_PATH = "/tests/docx_example.docx"


class TestReader(unittest.TestCase):
    def test_read_empty_file(self):
        with self.assertRaises(InvalidArgumentTypeException):
            reader = Reader(input_file=None, file_ext="")  # type: ignore

    def test_read_unsupported_file_type(self):
        with self.assertRaises(UnsupportedFileFormatException):
            reader = Reader(input_file="file_example.pdf", file_ext="pdf")


if __name__ == "__main__":
    unittest.main()
