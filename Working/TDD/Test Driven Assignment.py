import unittest
import Test_stringlib


class test_Test_stringlib(unittest.TestCase):

    def test_getstringlength_general1(self):

        self.assertEqual(3, Test_stringlib.getstringlength("abc"))

    def test_getstringlength_general2(self):

        self.assertEqual(6, Test_stringlib.getstringlength("abc123"))

    def test_getstringlength_cornercase(self):

        self.assertEqual(1, Test_stringlib.getstringlength(" "))

    def test_getstringlength_unusualcase(self):

        self.assertEqual("Enter A STRING", Test_stringlib.getstringlength(1))

    def test_lettercount_general1(self):

        self.assertEqual(1, Test_stringlib.lettercount("abc", "a"))

    def test_lettercount_general2(self):

        self.assertEqual()
