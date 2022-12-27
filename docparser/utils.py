import os
from io import BufferedReader
from typing import Tuple, Union


def get_file_name_and_ext(
    file_or_filename: Union[str, BufferedReader]
) -> Tuple[str, str]:
    """Get file extension"""
    filename = get_file_name(file_or_filename)
    ext = filename.rsplit(".", 1)[1]
    return (filename, ext.lower())


def get_file_name(file_or_filename: Union[str, BufferedReader]) -> str:
    if isinstance(file_or_filename, BufferedReader):
        return file_or_filename.name
    return os.path.basename(file_or_filename)
