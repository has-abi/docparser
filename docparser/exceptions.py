__doc__ = """
This module contains the package exceptions.

Exceptions Classes
------------------

Below is listed the exceptions classes within 
:py:mod:`docparser.exception`
"""


class InvalidArgumentTypeException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class FileNotFoundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class UnsupportedFileFormatException(Exception):
    def __init__(self, file_format: str) -> None:
        super().__init__(
            f"{file_format} if not supported. supported formats are docx and doc."
        )


class MissingAttributeException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidReturnValueException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
