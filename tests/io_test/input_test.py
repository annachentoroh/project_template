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


    def test_not_null_pandas(self):
        file = read_from_file_pandas("data/test.txt")
        self.assertIsNotNone(file)

    def test_return_dataframe_pandas(self):
        result = read_from_file_pandas("data/test.txt")
        self.assertIsInstance(result, pandas.DataFrame)

    def test_if_text_in_column_pandas(self):
        result = read_from_file_pandas("data/test.txt")
        self.assertIn("Today is wonderful day", result.columns)