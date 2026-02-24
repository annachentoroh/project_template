from app.io.input import input_text_from_console, read_from_file_python_builtin, read_from_file_pandas
from app.io.output import output_text_to_console, write_text_to_python_builtin

def main():
    user_input = input_text_from_console()
    output_text_to_console(f"Your input is: {user_input}")

    filepath = "data/test.txt"
    write_text_to_python_builtin(filepath, "Today is wonderful day")

    filepath = "data/test.txt"
    read_text_py = read_from_file_python_builtin(filepath)
    output_text_to_console(f"Read from file with python builtin functions: {read_text_py}")

    #filepath = "data/test.txt"
    #read_text_pandas = read_from_file_pandas(filepath)
    #output_text_to_console(f"Read from file with pandas: {read_text_pandas}")

if __name__ == "__main__":
    main()