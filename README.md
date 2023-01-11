# What is docparser?
docparser is python package that extract text form a DOCX document.

## How to use it?

```python
from docparser import parse 

document = parse("your_docx_document")
print(document.content)
```
