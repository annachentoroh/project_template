def output_text_to_console(text):
    """ Function to output text to console """
    print(text)
def write_text_to_python_builtin(filepath, text):
    """ Function to write text to file using builtin python functions """
    with open(filepath, mode="w", encoding="utf-8") as f:
        f.write(text)