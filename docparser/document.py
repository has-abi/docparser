__doc__ = """
This is dataclass module, namely :class:`Document`, which
holds the parsed data from a document.

Classes & methods
-----------------

Below is listed the class within :py:mod:`docparser.parser`
along with possessed methods.
"""


from dataclasses import dataclass
from typing import Dict


@dataclass
class Document:
    name: str
    ext: str
    content: str
    splitted_content: Dict[str, str]
