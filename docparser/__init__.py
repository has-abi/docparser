__doc__ = """
This is the package entrypoint which exposes the
`parse` method that handles the parsing process.
"""


from io import BufferedReader
from typing import Union

from docparser.document import Document
from docparser.parser import Parser
from docparser.reader import Reader
from docparser.utils import get_file_name_and_ext
from docparser.xml_parser import XMLParser


def parse(input_file: Union[str, BufferedReader]) -> Document:
    file_name, file_ext = get_file_name_and_ext(input_file)
    reader = Reader(input_file, file_ext)
    file_parser = XMLParser(reader.zip_file)
    parser = Parser(file_parser, file_ext, file_name)
    reader.zip_file.close()
    return parser.document
