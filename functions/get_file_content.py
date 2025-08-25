import os
from config import CHARS_MAX_LENGTH

def get_file_content(working_dir, file_path):
    try:
        full_file_path = os.path.join(working_dir, file_path)
        abspath_wdir = os.path.abspath(working_dir) + "/"
        abspath_file = os.path.abspath(full_file_path)

        if not abspath_file.startswith(abspath_wdir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abspath_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abspath_file, 'r') as file:
            file_content_string = file.read()
            if len(file_content_string) > CHARS_MAX_LENGTH:
                return file_content_string[:CHARS_MAX_LENGTH] + f' [...File "{file_path}" truncated at 10000 characters]'
            
            return file_content_string 

        
    except Exception as e:
        return f"Error: {e}"