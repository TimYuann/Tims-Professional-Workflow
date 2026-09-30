import unittest

from src.labels import normalize_label


class WhitespaceRunTests(unittest.TestCase):
    def test_collapses_mixed_internal_whitespace_run(self):
        self.assertEqual(normalize_label("alpha \t\n beta"), "ALPHA BETA")

    def test_collapses_multiple_runs_around_punctuation(self):
        self.assertEqual(normalize_label("north\t-\n star"), "NORTH - STAR")

    def test_empty_string_becomes_empty(self):
        self.assertEqual(normalize_label(""), "")


if __name__ == "__main__":
    unittest.main()
