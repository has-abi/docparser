from dataclasses import dataclass
from typing import Dict


@dataclass
class Document:
    name: str
    ext: str
    content: str
    splitted_content: Dict[str, str]
