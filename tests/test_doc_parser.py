import unittest
from pathlib import Path

from docparser import parse

DOCX_FILE_PATH = Path(__file__).parent / "data" / "docx_example.docx"


class TestDocParser(unittest.TestCase):
    def test_parse_docx_file_str(self):
        document = parse(str(DOCX_FILE_PATH))
        self.assertTrue(document.content)

    def test_parse_docx_file_binary(self):
        with open(DOCX_FILE_PATH, "rb") as docx_file:
            document = parse(docx_file)
            self.assertTrue(document.content)


if __name__ == "__main__":
    unittest.main()
