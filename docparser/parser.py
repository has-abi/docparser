from typing import Any

from docparser.document import Document


class Parser:
    def __init__(self, file_parser: Any, file_ext: str, file_name: str) -> None:
        self.file_parser = file_parser
        self.document = self.get_document(file_ext, file_name)

    def get_document(self, file_ext: str, file_name: str) -> Document:
        splitted_content = self.file_parser.extract_text()
        content = " ".join(list(splitted_content.values()))
        return Document(
            name=file_name,
            ext=file_ext,
            content=content,
            splitted_content=splitted_content,
        )
