from pathlib import Path
from unittest import TestCase

from stew.stew import Stew


class TestOne(TestCase):
    def test_one(self):
        strings_path = Path('tests/strings.stew')
        strings_txt = Stew(strings_path)
        self.assertEqual(len(strings_txt.terms), 2)
        self.assertEqual(len(strings_txt.terms['[string_one]']), 3)
        self.assertEqual(len(strings_txt.terms['[string_one]']['ru']), 4)

    def test_formatted(self):
        strings_path = Path('tests/strings.stew')
        strings_txt = Stew(strings_path)

        l = list(strings_txt.formatted())
        print()
        for s in l:
            print(s)
        print('----')
