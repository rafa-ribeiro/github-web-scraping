import unittest
import os

from webscraping.processors.files import write_file, open_file

class TestFiles(unittest.TestCase):

    def test_sucessful(self):
        path_name = os.path.join(os.getcwd(), "test_file.txt")
        content = "test"
        write_file(path_name, content)		
        self.assertEqual(open_file(path_name), content, "Should be " + content)
        os.remove(path_name)

    def test_fail(self):
        path_name = os.path.join(os.getcwd(), "test_file.txt")
        self.assertRaises(Exception, open_file, path_name)
