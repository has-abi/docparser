__doc__ = """
This module contains the package utils.

Utils methods
-------------

Below is listed the package util methos within 
:py:mod:`docparser.utils`
"""


import os
from io import BufferedReader
from typing import Tuple, Union


def get_file_name_and_ext(
    file_or_filepath: Union[str, BufferedReader]
) -> Tuple[str, str]:
    """Extract the file extension and the file name
    from a file or a file name.

    Args:
        file_or_filepath (Union[str, BufferedReader]): File or file path.

    Returns:
        Tuple[str, str]: Tuple of file name and file extension
    """
    filename = get_file_name(file_or_filepath)
    ext = filename.rsplit(".", 1)[1]
    return (filename, ext.lower())


def get_file_name(file_or_filepath: Union[str, BufferedReader]) -> str:
    """Extract the file name form a file or a file path.

    Args:
        file_or_filepath (Union[str, BufferedReader]): File or a file path.

    Returns:
        str: The extracted file name.
    """
    if isinstance(file_or_filepath, BufferedReader):
        return file_or_filepath.name
    return os.path.basename(file_or_filepath)
