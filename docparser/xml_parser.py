import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Union
from zipfile import ZipFile

import docparser.constants as CS
from docparser.enums import LayoutEnum, TagEnum
from docparser.exceptions import InvalidArgumentTypeException


class XMLParser:
    def __init__(self, input_file: ZipFile) -> None:
        self.__check(input_file)
        self.__zip_file = input_file
        self.__name_list = self.__zip_file.namelist()

    def __check(self, input_file: ZipFile) -> None:
        if not isinstance(input_file, ZipFile):
            raise InvalidArgumentTypeException("input file must of type ZipFile.")

    def extract_text(self) -> Dict[str, str]:
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
        text = ""
        root = ET.fromstring(xml_part)
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

    def to_xml(self) -> Dict[str, Union[bytes, List[bytes]]]:
        xml_parts: Dict[str, Union[bytes, List[bytes]]] = {}
        xml_parts["header"] = self.get_xml_part_by_pattern(CS.XML_HEADER)
        xml_parts["body"] = self.__zip_file.read(CS.XML_BODY)
        xml_parts["footer"] = self.get_xml_part_by_pattern(CS.XML_FOOTER)
        return xml_parts

    def get_xml_part_by_pattern(self, pattern: str) -> List[bytes]:
        xml_part: List[bytes] = []
        for file_name in self.__name_list:
            if re.match(pattern, file_name):
                xml_part.append(self.__zip_file.read(file_name))
        return xml_part
