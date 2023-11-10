import unittest
from string6 import StringModule

class TestStringModule(unittest.TestCase):

    def test_count_letters(self):
        self.assertEqual(StringModule.count_letters("Hello123"), 5)
        self.assertEqual(StringModule.count_letters("Spaces and numbers 123!"), 16)
        self.assertEqual(StringModule.count_letters(""), 0)

    def test_count_words(self):
        self.assertEqual(StringModule.count_words("Hello World"), 2)
        self.assertEqual(StringModule.count_words("This is a sentence."), 4)
        self.assertEqual(StringModule.count_words(""), 0)

    def test_count_vowels(self):
        self.assertEqual(StringModule.count_vowels("Hello"), 2)
        self.assertEqual(StringModule.count_vowels("Python"), 1)
        self.assertEqual(StringModule.count_vowels("AEIOU"), 5)
        self.assertEqual(StringModule.count_vowels(""), 0)

    def test_concatenate_strings(self):
        self.assertEqual(StringModule.concatenate_strings("Hello", " World"), "Hello World")
        self.assertEqual(StringModule.concatenate_strings("", "Python"), "Python")
        self.assertEqual(StringModule.concatenate_strings("Concatenate", ""), "Concatenate")

    def test_multiply_string(self):
        self.assertEqual(StringModule.multiply_string("Hello", 3), "HelloHelloHello")
        self.assertEqual(StringModule.multiply_string("", 5), "")
        self.assertEqual(StringModule.multiply_string("Python", 0), "")
        self.assertEqual(StringModule.multiply_string("GPT-3", 1), "GPT-3")

if __name__ == '__main__':
    unittest.main(exit=True)
