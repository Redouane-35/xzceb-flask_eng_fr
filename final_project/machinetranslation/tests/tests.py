""" Test module """
import unittest
from translator import english_to_french , french_to_english
class TestEnglishToFrench (unittest.TestCase):
    """ This class is for testing english_to_french() """
    def test1(self) :
        """ This is for testing """
        self.assertEqual(english_to_french("Good") , "Bonne")
        self.assertEqual(english_to_french("Take") , "Prendre")
        self.assertEqual(english_to_french("Love") , "Amour")
        self.assertEqual(english_to_french("Hello") , "Bonjour")
        # self.assertEqual(english_to_french(""),"") #null test
class TestFrenchToEnglish (unittest.TestCase):
    """ This class is for testing french_to_english() """
    def test1(self) :
        """ This is for testing """
        self.assertEqual(french_to_english("Salut")   , "Hi")
        self.assertEqual(french_to_english("chanter") , "Sing")
        self.assertEqual(french_to_english("Amour")   , "Love")
        self.assertEqual(french_to_english("Bonjour") , "Hello")
        # self.assertEqual(french_to_english(""),"") #null test
unittest.main()
