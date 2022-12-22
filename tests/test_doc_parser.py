import unittest
from unittest import TestCase

from docparser.doc_parser import DocParser


class TestDocParser(TestCase):
    def test_parse_docx_file_str(self):
        parser = DocParser("tests/data/docx_example.docx")
        self.assertTrue(parser.xml_file)

    def test_parse_docx_file_binary(self):
        with open("tests/data/docx_example.docx", "rb") as docx_file:
            parser = DocParser(docx_file)
            self.assertTrue(parser.xml_file)

    def test_parse_doc_file_str(self):
        parser = DocParser("tests/data/doc_example.doc")
        self.assertTrue(parser.xml_file)

    def test_parse_doc_file_binary(self):
        with open("tests/data/doc_example.doc", "rb") as docx_file:
            parser = DocParser(docx_file)
            self.assertTrue(parser.xml_file)


if __name__ == "__main__":
    unittest.main()
