from functions.get_files_info import get_files_info

def test():
    dir_tests = {"calculator": [(".", "Result for current directory:\n - main.py: file_size=576 bytes, is_dir=False\n - tests.py: file_size=1343 bytes, is_dir=False\n - pkg: file_size=92 bytes, is_dir=True")
                                ,("pkg", "Result for 'pkg' directory:\n - calculator.py: file_size=1739 bytes, is_dir=False\n - render.py: file_size=768 bytes, is_dir=False"), 
                                ("/bin", "Result for '/bin' directory:\nError: Cannot list '/bin' as it is outside the permitted working directory"), 
                                ("../", "Result for '../' directory:\nError: Cannot list '../' as it is outside the permitted working directory")]}
    for working_dir in dir_tests:
        print(f"Working directory: {working_dir}")
        for dir in dir_tests[working_dir]:
            print(f"Directory: {dir[0]}")
            print(f"Expected:\n{dir[1]}")
            result = get_files_info(working_dir, dir[0])
            print(f"Actual:{result}")


if __name__ == "__main__":
    test()