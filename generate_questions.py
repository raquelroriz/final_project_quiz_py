import pandas as pd
import os

questions = [
    ["What is the correct file extension for Python files?", ".pt", ".py", ".python", ".pyt", 2],

    ["Which keyword is used to define a function in Python?", "func", "define", "def", "function", 3],

    ["What is the output of print(2 + 3 * 2)?", "10", "12", "8", "7", 3],

    ["Which data type is immutable in Python?", "list", "dictionary", "set", "tuple", 4],

    ["How do you create a comment in Python?", "// comment", "<!-- comment -->", "# comment", "/* comment */", 3],

    ["Which function is used to get user input?", "input()", "scan()", "get()", "read()", 1],

    ["What is the output of len('Python')?", "5", "6", "7", "8", 2],

    ["Which operator is used for exponentiation?", "^", "**", "%", "//", 2],

    ["What is the correct way to create a list?", "{1,2,3}", "(1,2,3)", "[1,2,3]", "<1,2,3>", 3],

    ["Which keyword is used for a loop in Python?", "repeat", "for", "loop", "iterate", 2],

    ["What does the append() method do?", "Removes an item", "Adds an item to a list", "Sorts a list", "Copies a list", 2],

    ["What is the output of bool(0)?", "True", "False", "0", "None", 2],

    ["Which statement is used to handle exceptions?", "try-except", "catch-error", "error-handling", "exception", 1],

    ["What is the output of type(3.14)?", "int", "float", "string", "double", 2],

    ["Which collection does not allow duplicate values?", "list", "tuple", "dictionary", "set", 4],

    ["What is the result of 10 // 3?", "3.33", "3", "4", "1", 2],

    ["Which method converts a string to lowercase?", "lower()", "small()", "downcase()", "min()", 1],

    ["What is the output of print('Hello' + 'World')?", "Hello World", "Hello+World", "HelloWorld", "Error", 3],

    ["Which keyword is used to create a class?", "function", "object", "class", "struct", 3],

    ["What does the range(5) function generate?", "0 to 4", "1 to 5", "0 to 5", "1 to 4", 1],

    ["Which symbol is used for logical AND?", "&", "and", "&&", "AND", 2],

    ["What is the output of print(type([]))?", "tuple", "dictionary", "list", "set", 3],

    ["Which built-in function returns the largest value?", "max()", "high()", "largest()", "top()", 1],

    ["What is the correct syntax to import a module?", "include math", "import math", "using math", "require math", 2],

    ["What is the output of 5 % 2?", "2", "2.5", "1", "0", 3],

    ["Which method removes whitespace from a string?", "trim()", "strip()", "remove()", "clean()", 2],

    ["What is the output of print(3 == 3.0)?", "False", "Error", "0", "True", 4],

    ["Which keyword is used to stop a loop?", "stop", "exit", "break", "return", 3],

    ["What does a dictionary store?", "Only numbers", "Key-value pairs", "Only strings", "Ordered duplicates", 2],

    ["Which function converts a value to an integer?", "float()", "number()", "str()", "int()", 4]
]

df = pd.DataFrame(
    questions,
    columns=["question", "option1", "option2", "option3", "option4", "correct_answer"]
)

try:
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/questions.csv", index=False)
    print("Questions have been saved successfully!")

except Exception as e:
    print(f"Error while saving file: {e}")