# What is docparser?
docparser is python package that extract text form a DOCX document.

## Installation

```bash
pip install python-docparser
```

## Usage

```python
from docparser import parse 

document = parse("your_docx_document")
print(document.content)
```
