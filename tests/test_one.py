from pathlib import Path
from unittest import TestCase

from stew.strings_txt import Stew


class TestOne(TestCase):
    def test_one(self):
        strings_path = Path('tests/strings.stew')
        strings_txt = Stew(strings_path)
        self.assertEqual(len(strings_txt.terms), 1)
        self.assertEqual(len(strings_txt.terms['[string_one]']), 3)
        self.assertEqual(len(strings_txt.terms['[string_one]']['ru']), 4)
