__doc__ = """
This module is a single class, namely :class:`Parser`, which
is the end class that handles getting the parsing results from
a file parser.

Classes & methods
-----------------

Below is listed the class within :py:mod:`docparser.parser`
along with possessed methods.
"""


from typing import Any

from docparser.document import Document
from docparser.exceptions import InvalidReturnValueException, MissingAttributeException


class Parser:
    """Docparser `Parser` class.

    Args:
        file_parser (Any): A file parser that has an `extract_text` method
            that returns the parsed document content as a dictionary.
        file_ext (str): The original file extension.
        file_name (str): The original file name.
    """

    def __init__(self, file_parser: Any, file_ext: str, file_name: str) -> None:
        """Docparser `Parser` class.

        Args:
            file_parser (Any): A file parser that has an `extract_text` method
                that returns the parsed document content as a dictionary.
            file_ext (str): The original file extension.
            file_name (str): The original file name.
        """
        self.__check(file_parser)
        self.file_parser = file_parser
        self.document = self.get_document(file_ext, file_name)

    def __check(self, file_parser: Any) -> None:
        """Checks if the `file_parser` has a callable with the name
        `extract_text`.

        Args:
            file_parser (Any): A file parser.

        Raises:
            MissingAttributeException: Thrown if the file parser don't have
                a callable `extract_text`
        """
        if not (
            hasattr(file_parser, "extract_text") and callable(file_parser.extract_text)
        ):
            raise MissingAttributeException(
                "Missing callable extract_text() from file_parser instance."
            )

    def get_document(self, file_ext: str, file_name: str) -> Document:
        """Get the extracted document data.

        Args:
            file_ext (str): The original file extension
            file_name (str): The original file name.

        Raises:
            InvalidValueException: throw if the file parser callable
                `extract_text` return value is not a dict.

        Returns:
            Document: A document object that represents the parsed results.
        """
        splitted_content = self.file_parser.extract_text()
        if not isinstance(splitted_content, dict):
            raise InvalidReturnValueException(
                "The file parser extract_text callable return value must be a dict"
            )
        content = " ".join(list(splitted_content.values()))
        return Document(
            name=file_name,
            ext=file_ext,
            content=content,
            splitted_content=splitted_content,
        )
