import os
import unittest

from docparser.constants import TEMP_DOCX_FILE
from docparser.converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        if os.path.isfile(TEMP_DOCX_FILE):
            os.remove(TEMP_DOCX_FILE)

    def tearDown(self):
        os.remove(TEMP_DOCX_FILE)

    def test_convert_doc_to_docx_from_str_file(self):
        input_file = "tests/data/doc_example.doc"
        Converter(input_file).doc2docx()
        self.assertTrue(os.path.isfile(TEMP_DOCX_FILE))


if __name__ == "__main__":
    unittest.main()
