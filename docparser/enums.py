__doc__ = """
This module contains the package enums.

Enums Classes
-------------

Below is listed the enums classes within 
:py:mod:`docparser.enums`
"""


from enum import Enum

import docparser.constants as CS


class TagEnum(str, Enum):
    SPACE = CS.NSMAP + "t"
    TAB = CS.NSMAP + "tab"
    BREAK_LINE = CS.NSMAP + "br"
    CARRIAGE_RETURN = CS.NSMAP + "cr"
    PARAGRAPH = CS.NSMAP + "p"


class LayoutEnum(str, Enum):
    TAB = "\t"
    BREAK_LINE = "\n"
    MAJ_BREAK_LINE = "\n\n"
