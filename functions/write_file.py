import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a content of the specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path is a file path, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content is written to the file from the file_path."
            )
        },
    ),
)

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
        return f'Error: writing to file: {e}'
    
