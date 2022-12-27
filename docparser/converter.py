from io import BufferedReader
from typing import Union

import aspose.words as aw

import docparser.constants as CS


class Converter:
    def __init__(self, input_file: Union[str, BufferedReader]) -> None:
        self.input_file = input_file

    def doc2docx(self):
        doc = aw.Document(self.input_file, load_options=None)  # type: ignore
        doc.save(CS.TEMP_DOCX_FILE, save_options=None)  # type: ignore
