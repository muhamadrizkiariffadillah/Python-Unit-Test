import unittest


class TestSplitMethod(unittest.TestCase):
    def test_split(self):
        value = "Muhamad Rizki"
        test = value.split(" ")
        expect = ["Muhamad", "Rizki"]
        self.assertEqual(test, expect)

    def split_by_coma(self):
        actual = "Muhamad,Rizki,Arif,Fadillah".split(",")
        expect = ["Muhamad", "Rizki", "Arif", "Fadillah"]
        self.assertEqual(actual, expect)
