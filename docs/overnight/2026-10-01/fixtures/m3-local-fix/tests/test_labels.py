import unittest

from src.labels import normalize_label


class NormalizeLabelTests(unittest.TestCase):
    def test_collapses_internal_whitespace(self):
        self.assertEqual(normalize_label(" \tNorthern   Star\n"), "NORTHERN STAR")

    def test_preserves_punctuation(self):
        self.assertEqual(normalize_label("north-star"), "NORTH-STAR")

    def test_whitespace_only_becomes_empty(self):
        self.assertEqual(normalize_label(" \t\n"), "")

    def test_non_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            normalize_label(None)


if __name__ == "__main__":
    unittest.main()
