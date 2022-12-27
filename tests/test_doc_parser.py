import unittest

from docparser import parse


class TestDocParser(unittest.TestCase):
    def test_parse_docx_file_str(self):
        document = parse("tests/data/docx_example.docx")
        self.assertTrue(document.content)

    def test_parse_docx_file_binary(self):
        with open("tests/data/docx_example.docx", "rb") as docx_file:
            document = parse(docx_file)
            self.assertTrue(document.content)

    def test_parse_doc_file_str(self):
        document = parse("tests/data/doc_example.doc")
        self.assertTrue(document.splitted_content)

    def test_parse_doc_file_binary(self):
        with open("tests/data/doc_example.doc", "rb") as docx_file:
            document = parse(docx_file)
            self.assertTrue(document.splitted_content)


if __name__ == "__main__":
    unittest.main()
