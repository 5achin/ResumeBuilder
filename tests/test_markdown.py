import unittest

from resumebuilder.util.markdown import MarkdownFormatter


class MarkdownDecoratorsTestCase(unittest.TestCase):
    SAMPLE_TEXT = "Sample Text"

    def setUp(self) -> None:
        self.md = MarkdownFormatter()

    def test_header(self):
        self.assertEqual(
            self.md.header(self.SAMPLE_TEXT, 1),
            '#Sample Text'
        )
        self.assertEqual(
            self.md.header(self.SAMPLE_TEXT, 2),
            '##Sample Text'
        )
        self.assertEqual(
            self.md.header(self.SAMPLE_TEXT, 3),
            '###Sample Text'
        )

    def test_bold(self):
        self.assertEqual(
            self.md.bold(self.SAMPLE_TEXT),
            '**Sample Text**'
        )

    def test_italic(self):
        self.assertEqual(
            self.md.italic(self.SAMPLE_TEXT),
            '*Sample Text*'
        )

    def test_bullet_list_item(self):
        self.assertEqual(
            self.md.bullet_list_item(self.SAMPLE_TEXT),
            '+ Sample Text'
        )
