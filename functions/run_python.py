import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abspath_file = os.path.abspath(os.path.join(working_directory, file_path))
    abspath_wd = os.path.abspath(working_directory)

    if not abspath_file.startswith(abspath_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abspath_file):
        return f'Error: File "{file_path}" not found.'
    
    if not (os.path.isfile(abspath_file) and abspath_file.endswith(".py")):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        cli = ['python', abspath_file] + args
        completed_process = subprocess.run(args=cli, capture_output=True, timeout=30, encoding='utf-8', cwd=abspath_wd)
        stdoutput = completed_process.stdout
        stderror = completed_process.stderr
        exit_code = completed_process.returncode

        return_str = f'STDOUT: {stdoutput}\nSTDERR: {stderror}'

        if exit_code != 0:
            return f'Process exited with code {exit_code}\n{return_str}'
        
        if not (stderror or stdoutput):
            return f'No output produced'
        
        return return_str
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
