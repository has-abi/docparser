import unittest
from pathlib import Path
from zipfile import ZipFile

from docparser.exceptions import (
    InvalidArgumentTypeError,
    UnsupportedFileFormatError,
)
from docparser.reader import Reader

DOCX_FILE_PATH = Path(__file__).parent / "data" / "docx_example.docx"


class TestReader(unittest.TestCase):
    def test_read_empty_file(self):
        with self.assertRaises(InvalidArgumentTypeError):
            reader = Reader(input_file=None, file_ext="")  # type: ignore

    def test_read_unsupported_file_type(self):
        with self.assertRaises(UnsupportedFileFormatError):
            reader = Reader(input_file="file_example.pdf", file_ext="pdf")

    def test_read_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            reader = Reader(input_file="missing_file.docx", file_ext="docx")

    def test_to_zip_str_file(self):
        test_reader = Reader(input_file=str(DOCX_FILE_PATH), file_ext="docx")
        zip_file = test_reader.to_zip()
        self.assertTrue(isinstance(zip_file, ZipFile))


if __name__ == "__main__":
    unittest.main()
