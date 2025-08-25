from functions.run_python import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("Result of calculator and main.py")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result of calculator and main.py and args ['3'+'5']")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("Result of calculator and tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("Result of calculator and ../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("Result of calculator and nonexistent.py")
    print(result)

if __name__ == "__main__":
    test()