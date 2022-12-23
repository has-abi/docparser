import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Union
from zipfile import ZipFile

import docparser.constants as CS
from docparser.enums import LayoutEnum, TagEnum
from docparser.exceptions import InvalidArgumentTypeException


class XMLParser:
    def __init__(self, input_file: ZipFile, file_ext: str) -> None:
        self.__check(input_file)
        self.__xml_file_parts = self.__to_xml(input_file)
        self.__is_doc = bool(file_ext == CS.DOC_EXT)

    def __check(self, xml_file: ZipFile) -> None:
        if not isinstance(xml_file, ZipFile):
            raise InvalidArgumentTypeException("input file must of type bytes.")

    def extract_text(self, split: bool) -> Union[str, Dict[str, str]]:
        doc_text: Dict[str, str] = {}
        for part_name, content in self.__xml_file_parts.items():
            doc_text[part_name] = ""
            if isinstance(content, list):
                for sub_content in content:
                    doc_text[part_name] += self.__xml2text(sub_content)
            else:
                doc_text[part_name] += self.__xml2text(content)
        return doc_text if split else " ".join(list(doc_text.values()))

    def __xml2text(self, xml_part: bytes) -> str:
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
        if self.__is_doc:
            return re.sub(CS.ASPOSE_EVAL_STATEMENT, "", text)
        return text

    def __to_xml(self, zip_file: ZipFile) -> Dict[str, Union[bytes, List[bytes]]]:
        xml_parts: Dict[str, Union[bytes, List[bytes]]] = {}
        name_list = zip_file.namelist()
        xml_parts["header"] = self.__get_part_by_name_list(
            zip_file, name_list, CS.XML_HEADER
        )
        xml_parts["body"] = zip_file.read(CS.XML_BODY)
        xml_parts["footer"] = self.__get_part_by_name_list(
            zip_file, name_list, CS.XML_FOOTER
        )
        return xml_parts

    def __get_part_by_name_list(
        self, zip_file: ZipFile, name_list: List[str], pattern: str
    ) -> List[bytes]:
        xml_part: List[bytes] = []
        for file_name in name_list:
            if re.match(pattern, file_name):
                xml_part.append(zip_file.read(file_name))
        return xml_part
