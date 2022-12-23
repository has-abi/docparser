from datetime import date

TEMP_DOCX_FILE = "temp/temp_doc.docx"
DOCX_EXT = "docx"
DOC_EXT = "doc"
ALLOWED_EXTS = [DOCX_EXT, DOC_EXT]
XML_BODY = "word/document.xml"
XML_HEADER = "word/header[0-9]*.xml"
XML_FOOTER = "word/footer[0-9]*.xml"
NSMAP = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ASPOSE_EVAL_STATEMENT = f"Evaluation Only\\. Created with Aspose\\.Words\\. Copyright 2003\\-{date.today().year} Aspose Pty Ltd\\.|Created with an evaluation copy of Aspose\\.Words\\. To discover the full versions of our APIs please visit: https:\\/\\/products\\.aspose\\.com\\/words\\/"
