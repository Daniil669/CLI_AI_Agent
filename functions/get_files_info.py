import os

def get_files_info(working_directory, directory="."):
    try:
        absolute_path_dir = os.path.abspath(os.path.join(working_directory, directory))
        absolute_path_working_dir = os.path.abspath(working_directory)

        if not absolute_path_dir.startswith(absolute_path_working_dir+"/") and absolute_path_dir != absolute_path_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(absolute_path_dir):
            return f'Error: "{directory}" is not a directory'
    
        dir_info = []
        for item in os.listdir(absolute_path_dir):
            item_path = os.path.join(absolute_path_dir, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            dir_info.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}\n")
    except Exception as e:
        return f"Error: {e}"

    return '\n'.join(dir_info)