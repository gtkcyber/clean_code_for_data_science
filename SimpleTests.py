import unittest
from count_vowels import count_vowels

class SimpleTests(unittest.TestCase):
    def test_vowel_con_ratio(self):
        self.assertEqual(count_vowels.vowel_consonant_ratio('encylopedia'), 1.2)

    def test_empty_string(self):
        self.assertEqual(count_vowels.vowel_consonant_ratio(''), 0)


if __name__ == '__main__':
    unittest.main(argv=['ignored'])