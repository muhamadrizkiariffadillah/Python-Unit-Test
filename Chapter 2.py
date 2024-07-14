import unittest


class TestIsInstance(unittest.TestCase):

    def test_tuple(self):
        self.assertTrue(isinstance((), tuple))

    def test_array(self):
        self.assertTrue(isinstance([], list))

    def test_dict(self):
        self.assertTrue(isinstance({}, dict))

    def test_int(self):
        number: int = 1
        self.assertTrue(isinstance(number, int))

    def test_float(self):
        tall: float = 32.5
        self.assertTrue(isinstance(tall, float))

    def test_string(self):
        name: str = "Kibo"
        self.assertTrue(isinstance(name, str))
