import os

def write_file(working_directory, file_path, content):

    abspath_wd = os.path.abspath(working_directory)
    abspath_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not abspath_file.startswith(abspath_wd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abspath_file):
        try:
            dir_name = os.path.dirname(abspath_file)
            os.makedirs(dir_name, exist_ok=True)
        except Exception as e:
            return f'Error: creating directory: {e}'
            
    if os.path.exists(abspath_file) and not os.path.isfile(abspath_file):
        return f'Error: "{file_path}" is a directory, not a file'
        
    try:

        with open(abspath_file, 'w') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'
    
