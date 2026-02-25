import unittest
import pandas
from app.io.input import read_from_file_python_builtin, read_from_file_pandas

class InputTest(unittest.TestCase):
    def test_not_null_python_builtin(self):
        file = read_from_file_python_builtin("data/test.txt")
        self.assertIsNotNone(file)

    def test_return_result_python_builtin(self):
        result = read_from_file_python_builtin("data/test.txt")
        self.assertEqual(result, "Today is wonderful day")

    def test_return_str_python_builtin(self):
        string = read_from_file_python_builtin("data/test.txt")
        self.assertIsInstance(string, str)

    def test_read_from_file_pandas(self):
        pass