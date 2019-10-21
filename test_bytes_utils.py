import unittest

from webscraping.processors.bytes_utils import get_multiplier

class TestBytesUtils(unittest.TestCase):

    def test_bytes(self):
        self.assertEqual(get_multiplier("Bytes"), 1, "Should be 1")

    def test_kb(self):
        self.assertEqual(get_multiplier("KB"), 1000, "Should be 1000")

if __name__ == '__main__':
    unittest.main()