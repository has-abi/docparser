import unittest

from docparser import utils

FILE_NAME_NO_PATH = "docx_example.docx"
FILE_NAME_WITH_PATH = "/tests/docx_example.docx"


class TestDocParser(unittest.TestCase):
    def test_get_file_name_no_path(self):
        self.assertEqual(
            utils.get_file_name(FILE_NAME_NO_PATH),
            FILE_NAME_NO_PATH,
        )

    def test_get_file_name_with_path(self):
        self.assertEqual(
            utils.get_file_name(FILE_NAME_WITH_PATH),
            FILE_NAME_NO_PATH,
        )

    def test_get_file_name_and_ext(self):
        self.assertEqual(
            utils.get_file_name_and_ext(FILE_NAME_WITH_PATH),
            (FILE_NAME_NO_PATH, "docx"),
        )


if __name__ == "__main__":
    unittest.main()
