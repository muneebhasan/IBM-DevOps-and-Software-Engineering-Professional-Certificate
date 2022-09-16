import unittest
from translator import english_to_french,french_to_english

class Test(unittest.TestCase):
    def test_english(self):
        self.assertEqual(english_to_french("My name is Muneeb"),"Mon nom est Muneeb")

        self.assertNotEqual(english_to_french("My name is Muneeb"),"Hello My name is Munteb")
    def test_French(self):
        self.assertEqual(french_to_english("Mon nom est Muneeb"),"My name is Muneeb")

        self.assertNotEqual(english_to_french("Mon nom est Muneeb"),"Hello My name is Munteb")
if __name__ == '__main__':
    unittest.main()
