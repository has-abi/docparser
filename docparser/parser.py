from docparser.document import Document
from docparser.reader import Reader
from docparser.xml_parser import XMLParser


class Parser:
    def __init__(self, reader: Reader, file_ext: str, file_name: str) -> None:
        self.xml_parser = XMLParser(reader.zip_file, file_ext)
        self.document = self.get_document(file_ext, file_name)
        self.__end(reader)

    def get_document(self, file_ext: str, file_name: str) -> Document:
        splitted_content = self.xml_parser.extract_text()
        content = " ".join(list(splitted_content.values()))
        return Document(
            name=file_name,
            ext=file_ext,
            content=content,
            splitted_content=splitted_content,
        )

    def __end(self, reader: Reader) -> None:
        reader.zip_file.close()
        reader.clean_up()
