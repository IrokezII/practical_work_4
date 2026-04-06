import unittest
from data_processor2 import (
    parse_numbers,
    process_numbers,
    process_string,
    count_vowels,
    is_palindrome
)

class TestDataProcessor(unittest.TestCase):

    # ---------- parse_numbers ----------
    def test_parse_numbers_valid(self):
        self.assertEqual(parse_numbers("1 2 3"), [1, 2, 3])

    def test_parse_numbers_spaces(self):
        self.assertEqual(parse_numbers("  10   20  30  "), [10, 20, 30])

    def test_parse_numbers_empty(self):
        self.assertEqual(parse_numbers(""), [])
        self.assertEqual(parse_numbers("   "), [])

    def test_parse_numbers_single(self):
        self.assertEqual(parse_numbers("42"), [42])

    def test_parse_numbers_negative(self):
        self.assertEqual(parse_numbers("-1 -2 -3"), [-1, -2, -3])

    # ---------- process_numbers ----------
    def test_process_numbers_normal(self):
        result = process_numbers([1, 2, 3, 4])
        self.assertEqual(result["sum"], 10)
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 4)
        self.assertEqual(result["avg"], 2.5)
        self.assertEqual(result["count"], 4)

    def test_process_numbers_empty(self):
        result = process_numbers([])
        self.assertEqual(result["sum"], 0)
        self.assertIsNone(result["min"])
        self.assertIsNone(result["max"])
        self.assertIsNone(result["avg"])
        self.assertEqual(result["count"], 0)

    def test_process_numbers_single(self):
        result = process_numbers([7])
        self.assertEqual(result["sum"], 7)
        self.assertEqual(result["min"], 7)
        self.assertEqual(result["max"], 7)
        self.assertEqual(result["avg"], 7.0)

    # ---------- process_string ----------
    def test_process_string_upper(self):
        self.assertEqual(process_string("hello", "upper"), "HELLO")

    def test_process_string_lower(self):
        self.assertEqual(process_string("HELLO", "lower"), "hello")

    def test_process_string_reverse(self):
        self.assertEqual(process_string("hello", "reverse"), "olleh")

    def test_process_string_unknown_mode(self):
        self.assertEqual(process_string("hello", "unknown"), "hello")

    # ---------- count_vowels ----------
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)      # e, o
        self.assertEqual(count_vowels("HELLO"), 2)      # E, O
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("Python"), 1)

    # ---------- is_palindrome ----------
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("A man a plan a canal panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

if __name__ == "__main__":
    unittest.main()