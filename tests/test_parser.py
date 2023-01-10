import unittest
from unittest.mock import Mock

from docparser.document import Document
from docparser.exceptions import InvalidReturnValueException, MissingAttributeException
from docparser.parser import Parser


class TestParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        file_parser = Mock()
        file_parser.extract_text = Mock(
            return_value={
                "header": "xml header text",
                "body": "xml body text",
                "footer": "xml footer text",
            }
        )
        cls.parser = Parser(
            file_parser=file_parser,
            file_ext="docx",
            file_name="file_name_example.docx",
        )

    def test_parser_with_invalid_file_parser(self):
        test_file_parser = ""
        with self.assertRaises(MissingAttributeException):
            Parser(file_parser=test_file_parser, file_ext="", file_name="")

    def test_invalid_file_parser_extract_text_callable_return(self):
        test_file_parser = Mock()
        test_file_parser.extract_text = Mock(return_value=["list item"])
        with self.assertRaises(InvalidReturnValueException):
            Parser(file_parser=test_file_parser, file_ext="", file_name="")

    def test_get_document(self):
        result_document = __class__.parser.document
        self.assertTrue(isinstance(result_document, Document))
        self.assertEqual(result_document.name, "file_name_example.docx")
        self.assertEqual(result_document.ext, "docx")
        self.assertTrue(isinstance(result_document.splitted_content, dict))
        self.assertListEqual(
            list(result_document.splitted_content.keys()), ["header", "body", "footer"]
        )
        self.assertListEqual(
            list(result_document.splitted_content.values()),
            ["xml header text", "xml body text", "xml footer text"],
        )
        self.assertEqual(
            result_document.content, "xml header text xml body text xml footer text"
        )


if __name__ == "__main__":
    unittest.main()
