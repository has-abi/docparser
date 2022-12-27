from io import BufferedReader
from typing import Union

from docparser.document import Document
from docparser.parser import Parser
from docparser.reader import Reader
from docparser.utils import get_file_name_and_ext


def parse(input_file: Union[str, BufferedReader]) -> Document:
    file_name, file_ext = get_file_name_and_ext(input_file)
    reader = Reader(input_file, file_ext)
    parser = Parser(reader, file_ext, file_name)
    return parser.document
