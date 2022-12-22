class InvalidArgumentTypeException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class UnsupportedFileFormatException(Exception):
    def __init__(self, file_format: str) -> None:
        super().__init__(
            f"{file_format} if not supported. supported formats are docx and doc."
        )
