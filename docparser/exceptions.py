__doc__ = """
This module contains the package exceptions.

Exceptions Classes
------------------

Below is listed the exceptions classes within 
:py:mod:`docparser.exception`
"""


class InvalidArgumentTypeError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class UnsupportedFileFormatError(Exception):
    def __init__(self, file_format: str) -> None:
        super().__init__(
            f"{file_format} if not supported. supported formats are docx and doc."
        )


class MissingAttributeError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidReturnValueError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
