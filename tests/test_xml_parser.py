import unittest
from pathlib import Path
from zipfile import ZipFile

from docparser.exceptions import InvalidArgumentTypeError
from docparser.xml_parser import XMLParser

DOCX_FILE_PATH = Path(__file__).parent / "data" / "docx_example.docx"

XML_BODY = "word/document.xml"
XML_HEADER = "word/header[0-9]*.xml"
XML_FOOTER = "word/footer[0-9]*.xml"


class TestXMLParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.zip_file = ZipFile(DOCX_FILE_PATH)
        cls.xml_parser = XMLParser(cls.zip_file)

    def test_invalid_input_file(self):
        with self.assertRaises(InvalidArgumentTypeError):
            xml_parser = XMLParser(input_file="")  # type: ignore

    def test_get_xml_part_by_pattern_header(self) -> None:
        test_result = __class__.xml_parser.get_xml_part_by_pattern(XML_HEADER)
        self.assertTrue(isinstance(test_result, list))
        self.assertTrue(all(isinstance(result, bytes) for result in test_result))

    def test_get_xml_part_by_pattern_body(self) -> None:
        test_result = __class__.xml_parser.get_xml_part_by_pattern(XML_BODY)
        self.assertTrue(isinstance(test_result, list))
        self.assertTrue(all(isinstance(result, bytes) for result in test_result))

    def test_get_xml_part_by_pattern_footer(self) -> None:
        test_result = __class__.xml_parser.get_xml_part_by_pattern(XML_FOOTER)
        self.assertTrue(isinstance(test_result, list))
        self.assertTrue(all(isinstance(result, bytes) for result in test_result))

    def test_to_xml(self) -> None:
        test_xml_components = __class__.xml_parser.to_xml()
        self.assertTrue(
            ["header", "body", "footer"] == list(test_xml_components.keys())
        )

    def test_xml2text(self) -> None:
        test_xml_body = __class__.xml_parser.get_xml_part_by_pattern(XML_BODY)
        text_result = " ".join(
            [self.xml_parser.xml2text(part) for part in test_xml_body]
        )
        self.assertTrue(len(text_result) > 0)

    def test_extract_text(self) -> None:
        doc_content = __class__.xml_parser.extract_text()
        self.assertTrue(isinstance(doc_content, dict))
        self.assertTrue(["header", "body", "footer"] == list(doc_content.keys()))
        self.assertTrue(
            (
                (isinstance(component_content, str) and len(component_content) > 0)
                for component_content in doc_content.values()
            )
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.zip_file.close()


if __name__ == "__main__":
    unittest.main()
