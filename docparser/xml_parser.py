__doc__ = """
This module is a single class, namely :class:`XMLParser`, which
represents an XML parser that extracts text from different XML
nodes.

Classes & methods
-----------------

Below is listed the class within :py:mod:`docparser.xml_parser`
along with possessed methods.
"""


import re
import xml.etree.ElementTree as ETree
from typing import Dict, List
from zipfile import ZipFile

import docparser.constants as CS
from docparser.enums import LayoutEnum, TagEnum
from docparser.exceptions import InvalidArgumentTypeError


XML_Type = Dict[str, bytes | List[bytes]]


class XMLParser:
    """Docparser `XMLParser` class that parses the input zip file
    using the python package `xml`.

    Args:
        input_file (ZipFile): Zip file.
    """

    def __init__(self, input_file: ZipFile) -> None:
        """Docparser `XMLParser` class that parses the input zip file
        using the python package `xml`.

        Args:
            input_file (ZipFile): Zip file.
        """
        self.__check(input_file)
        self.__zip_file = input_file
        self.__name_list = self.__zip_file.namelist()

    def __check(self, input_file: ZipFile) -> None:
        """Check the input arguments of the class constructor for invalid
        types or values.

        Args:
            input_file (ZipFile): Zip file.

        Raises:
            InvalidArgumentTypeError: Thrown if the input file is not an
                instance of ZipFile.
        """
        if not isinstance(input_file, ZipFile):
            raise InvalidArgumentTypeError("input file must of type ZipFile.")

    def extract_text(self) -> Dict[str, str]:
        """Extract text from the zip file using XML.

        Returns:
            Dict[str, str]: A dictionary containing the document
                XML parts [head, body, footer] and their text.
        """
        doc_text: Dict[str, str] = {}
        xml_components = self.to_xml()
        for part_name, content in xml_components.items():
            doc_text[part_name] = ""
            if isinstance(content, list):
                for sub_content in content:
                    doc_text[part_name] += self.xml2text(sub_content)
            else:
                doc_text[part_name] += self.xml2text(content)
        return doc_text

    def xml2text(self, xml_part: bytes) -> str:
        """Extract text from xml component nodes.

        Args:
            xml_part (bytes): XML component.

        Returns:
            str: The extracted text.
        """
        text = ""
        root = ETree.fromstring(xml_part)
        for child in root.iter():
            if child.tag == TagEnum.SPACE:
                text += child.text if child.text is not None else ""
            elif child.tag == TagEnum.TAB:
                text += LayoutEnum.TAB
            elif child.tag in (
                TagEnum.BREAK_LINE,
                TagEnum.CARRIAGE_RETURN,
            ):
                text += LayoutEnum.BREAK_LINE
            elif child.tag == TagEnum.PARAGRAPH:
                text += LayoutEnum.MAJ_BREAK_LINE
        return text

    def to_xml(self) -> XML_Type:
        """Convert a zip file to XML components header, body and footer.

        Returns:
            XML_Type: Dictionary containing
                the components content.
        """
        xml_parts: XML_Type = {"header": self.get_xml_part_by_pattern(CS.XML_HEADER),
                               "body": self.__zip_file.read(CS.XML_BODY),
                               "footer": self.get_xml_part_by_pattern(CS.XML_FOOTER)}
        return xml_parts

    def get_xml_part_by_pattern(self, pattern: str) -> List[bytes]:
        """Get all XML component parts based on the input `pattern`.

        Args:
            pattern (str): The pattern of the component.

        Returns:
            List[bytes]: List of the components parts.
        """
        xml_part: List[bytes] = []
        for file_name in self.__name_list:
            if re.match(pattern, file_name):
                xml_part.append(self.__zip_file.read(file_name))
        return xml_part
