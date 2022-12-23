import os
from io import BufferedReader
from typing import Union
from zipfile import ZipFile

import aspose.words as aw

import docparser.constants as CS


class DocReader:
    def __init__(self, input_file: Union[str, BufferedReader], file_ext: str) -> None:
        if file_ext == CS.DOC_EXT:
            self.__doc2docx(input_file)
        self.zip_file = self.__to_zip(
            input_file if file_ext == CS.DOCX_EXT else CS.TEMP_DOCX_FILE
        )

    def __to_zip(self, input_file: Union[str, BufferedReader]) -> ZipFile:
        zip_file = ZipFile(input_file)
        return zip_file

    def __doc2docx(self, input_file: Union[str, BufferedReader]):
        doc = aw.Document(input_file, load_options=None)  # type: ignore
        doc.save(CS.TEMP_DOCX_FILE, save_options=None)  # type: ignore

    def clean_up(self):
        if os.path.isfile(CS.TEMP_DOCX_FILE):
            os.remove(CS.TEMP_DOCX_FILE)
