from io import BufferedReader
from typing import Union


def get_file_extension(file_or_filename: Union[str, BufferedReader]) -> str:
    """Get file extension"""
    if isinstance(file_or_filename, BufferedReader):
        file_or_filename = file_or_filename.name
    return file_or_filename.rsplit(".", 1)[1].lower() if "." in file_or_filename else ""
