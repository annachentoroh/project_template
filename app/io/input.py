import pandas

def input_text_from_console():
    """ Function to read text from console """
    return input("Please enter a text: ")

def read_from_file_python_builtin(filepath):
    """ Function to read text from file with python built-in capabilities"""
    with open(filepath, mode="r", encoding="utf-8") as f:
        return f.read()

def read_from_file_pandas(filepath):
    """ Function to read text from file with pandas capabilities """
    return pandas.read_csv(filepath)