from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "main.py")
    print("Result of calculator and main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result of calculator and pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result of calculator and /bin/cat")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result of calculator and pkg/does_not_exist.py")
    print(result)

if __name__ == "__main__":
    test()